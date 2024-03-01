import sys
import os
import pandas as pd
from sqlalchemy import create_engine, exc
from sqlalchemy.orm import sessionmaker
from datetime import datetime
import logging

# Append the parent directory to sys.path to access the 'db' package
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'db'))

from sentiment_table_creator import FearAndGreedIndex, NewsBTC

# Logging configuration
logging.basicConfig(filename='load_cleaned_sentiment.log', level=logging.INFO,
                    format='%(asctime)s:%(levelname)s:%(message)s')

# Database credentials and connection
DATABASE_URI = 'postgresql+psycopg2://nikhilrazab-sekh@localhost:5432/cryptovaultdb'
engine = create_engine(DATABASE_URI)
Session = sessionmaker(bind=engine)
session = Session()

# Adjusted file paths according to your provided paths
fear_and_greed_index_filepath = os.path.join(os.path.dirname(__file__), '..', '..', 'raw_collected_data', 'sentiment', 'fear_and_greed_index.csv')
news_btc_filepath = os.path.join(os.path.dirname(__file__), '..', '..', 'raw_collected_data', 'sentiment', 'news_btc.csv')

def load_data():
    # Load and insert FearAndGreedIndex data
    try:
        fear_and_greed_index_data = pd.read_csv(fear_and_greed_index_filepath)
        for index, row in fear_and_greed_index_data.iterrows():
            entry = FearAndGreedIndex(
                timestamp=datetime.strptime(row['timestamp'], '%Y-%m-%d %H:%M:%S'),  # Adjust date format as necessary
                value=row['value'],
                classification=row['classification']
            )
            session.add(entry)
        session.commit()
        logging.info('Successfully loaded FearAndGreedIndex data.')
    except exc.SQLAlchemyError as e:
        session.rollback()
        logging.error(f'Error loading FearAndGreedIndex data: {e}')

    # Load and insert NewsBTC data
    try:
        news_btc_data = pd.read_csv(news_btc_filepath)
        for index, row in news_btc_data.iterrows():
            try:
                sentiment_score = float(row['sentiment_score'])  # Attempt to convert to float
            except ValueError:
                logging.error(f"Invalid sentiment_score '{row['sentiment_score']}' for title '{row['title']}' - skipping row")
                continue  # Skip this row and move to the next

            # If conversion is successful, proceed with creating the entry
            entry = NewsBTC(
                title=row['title'],
                url=row['url'],
                sentiment_score=sentiment_score,  # Use the converted float value
                sentiment_interpretation=row['sentiment_interpretation'],
                author=row['author'],
                timestamp=datetime.strptime(row['timestamp'], '%Y-%m-%d %H:%M:%S')
            )
            session.add(entry)

        session.commit()
        
        logging.info('Successfully loaded NewsBTC data.')
    except exc.SQLAlchemyError as e:
        session.rollback()
        logging.error(f'Error loading NewsBTC data: {e}')

if __name__ == "__main__":
    load_data()
