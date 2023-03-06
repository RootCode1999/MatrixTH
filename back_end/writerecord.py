from operator import index
from Linksql import linksql
from SQLA import HISTORY
import datetime, time

with open("../data/2022.csv",encoding="unicode_escape") as f:
    dataforum = linksql()
    count = 0
    for line in f:
        if(count == 0):
            count = count + 1
            continue
        count = count + 1
        date_record = datetime.datetime.strptime(line[0:16], '%d.%m.%Y %H:%M')
        this_time =  date_record.strftime('%Y-%m-%d %H:%M')
        flag = dataforum.query(HISTORY).filter(
            HISTORY.this_time == this_time).all().__len__()
        if(flag > 0):
            print("exist")
            continue
        index1 = line.find(",")
        index2 = line.find(",",index1+1)
        if(index1+1 == index2):
            print("no temperature")
            continue
        tem = float(line[index1+1:index2])
        for i in range(0,4):
            index1 = line.find(",", index1+1)
        if(index1 + 1 >= line.__len__() - 1):
            print("no humidity")
            continue
        index2 = line.find(",",index1+1)
        index3 = line.find("\n",index1+1)
        if(index2 != -1):
            if(index1+1==index2):
                print("no humdity")
                continue
            hum = float(line[index1+1:index2])
        else:
            hum = float(line[index1+1:-1])
        newone = HISTORY(this_time=this_time, temperature=tem, humidity=hum)
        dataforum.add(newone)
        dataforum.commit()
        print(this_time)
    dataforum.commit()
    dataforum.close()
