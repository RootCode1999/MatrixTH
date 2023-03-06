import json
from flask import request
from Linksql import linksql
from SQLA import  HISTORY
from JsonWrap import jsonwrap
from datetime import datetime, date, timedelta
import requests

def get_year_history():
    try:
        dataforum = linksql()
        today_format = datetime.today().strftime('%Y-%m-%d') + " 23:00:00"
        year_ago_format =  (datetime.today() + timedelta(-365)).strftime('%Y-%m-%d') + " 00:00:00"
        record = dataforum.query(HISTORY).filter(
            HISTORY.this_time < today_format, \
                HISTORY.this_time > year_ago_format).order_by(HISTORY.this_time).all()
        date_arry = []
        humidity_arry = []
        temperature_arry = []
        for i in record:
            thisdate = i.this_time.strftime('%Y-%m-%d %H:%M:%S')
            humidity = i.humidity
            temperature = i.temperature
            date_arry.append(thisdate.replace(' ','\n'))
            humidity_arry.append(humidity)
            temperature_arry.append(temperature)
            if(humidity < 1):
                a = 1
        res = {}
        res["date_arry"] = date_arry
        res["humidity_arry"] = humidity_arry
        res["temperature_arry"] = temperature_arry
        return jsonwrap(0,"success",res)
    except Exception as e:
        error = {}
        return jsonwrap(-1, str(e), error)
    finally:
        dataforum.commit()
        dataforum.close()

def get_predict():
    try:
        dataforum = linksql()
        res = {}
        url_head = "https://api.seniverse.com/v3/weather/daily.json?key=SRPhoLBlmtHtILmuM&location="
        local_name = "beijing"
        url_end = "&language=zh-Hans&unit=c&start=-1&days=5"
        url = url_head + local_name +url_end
        predict_str = requests.get(url)
        predict_data = json.loads(predict_str.content)["results"][0]['daily']
        humidity = []
        temperature = []
        days = []
        for i in predict_data:
            humidity.append(i["humidity"]) 
            temperature.append(i["high"])
            days.append(i["date"][5:])
        res["days"] = days
        res["humidity"] = humidity
        res["temperature"] = temperature
        if(humidity[0] == humidity[1]):
            res["humdis"] = "相较于今天没什么变化"
        if(humidity[0] > humidity[1]):
            res["humdis"] = "相较于今天会降低"
        if(humidity[0] < humidity[1]):
            res["humdis"] = "相较于今天会升高"
        if(temperature[0] == temperature[1]):
            res["tempdis"] = "相较于今天没什么变化"
        if(temperature[0] > temperature[1]):
            res["tempdis"] = "相较于今天会降低"
        if(temperature[0] < temperature[1]):
            res["tempdis"] = "相较于今天会升高"
        return jsonwrap(0,"success", res)
    except Exception as e:
        error = {}
        return jsonwrap(-1, str(e), error)
    finally:
        dataforum.commit()
        dataforum.close()