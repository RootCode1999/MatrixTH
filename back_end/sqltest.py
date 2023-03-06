from SQLA import CUSTOMER
from sqlalchemy import String, Column, Integer
from sqlalchemy import create_engine, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, Integer, String, DateTime, Float, func, and_, or_
from sqlalchemy.orm import sessionmaker
import random
from JsonWrap import jsonwrap
import datetime
import time
import pymysql
from functools import cmp_to_key
from Linksql import linksql

dataforum = linksql()

ans_p = dataforum.query(CUSTOMER).filter(
    CUSTOMER.cname == "lee").all()

print(ans_p)
