import random
from Linksql import linksql
from SQLA import TEMP_HUM_NOW

def generate_random_str(randomlength=32):
    random_str = ''
    base_str = 'ABCDEFGHIGKLMNOPQRSTUVWXYZabcdefghigklmnopqrstuvwxyz0123456789'
    if(randomlength==4):
        base_str = '0123456789'
    length = len(base_str) - 1
    for i in range(randomlength):
        random_str += base_str[random.randint(0, length)]
    return random_str

import os
import time

def getrecord():
    os.system("/home/pi/matrixth/back_end/get.sh")
    time.sleep(10)

import json
def readrecord():
    res = []
    with open("./record.json",'r') as load_f:
        load_dict = json.load(load_f,encoding='UTF-8')
        points = [0,0,0]
        res = []
        for i in range(0, load_dict.__len__()):
            this_massage = load_dict[i]
            point = this_massage[0:4]
            index = this_massage.find(":")
            tem = this_massage[index+1:index+6]
            index = this_massage.find(":",index+2)
            hum =  this_massage[index+1:index+6]
            temp={}
            temp["point"] = int(point[3:4])
            temp["temperature"] = tem
            temp["humidity"] = hum
            if(points[temp["point"]-1]==0):
                points[temp["point"]-1] = 1
                res.append(temp)
        return res

import datetime
def writerecord():
    try:
        #getrecord
        res = readrecord()
        dataforum = linksql()
        points = [0,0,0]
        for i in range(res.__len__()):
            point_record = res[i]
            this_point = dataforum.query(TEMP_HUM_NOW).filter( TEMP_HUM_NOW.point == point_record["point"]).first()
            this_point.temperature = float(point_record["temperature"])
            this_point.humidity = float(point_record["humidity"])
            nowtime = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
            this_point.date = nowtime
            points[point_record["point"] - 1] = 1
            dataforum.commit()

    except Exception as e:
        error = {}
        print(e)
    finally:
        dataforum.commit()
        dataforum.close()


