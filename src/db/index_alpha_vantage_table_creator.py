from sqlalchemy import create_engine, Column, Float, Integer, DateTime, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

# Hourly Data Tables
class DIAHourly(Base):
    __tablename__ = 'dia_hourly'
    __table_args__ = {'schema': 'index_alpha_vantage'}
    id = Column(Integer, primary_key=True)
    timestamp = Column(DateTime, nullable=False)
    open = Column(Float)
    high = Column(Float)
    low = Column(Float)
    close = Column(Float)
    volume = Column(Float)

class GOLDHourly(Base):
    __tablename__ = 'gold_hourly'
    __table_args__ = {'schema': 'index_alpha_vantage'}
    id = Column(Integer, primary_key=True)
    timestamp = Column(DateTime, nullable=False)
    open = Column(Float)
    high = Column(Float)
    low = Column(Float)
    close = Column(Float)
    volume = Column(Float)

class GLDHourly(Base):
    __tablename__ = 'gld_hourly'
    __table_args__ = {'schema': 'index_alpha_vantage'}
    id = Column(Integer, primary_key=True)
    timestamp = Column(DateTime, nullable=False)
    open = Column(Float)
    high = Column(Float)
    low = Column(Float)
    close = Column(Float)
    volume = Column(Float)

class SPYHourly(Base):
    __tablename__ = 'spy_hourly'
    __table_args__ = {'schema': 'index_alpha_vantage'}
    id = Column(Integer, primary_key=True)
    timestamp = Column(DateTime, nullable=False)
    open = Column(Float)
    high = Column(Float)
    low = Column(Float)
    close = Column(Float)
    volume = Column(Float)

# Daily Data Tables
class DIADaily(Base):
    __tablename__ = 'dia_daily'
    __table_args__ = {'schema': 'index_alpha_vantage'}
    id = Column(Integer, primary_key=True)
    date = Column(Date, nullable=False)
    open = Column(Float)
    high = Column(Float)
    low = Column(Float)
    close = Column(Float)
    volume = Column(Float)

class GOLDDaily(Base):
    __tablename__ = 'gold_daily'
    __table_args__ = {'schema': 'index_alpha_vantage'}
    id = Column(Integer, primary_key=True)
    date = Column(Date, nullable=False)
    open = Column(Float)
    high = Column(Float)
    low = Column(Float)
    close = Column(Float)
    volume = Column(Float)

class GLDDaily(Base):
    __tablename__ = 'gld_daily'
    __table_args__ = {'schema': 'index_alpha_vantage'}
    id = Column(Integer, primary_key=True)
    date = Column(Date, nullable=False)
    open = Column(Float)
    high = Column(Float)
    low = Column(Float)
    close = Column(Float)
    volume = Column(Float)

class SPYDaily(Base):
    __tablename__ = 'spy_daily'
    __table_args__ = {'schema': 'index_alpha_vantage'}
    id = Column(Integer, primary_key=True)
    date = Column(Date, nullable=False)
    open = Column(Float)
    high = Column(Float)
    low = Column(Float)
    close = Column(Float)
    volume = Column(Float)

DATABASE_URI = 'postgresql+psycopg2://nikhilrazab-sekh@localhost:5432/cryptovaultdb'
engine = create_engine(DATABASE_URI)
Session = sessionmaker(bind=engine)

if __name__ == "__main__":
    Base.metadata.create_all(engine)
    print("Index and Alpha Vantage tables have been created successfully.")
