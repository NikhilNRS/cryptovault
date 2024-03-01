import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import datetime
import logging
import sys
import os

# Append the parent directory to sys.path to access the 'db' package
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'db'))

# Import the table classes from the table creator script
from marketstack_table_creator import DJIA, Gold, SP500

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Database connection string
DATABASE_URI = 'postgresql+psycopg2://nikhilrazab-sekh@localhost:5432/cryptovaultdb'
engine = create_engine(DATABASE_URI)
Session = sessionmaker(bind=engine)

def load_data(csv_file, Model):
    """
    Load data from a CSV file into the specified model's table.
    """
    session = Session()
    try:
        # Read the CSV file
        df = pd.read_csv(csv_file)
        for _, row in df.iterrows():
            # Convert date from string to datetime object
            date_obj = datetime.strptime(row['date'], '%Y-%m-%d')
            record = Model(date=date_obj, closing_price=row['Closing Price'])
            session.add(record)
        session.commit()
        logging.info(f"Data loaded successfully from {csv_file} into {Model.__tablename__} table.")
    except Exception as e:
        session.rollback()
        logging.error(f"Error loading data from {csv_file}: {e}")
    finally:
        session.close()

if __name__ == "__main__":
    # Load data into the DJIA table
    load_data('/Users/nikhilrazab-sekh/Desktop/data_preparation/src/data_loading/../../raw_collected_data/marketstack/djia_data_daily.csv', DJIA)
    # Load data into the Gold table
    load_data('/Users/nikhilrazab-sekh/Desktop/data_preparation/src/data_loading/../../raw_collected_data/marketstack/gold_data_daily.csv', Gold)
    # Load data into the S&P 500 table
    load_data('/Users/nikhilrazab-sekh/Desktop/data_preparation/src/data_loading/../../raw_collected_data/marketstack/s&p_500_data_daily.csv', SP500)
