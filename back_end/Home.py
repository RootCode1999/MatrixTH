import json
from flask import request
from Linksql import linksql
from SQLA import TEMP_HUM_NOW, HISTORY
from JsonWrap import jsonwrap
from datetime import datetime, date, timedelta
import time
from tools import readrecord, writerecord

def get_temp_hum_now():
    try:
        readrecord()
        writerecord()
        dataforum = linksql()
        temp_hum_now = dataforum.query(TEMP_HUM_NOW).filter().all()
        if(temp_hum_now.__len__() > 0):
            res = {}
            temperature = 0.0
            humidity = 0.0
            for i in range(0,temp_hum_now.__len__()):
                temperature = temperature + temp_hum_now[i].temperature
                humidity = humidity + temp_hum_now[i].humidity 
            res["temperature"] =  round(temperature / temp_hum_now.__len__(), 2)
            res["humidity"] = round(humidity / temp_hum_now.__len__(), 2)
            return jsonwrap(0,"success", res)
        return jsonwrap(1,"error", res)
    except Exception as e:
        error = {}
        return jsonwrap(-1, str(e), error)
    finally:
        dataforum.commit()
        dataforum.close()

def home_get_history():
    try:
        res = {}
        dataforum = linksql()
        yesterday = datetime.today() + timedelta(-1)
        week_ago = datetime.today() + timedelta(-7)
        yesterday_format = yesterday.strftime('%Y-%m-%d') + " 23:00:00"
        week_ago_format = week_ago.strftime('%Y-%m-%d') + " 00:00:00"
        record = dataforum.query(HISTORY).filter(
            HISTORY.this_time < yesterday_format, \
                HISTORY.this_time > week_ago_format).order_by(HISTORY.this_time).all()
        date_now = record[0].this_time.strftime('%m-%d')
        temperature = 0.0
        humidity = 0.0
        count = 0
        temperature_arry = []
        humidity_arry = []
        date_arry = []
        for i in record:
            if(i.this_time.strftime('%m-%d') == date_now):
                temperature = temperature + i.temperature
                humidity = humidity + i.humidity
                count = count + 1
            else:
                temperature_arry.append(round(temperature/count,2))
                humidity_arry.append(round(humidity/count,2))
                date_arry.append(date_now)
                temperature = i.temperature
                humidity = i.temperature
                count = 0
                date_now = i.this_time.strftime('%m-%d')
        temperature_arry.append(round(temperature/count,2))
        humidity_arry.append(round(humidity/count,2))
        date_arry.append(date_now)
        res["temperature_arry"] = temperature_arry
        res["humidity_arry"] = humidity_arry
        res["date_arry"] = date_arry
        return jsonwrap(0,"success",res)
    except Exception as e:
        error = {}
        return jsonwrap(-1, str(e), error)
    finally:
        dataforum.commit()
        dataforum.close()

def judgecmp(a,b):
    if(a["date"] > b["date"]):
        return True
    return False

station_record = []

def get_station():
    try:
        res={}
        dataforum = linksql()
        temp_hum_now = dataforum.query(TEMP_HUM_NOW).filter().all()
        for i in temp_hum_now:
            dic = {}
            this_point = "station"+str(i.point)
            date = i.date.strftime('%H:%M:%S')
            temp = i.temperature
            hum = i.humidity
            dic["point"] = this_point
            dic["date"] = date
            dic["temp"] = int(temp)
            dic["hum"] = int(hum)
            station_record.append(dic)
        station_record.sort(key=lambda a:a["date"], reverse=True)
        ans = []
        index = 0
        re_len = 0
        while(index < station_record.__len__()):
            if(re_len > 7):
                break
            if(index < 3):
                ans.append(station_record[index])
                re_len = re_len + 1
                index = index + 1
            else:
                if(station_record[index]["date"] == station_record[index-1]["date"] and \
                    station_record[index]["point"] == station_record[index-1]["point"]):
                    index = index + 1
                    continue
                if(station_record[index]["date"] == station_record[index-2]["date"] and \
                    station_record[index]["point"] == station_record[index-2]["point"]):
                    index = index + 1
                    continue
                if(station_record[index]["date"] == station_record[index-3]["date"] and \
                    station_record[index]["point"] == station_record[index-3]["point"]):
                    index = index + 1
                    continue
                else:
                    ans.append(station_record[index])
                    index = index + 1
                    re_len = re_len + 1
        del station_record[index : -1]
        res["data"] = ans
        return jsonwrap(0,"sucess",res)
    except Exception as e:
        error = {}
        return jsonwrap(-1, str(e), error)
    finally:
        dataforum.commit()
        dataforum.close()
