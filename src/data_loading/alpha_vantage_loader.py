import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import datetime
import logging
import sys
import os

# Append the parent directory to sys.path to access the 'db' package
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'db'))

# Import table classes
from alpha_vantage_table_creator import (CPIMonthly, CPISemiannual, DurablesMonthly, 
                                         FederalFundsRateDaily, FederalFundsRateMonthly, 
                                         FederalFundsRateWeekly, InflationAnnual, NonfarmPayrollMonthly, 
                                         RealGDPAnnual, RealGDPPerCapitaQuarterly, RealGDPQuarterly, 
                                         RetailSalesMonthly, TreasuryYieldDaily, TreasuryYieldMonthly, 
                                         TreasuryYieldWeekly, UnemploymentMonthly)

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Database connection string
DATABASE_URI = 'postgresql+psycopg2://nikhilrazab-sekh@localhost:5432/cryptovaultdb'
engine = create_engine(DATABASE_URI)
Session = sessionmaker(bind=engine)

# Function to get the file path based on the CSV file name
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
    
    # Assuming the script is run from a specific location, adjust accordingly
    base_path = os.path.join(os.path.dirname(__file__), '..', '..', 'raw_collected_data')
    
    for directory in directories:
        potential_path = os.path.join(base_path, directory, csv_file_name)
        if os.path.exists(potential_path):
            return potential_path
    
    return f"File {csv_file_name} not found in known directories."

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Database connection string
DATABASE_URI = 'postgresql+psycopg2://nikhilrazab-sekh@localhost:5432/cryptovaultdb'
engine = create_engine(DATABASE_URI)
Session = sessionmaker(bind=engine)

def load_data(Model):
    """
    Load data from a CSV file into the specified model's table based on the model's __tablename__.
    """
    session = Session()
    csv_file_name = f"{Model.__tablename__}.csv"
    csv_file_path = get_file_path(csv_file_name)
    
    if "not found" in csv_file_path:
        logging.error(csv_file_path)
        return

    try:
        df = pd.read_csv(csv_file_path, parse_dates=['timestamp'])
        for index, row in df.iterrows():
            record = Model(timestamp=row['timestamp'], value=row['value'])
            session.add(record)
        session.commit()
        logging.info(f"Data loaded successfully from {csv_file_path} into {Model.__tablename__} table.")
    except Exception as e:
        session.rollback()
        logging.error(f"Error loading data from {csv_file_path}: {e}")
    finally:
        session.close()

if __name__ == "__main__":
    # Iterate over each model to load data
    models = [CPIMonthly, CPISemiannual, DurablesMonthly, 
                FederalFundsRateDaily, FederalFundsRateMonthly, 
                FederalFundsRateWeekly, InflationAnnual, NonfarmPayrollMonthly, 
                RealGDPAnnual, RealGDPPerCapitaQuarterly, RealGDPQuarterly, 
                RetailSalesMonthly, TreasuryYieldDaily, TreasuryYieldMonthly, 
                TreasuryYieldWeekly, UnemploymentMonthly]
    
    for model in models:
        load_data(model)