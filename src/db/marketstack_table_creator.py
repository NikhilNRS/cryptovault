from sqlalchemy import create_engine, Column, Float, Integer, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Define the base class for all table models
Base = declarative_base()

# Define the DJIA table
class DJIA(Base):
    __tablename__ = 'djia'
    id = Column(Integer, primary_key=True)
    date = Column(Date, unique=True, nullable=False)
    closing_price = Column(Float, nullable=False)

# Define the Gold table
class Gold(Base):
    __tablename__ = 'gold'
    id = Column(Integer, primary_key=True)
    date = Column(Date, unique=True, nullable=False)
    closing_price = Column(Float, nullable=False)

# Define the S&P 500 table
class SP500(Base):
    __tablename__ = 'sp500'
    id = Column(Integer, primary_key=True)
    date = Column(Date, unique=True, nullable=False)
    closing_price = Column(Float, nullable=False)

# Database connection string
DATABASE_URI = 'postgresql+psycopg2://nikhilrazab-sekh@localhost:5432/cryptovaultdb'

# Create engine and bind the session
engine = create_engine(DATABASE_URI)
Session = sessionmaker(bind=engine)

# Create all tables in the database
Base.metadata.create_all(engine)

if __name__ == "__main__":
    print("Tables for DJIA, Gold, and S&P 500 have been created successfully.")
