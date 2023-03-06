from Warning import set_temperature_threshold, set_humidity_threshold, get_warning
from History import get_year_history, get_predict
from Home import get_temp_hum_now, home_get_history, get_station
from Regist import regist, send_vercode
from Login import login
from flask import Flask
from sqlalchemy import true
from Test import test
from flask_mail import Mail, Message
import os
from flask_cors import *
from flask_apscheduler import APScheduler
from NewThread import NewThread

app = Flask(__name__)

mail = Mail()

app = Flask(__name__)

CORS(app,  resources=r"/*")

app.add_url_rule(rule='/test', view_func=test, methods=['POST', 'GET'])

app.add_url_rule(rule='/login', view_func=login, methods=['POST', 'GET'])

app.add_url_rule(rule='/regist', view_func=regist, methods=['POST', 'GET'])
app.add_url_rule(rule='/sendcode', view_func=send_vercode,
                 methods=['POST', 'GET'])

app.add_url_rule(rule='/gettemphumnow',
                 view_func=get_temp_hum_now, methods=['POST', 'GET'])
app.add_url_rule(rule='/homegethistory',
                 view_func=home_get_history, methods=['POST', 'GET'])
app.add_url_rule(rule='/get_station', view_func=get_station,
                 methods=['POST', 'GET'])

app.add_url_rule(rule='/get_year_history',
                 view_func=get_year_history, methods=['POST', 'GET'])
app.add_url_rule(rule='/get_predict', view_func=get_predict,
                 methods=['POST', 'GET'])

app.add_url_rule(rule='/set_temperature_threshold',
                 view_func=set_temperature_threshold, methods=['POST', 'GET'])
app.add_url_rule(rule='/set_humidity_threshold',
                 view_func=set_humidity_threshold, methods=['POST', 'GET'])
app.add_url_rule(rule='/get_warning', view_func=get_warning,
                 methods=['POST', 'GET'])

if __name__ == '__main__':
    # 创建子线程
    # 启动
    t1 = NewThread()
    t1.start()
    app.run(debug=True, host='0.0.0.0', port=5000, threaded=True)
