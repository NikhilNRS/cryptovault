from sqlalchemy import create_engine, Column, Float, Integer, String, BigInteger, Text, Numeric, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class InflationRatesUSACleaned(Base):
    __tablename__ = 'inflation_rates_usa_cleaned'
    __table_args__ = {'schema': 'world_bank'}
    id = Column(Integer, primary_key=True)
    indicator_id = Column(Text)
    indicator_value = Column(Text)
    country_id = Column(Text)
    country_value = Column(Text)
    countryiso3code = Column(Text)
    timestamp = Column(DateTime)
    value = Column(Numeric)
    unit = Column(Numeric)
    obs_status = Column(Numeric)
    decimal = Column(BigInteger)

class TradeBalanceUSACleaned(Base):
    __tablename__ = 'trade_balance_usa_cleaned'
    __table_args__ = {'schema': 'world_bank'}
    id = Column(Integer, primary_key=True)
    timestamp = Column(DateTime)
    value = Column(BigInteger)
    indicator_value = Column(Text)
    country_value = Column(Text)

class WorldBankEconomicIndicatorsNL(Base):
    __tablename__ = 'world_bank_economic_indicators_nl'
    __table_args__ = {'schema': 'world_bank'}
    id = Column(Integer, primary_key=True)
    timestamp = Column(DateTime)
    gdp_growth_rate = Column(Numeric)
    inflation_rate = Column(Numeric)
    unemployment_rate = Column(Numeric)
    trade_balance = Column(Numeric)
    foreign_direct_investment = Column(Numeric)
    internet_penetration = Column(Numeric)

class TariffsUSACleaned(Base):
    __tablename__ = 'tariffs_usa_cleaned'
    __table_args__ = {'schema': 'world_bank'}
    id = Column(Integer, primary_key=True)
    timestamp = Column(DateTime)
    countryiso3code = Column(Text)
    value = Column(Numeric)
    unit = Column(Numeric)
    obs_status = Column(Numeric)
    decimal = Column(BigInteger)
    indicator_value = Column(Text)
    country_value = Column(Text)

class CentralBankPolicyRatesUSACleaned(Base):
    __tablename__ = 'central_bank_policy_rates_usa_cleaned'
    __table_args__ = {'schema': 'world_bank'}
    id = Column(Integer, primary_key=True)
    timestamp = Column(DateTime)
    central_bank_policy_rate_prcnt = Column(Numeric)  # Updated attribute name

class InternetPenetrationUSACleaned(Base):
    __tablename__ = 'internet_penetration_usa_cleaned'
    __table_args__ = {'schema': 'world_bank'}
    id = Column(Integer, primary_key=True)
    timestamp = Column(DateTime)
    individuals_using_the_internet_prcnt_of_population = Column(Numeric)  # Updated

class UnemploymentRatesUSACleaned(Base):
    __tablename__ = 'unemployment_rates_usa_cleaned'
    __table_args__ = {'schema': 'world_bank'}
    id = Column(Integer, primary_key=True)
    timestamp = Column(DateTime)
    value = Column(Numeric)

class RemittancesUSACleaned(Base):
    __tablename__ = 'remittances_usa_cleaned'
    __table_args__ = {'schema': 'world_bank'}
    id = Column(Integer, primary_key=True)
    indicator = Column(Text)
    country = Column(Text)
    timestamp = Column(DateTime)
    personal_remittances_received_prcnt_of_gdp = Column(Numeric)  # Updated

class GDPGrowthRatesUSACleaned(Base):
    __tablename__ = 'gdp_growth_rates_usa_cleaned'
    __table_args__ = {'schema': 'world_bank'}
    id = Column(Integer, primary_key=True)
    timestamp = Column(DateTime)
    gdp_growth_annual_prcnt = Column(Numeric)  # Updated

# Stock Market Indices USA Cleaned
class StockMarketIndicesUSACleaned(Base):
    __tablename__ = 'stock_market_indices_usa_cleaned'
    __table_args__ = {'schema': 'world_bank'}
    id = Column(Integer, primary_key=True)
    timestamp = Column(DateTime)
    countryiso3code = Column(Text)
    value = Column(Numeric)
    unit = Column(Numeric)
    obs_status = Column(Numeric)
    decimal = Column(BigInteger)
    indicator_value = Column(Text)
    country_value = Column(Text)

# Mobile Cellular Subscriptions USA Cleaned
class MobileCellularSubscriptionsUSACleaned(Base):
    __tablename__ = 'mobile_cellular_subscriptions_usa_cleaned'
    __table_args__ = {'schema': 'world_bank'}
    id = Column(Integer, primary_key=True)
    indicator = Column(Text)
    country = Column(Text)
    timestamp = Column(DateTime)
    mobile_cellular_subscriptions_per_100_people = Column(Numeric)

# Total Public Debt GDP USA Cleaned
class TotalPublicDebtGDPUSACleaned(Base):
    __tablename__ = 'total_public_debt_gdp_usa_cleaned'
    __table_args__ = {'schema': 'world_bank'}
    id = Column(Integer, primary_key=True)
    timestamp = Column(DateTime)
    countryiso3code = Column(Text)
    value = Column(Numeric)
    unit = Column(Numeric)
    obs_status = Column(Numeric)
    decimal = Column(BigInteger)
    indicator_value = Column(Text)
    country_value = Column(Text)

# Trade in Services USA Cleaned
class TradeInServicesUSACleaned(Base):
    __tablename__ = 'trade_in_services_usa_cleaned'
    __table_args__ = {'schema': 'world_bank'}
    id = Column(Integer, primary_key=True)
    timestamp = Column(DateTime)
    value = Column(Numeric)
    indicator_value = Column(Text)
    country_value = Column(Text)

# World Bank Economic Indicators USA Preprocessed
class WorldBankEconomicIndicatorsUSAPreprocessed(Base):
    __tablename__ = 'world_bank_economic_indicators_usa_preprocessed'
    __table_args__ = {'schema': 'world_bank'}
    id = Column(Integer, primary_key=True)
    timestamp = Column(DateTime)
    value = Column(Numeric)

# Domestic Credit Private Sector USA Cleaned
class DomesticCreditPrivateSectorUSACleaned(Base):
    __tablename__ = 'domestic_credit_private_sector_usa_cleaned'
    __table_args__ = {'schema': 'world_bank'}
    id = Column(Integer, primary_key=True)
    timestamp = Column(DateTime)
    domestic_credit_to_private_sector_prcnt_of_gdp = Column(Numeric)

# Foreign Direct Investment USA Cleaned
class ForeignDirectInvestmentUSACleaned(Base):
    __tablename__ = 'foreign_direct_investment_usa_cleaned'
    __table_args__ = {'schema': 'world_bank'}
    id = Column(Integer, primary_key=True)
    indicator = Column(Text)
    country = Column(Text)
    countryiso3code = Column(Text)
    timestamp = Column(DateTime)
    fdi_net_inflows_bop_current_usd = Column(BigInteger)

DATABASE_URI = 'postgresql+psycopg2://nikhilrazab-sekh@localhost:5432/cryptovaultdb'
engine = create_engine(DATABASE_URI)
Session = sessionmaker(bind=engine)

if __name__ == "__main__":
    Base.metadata.create_all(engine)
    print("Database tables based on provided CSV files have been created successfully.")
