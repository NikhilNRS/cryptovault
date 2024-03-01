import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import logging
import os
import sys

# Append the parent directory to sys.path to access the 'db' package
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'db'))

# Import table classes from your table creator script
from index_alpha_vantage_table_creator import (DIAHourly, DIADaily, GOLDHourly, GOLDDaily,
                                                GLDHourly, GLDDaily, SPYHourly, SPYDaily)

# Function to dynamically find file paths
def get_file_path(csv_file_name):
    directories = ['alpha_vantage', 'coinbase', 'index_alpha_vantage', 'marketstack', 'sentiment', 'world_bank']
    base_path = os.path.join(os.path.dirname(__file__), '..', '..', 'raw_collected_data')
    for directory in directories:
        potential_path = os.path.join(base_path, directory, csv_file_name)
        if os.path.exists(potential_path):
            return potential_path
    return None

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
DATABASE_URI = 'postgresql+psycopg2://nikhilrazab-sekh@localhost:5432/cryptovaultdb'
engine = create_engine(DATABASE_URI)
Session = sessionmaker(bind=engine)

def load_data(Model, csv_file_name):
    session = Session()
    csv_file_path = get_file_path(csv_file_name)
    if not csv_file_path:
        logging.error(f"File {csv_file_name} not found.")
        return

    try:
        df = pd.read_csv(csv_file_path)
        for index, row in df.iterrows():
            record = Model(**row.to_dict())
            session.add(record)
        session.commit()
        logging.info(f"Data loaded successfully from {csv_file_path} into {Model.__tablename__} table.")
    except Exception as e:
        session.rollback()
        logging.error(f"Error loading data from {csv_file_path}: {e}")
    finally:
        session.close()

if __name__ == "__main__":
    # Load data for each dataset
    datasets = [
        (DIAHourly, 'DIA_hourly_data_2013_to_2023.csv'),
        (DIADaily, 'DIA_daily_data.csv'),
        (GOLDHourly, 'GOLD_hourly_data_2013_to_2023.csv'),
        (GOLDDaily, 'GOLD_daily_data.csv'),
        (GLDHourly, 'GLD_hourly_data_2013_to_2023.csv'),
        (GLDDaily, 'GLD_daily_data.csv'),
        (SPYHourly, 'SPY_hourly_data_2013_to_2023.csv'),
        (SPYDaily, 'SPY_daily_data.csv')
    ]

    for model, file_name in datasets:
        load_data(model, file_name)
