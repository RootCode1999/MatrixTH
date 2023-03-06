from sqlalchemy import String, Column, Integer
from sqlalchemy import create_engine, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, Integer, String, DateTime, Float, func, and_, or_
from sqlalchemy.orm import sessionmaker
from JsonWrap import jsonwrap
from functools import cmp_to_key


def linksql():
    Base = declarative_base()
    # localhost
    # raspberrypi.local
    engine = create_engine(
        'mysql+pymysql://root:raspberry@localhost:3306/matrixth')
    Base = declarative_base((engine))
    Session = sessionmaker(engine)
    dataforum = Session()
    return dataforum
