import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import logging
import os
import sys


# Append the parent directory to sys.path to access the 'db' package
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'db'))


from world_bank_table_creator import *  # Import your SQLAlchemy models here


# Assuming finder.py is in the same directory and contains get_file_path function
from finder import get_file_path

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
DATABASE_URI = 'postgresql+psycopg2://nikhilrazab-sekh@localhost:5432/cryptovaultdb'
engine = create_engine(DATABASE_URI)
Session = sessionmaker(bind=engine)

def load_data(model, csv_file_name):
    session = Session()
    csv_file_path = get_file_path(csv_file_name)
    if csv_file_path is None:
        logging.error(f"{csv_file_name} not found.")
        return

    try:
        df = pd.read_csv(csv_file_path)
        # Convert column names to lowercase to match the model attributes
        df.columns = [c.lower() for c in df.columns]
        records = df.to_dict(orient='records')

        for record in records:
            obj = model(**record)
            session.add(obj)
        session.commit()
        logging.info(f"Data loaded successfully from {csv_file_path} into {model.__tablename__}.")
    except Exception as e:
        session.rollback()
        logging.error(f"Failed to load data from {csv_file_path}: {e}")
    finally:
        session.close()

if __name__ == "__main__":
    Base.metadata.create_all(engine)
    datasets = [
        (InflationRatesUSACleaned, 'inflation_rates_usa_cleaned.csv'),
        (TradeBalanceUSACleaned, 'trade_balance_usa_cleaned.csv'),
        (WorldBankEconomicIndicatorsNL, 'world_bank_economic_indicators_nl.csv'),
        (TariffsUSACleaned, 'tariffs_usa_cleaned.csv'),
        (CentralBankPolicyRatesUSACleaned, 'central_bank_policy_rates_usa_cleaned.csv'),
        (InternetPenetrationUSACleaned, 'internet_penetration_usa_cleaned.csv'),
        (UnemploymentRatesUSACleaned, 'unemployment_rates_usa_cleaned.csv'),
        (RemittancesUSACleaned, 'remittances_usa_cleaned.csv'),
        (GDPGrowthRatesUSACleaned, 'gdp_growth_rates_usa_cleaned.csv'),
        (StockMarketIndicesUSACleaned, 'stock_market_indices_usa_cleaned.csv'),
        (MobileCellularSubscriptionsUSACleaned, 'mobile_cellular_subscriptions_usa_cleaned.csv'),
        (TotalPublicDebtGDPUSACleaned, 'total_public_debt_gdp_usa_cleaned.csv'),
        (TradeInServicesUSACleaned, 'trade_in_services_usa_cleaned.csv'),
        (WorldBankEconomicIndicatorsUSAPreprocessed, 'world_bank_economic_indicators_usa_preprocessed.csv'),
        (DomesticCreditPrivateSectorUSACleaned, 'domestic_credit_private_sector_usa_cleaned.csv'),
        (ForeignDirectInvestmentUSACleaned, 'foreign_direct_investment_usa_cleaned.csv')
    ]

    for model, csv_file_name in datasets:
        load_data(model, csv_file_name)

    print("Data loading process completed successfully.")
