from sqlalchemy import Column, String, create_engine, Integer, DateTime, Float
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey

# 创建对象的基类:
# raspberrypi.local
# localhost
Base = declarative_base()
engine = create_engine(
    'mysql+pymysql://root:raspberry@localhost:3306/matrixth')
Base = declarative_base((engine))
Session = sessionmaker(engine)
session = Session()


class SESSION(Base):
    # 表的名字:
    __tablename__ = 'session'
    # 表的结构:
    sid = Column(String(256), primary_key=True)
    cid = Column(String(256))
    dt = Column(DateTime)


# 定义User对象:
class CUSTOMER(Base):
    # 表的名字:
    __tablename__ = 'Customer'
    # 表的结构:
    cid = Column(String(256), primary_key=True)
    cname = Column(String(256))
    passwd = Column(String(256))
    flag = Column(Integer)
    email = Column(String(256))


class VERIFICATION(Base):
    # 表的名字:
    __tablename__ = 'verification'
    # 表的结构:
    email = Column(String(256), primary_key=True)
    code = Column(String(256))

class TEMP_HUM_NOW(Base):
    # 表的名字:
    __tablename__='temp_hum_now'
    # 表的结构:
    point = Column(Integer,primary_key=True)
    date = Column(DateTime)
    temperature = Column(Float)
    humidity = Column(Float)
    flag = Column(Integer)

class HISTORY(Base):
    __tablename__ = 'history'
    this_time = Column(DateTime, primary_key=True)
    temperature = Column(Float)
    humidity = Column(Float)

class WARNING(Base):
    __tablename__ = 'warning'
    cid = Column(Integer,primary_key=True)
    temp_top = Column(Float)
    temp_low = Column(Float)
    hum_top = Column(Float)
    hum_low = Column(Float)
    send_time = Column(DateTime)

