# import package
import requests
import json
import time
import datetime
import calendar

'''
input  : url
output : html_txt 
'''
def get_html(url):
    get_html = requests.get(url)
    text = get_html.text
    return text

'''
input  : year and month
output : the last day
'''
def getLastDay(year, month):
    weekDay,monthCountDay = calendar.monthrange(year,month)
    lastDay = datetime.date(year,month,day=monthCountDay)
    return lastDay.day

def get_txt(year, month):
    # str_station is the id of Observatory 
    # url = str_url_head + str_month + str_start + str_end + str_station
    str_url_head = "http://weather.uwyo.edu/cgi-bin/sounding?region=naconf&TYPE=TEXT%3ALIST&"
    str_year = "YEAR="
    str_month = "&MONTH="
    str_start = "&FROM=0100" 
    str_end = "&TO=" # style : &TO=3112
    str_station = "&STNM=72493"
    lastday = getLastDay(year, month)
    url = str_url_head + str_year+ str(year) + str_month + str(month) + str_start + \
        str_end + str(lastday) + "12" + str_station
    print(url)
    html = get_html(url)
    time.sleep(2)
    return html

'''
main
'''
if __name__ == '__main__':
    for year in range(2010, 2022):
        for month in range(1, 13):
            print( str(year) + "-" + str(month))
            html = get_txt(year, month)
            file_name = "./data/" + str(year) + "-" + str(month) + ".html"
            with open(file_name, 'w') as f:
                f.write(html)
            f.close()