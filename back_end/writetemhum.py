from numpy import record
from Linksql import linksql
from SQLA import HISTORY, WARNING, CUSTOMER
from tools import readrecord
from datetime import datetime, date, timedelta
import time
from sendmail import sendmail

def writetemhum():
    try:
        dataforum = linksql()
        record = readrecord()
        tem = 0.0
        hum = 0.0
        for i in record:
            tem = tem + (float)(i['temperature'])
            hum = hum + (float)(i['humidity'])
        today_format = datetime.today().strftime('%Y-%m-%d') + " 23:00:00"
        ago_format =  (datetime.today() + timedelta(-5)).strftime('%Y-%m-%d') + " 00:00:00"
        his_record = dataforum.query(HISTORY).filter(
            HISTORY.this_time < today_format, \
                HISTORY.this_time > ago_format).order_by(HISTORY.this_time.desc())[0]
        tem = round(tem / 3.0, 2)
        hum = round(hum / 3.0, 2)
        now = datetime.now() 
        sub = (now - his_record.this_time).seconds

        ###warnning
        send_time = now + timedelta(hours = -1)
        check_time = send_time.strftime('%Y-%m-%d %H:%M:%S')
        from sqlalchemy import or_
        warners = dataforum.query(WARNING).filter(or_(WARNING.hum_low > hum, WARNING.hum_top < hum,\
            WARNING.temp_low > tem, WARNING.temp_top < tem)).all()
        if(warners.__len__()>0):
            content = "Warnning! The Humidity is " + str(hum) +", the Temperature is" + str(tem)
            receiver = []
            for i in warners:
                this_time = i.send_time.strftime('%Y-%m-%d %H:%M:%S')
                if(this_time < check_time):
                    this_warner = dataforum.query(CUSTOMER).filter(CUSTOMER.cid == i.cid).first()
                    receiver.append(this_warner.email)
                    i.send_time = now.strftime('%Y-%m-%d %H:%M:%S')
            sendmail(content,receiver)
            
        if(sub > 14400):
            now_time = his_record.this_time + timedelta(hours=4)
            newone = HISTORY(this_time=now_time, temperature=tem, humidity=hum)
            dataforum.add(newone)
            dataforum.commit()
    except Exception as e:
        print(e)
    finally:
        dataforum.commit()
        dataforum.close()