from sqlalchemy import create_engine, Column, Float, DateTime, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class BTCData6Hrs(Base):
    __tablename__ = 'btc_data_6hrs'
    id = Column(Integer, primary_key=True)
    timestamp = Column(DateTime, nullable=False)
    low = Column(Float)
    high = Column(Float)
    open = Column(Float)
    close = Column(Float)
    volume = Column(Float)
    sma_30 = Column(Float)
    rsi = Column(Float)
    macd = Column(Float)

class BTCData15Daily(Base):
    __tablename__ = 'btc_data_15_daily'
    id = Column(Integer, primary_key=True)
    timestamp = Column(DateTime, nullable=False)
    low = Column(Float)
    high = Column(Float)
    open = Column(Float)
    close = Column(Float)
    volume = Column(Float)
    sma_30 = Column(Float)
    rsi = Column(Float)
    macd = Column(Float)

class BTCData15Hourly(Base):
    __tablename__ = 'btc_data_15_hourly'
    id = Column(Integer, primary_key=True)
    timestamp = Column(DateTime, nullable=False)
    low = Column(Float)
    high = Column(Float)
    open = Column(Float)
    close = Column(Float)
    volume = Column(Float)
    sma_30 = Column(Float)
    rsi = Column(Float)
    macd = Column(Float)

DATABASE_URI = 'postgresql+psycopg2://nikhilrazab-sekh@localhost:5432/cryptovaultdb'
engine = create_engine(DATABASE_URI)
Session = sessionmaker(bind=engine)

if __name__ == "__main__":
    Base.metadata.create_all(engine)
    print("Coinbase BTC data tables have been created successfully.")
