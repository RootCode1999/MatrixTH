from flask import request
from SQLA import CUSTOMER, VERIFICATION
from JsonWrap import jsonwrap
from Linksql import linksql
from sqlalchemy import func
from tools import generate_random_str
from sendmail import sendmail


def regist():
    try:
        res = {}
        dataforum = linksql()
        user_name = request.args.get('username')
        password = request.args.get('passwd')
        verification_code = request.args.get('ver_code')
        email = request.args.get('email')
        if (user_name is None or password is None):
            return jsonwrap(1, "Something empty.", res)
        if (dataforum.query(CUSTOMER).filter(CUSTOMER.cname == user_name).all() or user_name == None):
            dataforum.close()
            return jsonwrap(2, "Username already exists.", res)
        ver = dataforum.query(VERIFICATION).filter(VERIFICATION.email == email,
                                                   VERIFICATION.code == verification_code).all()
        if (ver.__len__() == 0):
            return jsonwrap(3, "You get wrong verification code or email.", res)
        if (dataforum.query(CUSTOMER).filter(CUSTOMER.email == email).all()):
            dataforum.close()
            return jsonwrap(4, "email already exists.", res)
        num = dataforum.query(func.count('*')).select_from(CUSTOMER).scalar()
        num = num + 1
        this_cid = str(num)
        newcustomer = CUSTOMER(cid=this_cid, cname=user_name,
                               passwd=password, flag=0, email=email)
        dataforum.add(newcustomer)
        dataforum.commit()
        res['cid'] = this_cid
        res['cname'] = user_name
        res['passwd'] = password
        dataforum.close()
        return jsonwrap(0, "success", res)
    except Exception as e:
        error = {}
        return jsonwrap(-1, str(e), error)
    finally:
        dataforum.commit()
        dataforum.close()


def send_vercode():
    try:
        res = {}
        user_email = request.args.get('email')
        if (user_email is None):
            return jsonwrap(1, "Something empty.", res)
        dataforum = linksql()
        dataforum.query(VERIFICATION).filter(
            VERIFICATION.email == user_email).delete()
        ver_code = generate_random_str(4)
        new_ver = VERIFICATION(email=user_email, code=ver_code)
        dataforum.add(new_ver)
        res["email"] = user_email
        res["vercode"] = ver_code
        content = "Your verification code is: " + ver_code + "."
        sendmail(content, user_email)
        return jsonwrap(0, "success", res)
    except Exception as e:
        error = {}
        return jsonwrap(-1, str(e), error)
    finally:
        dataforum.commit()
        dataforum.close()
