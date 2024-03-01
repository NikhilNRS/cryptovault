import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import datetime
import logging
import sys
import os


# Append the parent directory to sys.path to access the 'db' package
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'db'))


# Assuming the table classes are defined in 'coinbase_table_creator.py'
from coinbase_table_creator import BTCData6Hrs, BTCData15Daily, BTCData15Hourly

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
DATABASE_URI = 'postgresql+psycopg2://nikhilrazab-sekh@localhost:5432/cryptovaultdb'
engine = create_engine(DATABASE_URI)
Session = sessionmaker(bind=engine)

def get_file_path(csv_file_name):
    # Define the directories for a basic search
    directories = [
        'alpha_vantage',
        'coinbase',
        'index_alpha_vantage',
        'marketstack',
        'sentiment',
        'world_bank'
    ]
    
    # Base path from the script's location to the 'raw_collected_data'
    base_path = os.path.join(os.path.dirname(__file__), '..', '..', 'raw_collected_data')
    
    # Check each directory for the file
    for directory in directories:
        potential_path = os.path.join(base_path, directory, csv_file_name)
        if os.path.exists(potential_path):
            # File found, return the relative path
            return potential_path
    
    # File not found in the predefined directories, return a message or raise an error
    return f"File {csv_file_name} not found in known directories."

def load_data(Model):
    session = Session()
    csv_file_name = f"{Model.__tablename__}.csv"
    csv_file_path = get_file_path(csv_file_name)
    
    if "not found" in csv_file_path:
        logging.error(csv_file_path)
        return

    try:
        df = pd.read_csv(csv_file_path, parse_dates=['timestamp'])
        for index, row in df.iterrows():
            record = Model(timestamp=row['timestamp'], low=row['low'], high=row['high'], 
                           open=row['open'], close=row['close'], volume=row['volume'],
                           sma_30=row.get('SMA_30', None), rsi=row.get('RSI', None), 
                           macd=row.get('MACD', None))
            session.add(record)
        session.commit()
        logging.info(f"Data loaded successfully from {csv_file_path} into {Model.__tablename__} table.")
    except Exception as e:
        session.rollback()
        logging.error(f"Error loading data from {csv_file_path}: {e}")
    finally:
        session.close()

if __name__ == "__main__":
    models = [BTCData6Hrs, BTCData15Daily, BTCData15Hourly]
    for model in models:
        load_data(model)
