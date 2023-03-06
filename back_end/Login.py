from flask import redirect, request, url_for
from sqlalchemy import String, Column, Integer
from sqlalchemy import create_engine, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, Integer, String, DateTime, Float, func, and_, or_
from sqlalchemy.orm import sessionmaker
import datetime
import time
from SQLA import CUSTOMER, SESSION
from flask import request
from JsonWrap import jsonwrap
from Linksql import linksql
from tools import generate_random_str


def login():
    try:
        res = {}
        user_name = request.args.get('name')
        password = request.args.get('passwd')
        if (user_name == None or password == None or user_name == '' and password == ''):
            return jsonwrap(1, "Something empty.", res)
        dataforum = linksql()
        ans_p = dataforum.query(CUSTOMER).filter(
            CUSTOMER.cname == user_name, CUSTOMER.passwd == password).all()
        res = {}
        if (len(ans_p) > 0):
            user_now = ans_p[0]
            nowtime = time.strftime(
                '%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
            dataforum.query(SESSION).filter(
                SESSION.cid == user_now.cid).delete()
            ranstr = generate_random_str()
            nowtime = time.strftime(
                '%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
            newsession = SESSION(sid=ranstr, cid=user_now.cid, dt=nowtime)
            dataforum.add(newsession)
            dataforum.commit()
            res['sid'] = ranstr
            res['cname'] = user_now.cname
            res['logintime'] = nowtime
            res['cid'] = user_now.cid
            dataforum.close()
            return jsonwrap(0, "success", res)
        else:
            dataforum.close()
            return jsonwrap(2, "Pelease check password and username again.", res)
    except Exception as e:
        error = {}
        return jsonwrap(-1, str(e), error)
    finally:
        dataforum.commit()
        dataforum.close()
