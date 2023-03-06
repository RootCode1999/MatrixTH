from Linksql import linksql
from flask import request
from JsonWrap import jsonwrap
from SQLA import WARNING, HISTORY
from datetime import datetime, date, timedelta
from sqlalchemy import desc

def set_temperature_threshold():
    try:
        res = {}
        temp_top = request.args.get('temp_top')
        temp_low = request.args.get('temp_low')
        cid = int(request.args.get('cid'))
        dataforum = linksql()
        temp_top_format = round(float(temp_top),2)
        temp_low_format = round(float(temp_low),2)
        ans_p = dataforum.query(WARNING).filter(WARNING.cid == cid).first()
        if(ans_p is None):
            newone = WARNING(cid = cid, temp_low = temp_low_format, temp_top=temp_top_format)
            dataforum.add(newone)
            dataforum.commit()
        else:
            ans_p.temp_low = temp_low_format
            ans_p.temp_top = temp_top_format
            dataforum.commit()
        return jsonwrap(0,"success",res)
    except Exception as e:
        error = {}
        return jsonwrap(-1, str(e), error)
    finally:
        dataforum.commit()
        dataforum.close()


def set_humidity_threshold():
    try:
        res = {}
        hum_top = request.args.get('hum_top')
        hum_low = request.args.get('hum_low')
        cid = int(request.args.get('cid'))
        dataforum = linksql()
        hum_top_format = round(float(hum_top),2)
        hum_low_format = round(float(hum_low),2)
        ans_p = dataforum.query(WARNING).filter(WARNING.cid == cid).first()
        if(ans_p is None):
            newone = WARNING(cid = cid, hum_low = hum_low_format, hum_top=hum_top_format)
            dataforum.add(newone)
            dataforum.commit()
        else:
            ans_p.hum_low = hum_low_format
            ans_p.hum_top = hum_top_format
            dataforum.commit()
        return jsonwrap(0,"success",res)
    except Exception as e:
        error = {}
        return jsonwrap(-1, str(e), error)
    finally:
        dataforum.commit()
        dataforum.close()

def get_warning():
    try:
        cid = int(request.args.get('cid'))
        dataforum = linksql()
        threshold = dataforum.query(WARNING).filter(WARNING.cid == cid).first()
        temp_top_format = threshold.temp_top
        temp_low_format = threshold.temp_low
        hum_top_format = threshold.hum_top
        hum_low_format = threshold.hum_low
        today_format = datetime.today().strftime('%Y-%m-%d') + " 23:00:00"
        month_ago_format =  (datetime.today() + timedelta(-15)).strftime('%Y-%m-%d') + " 00:00:00"
        warn_arry = dataforum.query(HISTORY).filter(
                HISTORY.this_time < today_format, \
                    HISTORY.this_time > month_ago_format).order_by(desc(HISTORY.this_time)).all()
        res = {}
        ans_arry = []
        for i in warn_arry:
            temp = {}
            temp["color"] = "#ae2012"
            temp["size"] = "large"
            if(i.temperature > temp_top_format):
                temp["content"] = "此时温度偏高，大约有：" + str(i.temperature) + "°C"
                temp["timestamp"] = i.this_time.strftime('%Y-%m-%d %H:%M:%S')
                ans_arry.append(temp)
                continue
            if(i.temperature < temp_low_format):
                temp["content"] = "此时温度偏低，大约有：" + str(i.temperature) + "°C"
                temp["timestamp"] = i.this_time.strftime('%Y-%m-%d %H:%M:%S')
                ans_arry.append(temp)
                continue
            if(i.humidity > hum_top_format):
                temp["content"] = "此时湿度偏高，大约有：" + str(i.humidity) + "%"
                temp["timestamp"] = i.this_time.strftime('%Y-%m-%d %H:%M:%S')
                ans_arry.append(temp)
                continue
            if(i.humidity < hum_low_format):
                temp["content"] = "此时湿度偏低，大约有：" + str(i.humidity) + "%"
                temp["timestamp"] = i.this_time.strftime('%Y-%m-%d %H:%M:%S')
                ans_arry.append(temp)
                continue
        res["warn_arry"] = ans_arry
        return jsonwrap(0,"success",res)
    except Exception as e:
        error = {}
        return jsonwrap(-1, str(e), error)
    finally:
        dataforum.commit()
        dataforum.close()
