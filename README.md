# README for CryptoVaultDB Economic and Financial Data

Welcome to the CryptoVaultDB repository, authored by Nikhil Razab-Sekh. This repository offers a comprehensive suite of economic and financial data ready to be integrated into your projects. It's designed to facilitate the rapid setup of a robust database filled with relevant datasets for analysis, research, or application development in the fields of economics, finance, and cryptocurrency.

## Overview

CryptoVaultDB contains pre-structured tables across various schemas, tailored to different financial and economic indicators. These datasets range from consumer price indexes and GDP growth rates to cryptocurrency market data, providing a versatile resource for diverse analytical needs.

## Schemas and Tables

Our database is organized into multiple schemas, each focusing on different data sources and themes:

- **alpha_vantage**: Economic indicators such as CPI, GDP, unemployment rates, and more.
- **coinbase**: Cryptocurrency market data, including Bitcoin trading information.
- **index_alpha_vantage**: Market indices data for DIA, GLD, and SPY across daily and hourly intervals.
- **marketstack**: Data on major financial markets including DJIA, gold, and S&P 500.
- **sentiment**: Sentiment analysis data, including the Fear and Greed index and Bitcoin news sentiment.
- **world_bank**: A variety of cleaned and preprocessed economic indicators from the World Bank, focused on the USA and globally.

## Getting Started

To utilize CryptoVaultDB:

1. **Clone the Repository**: Clone this repository to your local machine.
2. **Unzip the Data**: Dataset files are provided in a compressed format. Unzip these files to access the SQL scripts and data dumps.
3. **Database Setup**: Use the provided SQL scripts to create the schemas and tables in your PostgreSQL instance. Ensure PostgreSQL is installed and configured properly.
4. **Import Data**: Import the data into the respective tables. Instructions for importing data are included.
5. **Explore and Analyze**: With the database set up, you're ready to explore the datasets and conduct your analysis.

## Prerequisites

- PostgreSQL (latest version recommended)
- Python (for SQLAlchemy usage)
- SQLAlchemy (for ORM-based database interactions, if needed)

## Contributions and Feedback

Contributions and feedback are welcome. If you have any suggestions for additional datasets, improvements, or issues, please open an issue or submit a pull request.

## Author

Nikhil Razab-Sekh

---

Enjoy exploring and analyzing the vast amount of economic and financial data provided in CryptoVaultDB. Happy data diving!
