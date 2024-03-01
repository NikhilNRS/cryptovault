from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

class FearAndGreedIndex(Base):
    __tablename__ = 'fear_and_greed_index'
    __table_args__ = {'schema': 'sentiment'}
    timestamp = Column(DateTime, primary_key=True)
    value = Column(Integer)
    classification = Column(String)

class NewsBTC(Base):
    __tablename__ = 'news_btc'
    __table_args__ = {'schema': 'sentiment'}
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String)
    url = Column(String)
    sentiment_score = Column(Float)
    sentiment_interpretation = Column(String)
    author = Column(String)
    timestamp = Column(DateTime)

# Replace 'username', 'password', 'localhost', '5432', and 'cryptovaultdb' with your actual database credentials
DATABASE_URI = 'postgresql+psycopg2://nikhilrazab-sekh@localhost:5432/cryptovaultdb'
engine = create_engine(DATABASE_URI)

if __name__ == "__main__":
    Base.metadata.create_all(engine)
