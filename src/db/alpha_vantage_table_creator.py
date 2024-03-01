from sqlalchemy import create_engine, Column, Float, DateTime, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Define the base class for all table models
Base = declarative_base()

# Define table classes for each dataset
class CPIMonthly(Base):
    __tablename__ = 'cpi_monthly'
    id = Column(Integer, primary_key=True)
    timestamp = Column(DateTime, unique=True, nullable=False)
    value = Column(Float, nullable=False)

class CPISemiannual(Base):
    __tablename__ = 'cpi_semiannual'
    id = Column(Integer, primary_key=True)
    timestamp = Column(DateTime, unique=True, nullable=False)
    value = Column(Float, nullable=False)

# Repeat for each dataset
class DurablesMonthly(Base):
    __tablename__ = 'durables_monthly'
    id = Column(Integer, primary_key=True)
    timestamp = Column(DateTime, unique=True, nullable=False)
    value = Column(Float, nullable=False)

class FederalFundsRateDaily(Base):
    __tablename__ = 'federal_funds_rate_daily'
    id = Column(Integer, primary_key=True)
    timestamp = Column(DateTime, unique=True, nullable=False)
    value = Column(Float, nullable=False)

class FederalFundsRateMonthly(Base):
    __tablename__ = 'federal_funds_rate_monthly'
    id = Column(Integer, primary_key=True)
    timestamp = Column(DateTime, unique=True, nullable=False)
    value = Column(Float, nullable=False)

class FederalFundsRateWeekly(Base):
    __tablename__ = 'federal_funds_rate_weekly'
    id = Column(Integer, primary_key=True)
    timestamp = Column(DateTime, unique=True, nullable=False)
    value = Column(Float, nullable=False)

class InflationAnnual(Base):
    __tablename__ = 'inflation_annual'
    id = Column(Integer, primary_key=True)
    timestamp = Column(DateTime, unique=True, nullable=False)
    value = Column(Float, nullable=False)

class NonfarmPayrollMonthly(Base):
    __tablename__ = 'nonfarm_payroll_monthly'
    id = Column(Integer, primary_key=True)
    timestamp = Column(DateTime, unique=True, nullable=False)
    value = Column(Float, nullable=False)

class RealGDPAnnual(Base):
    __tablename__ = 'real_gdp_annual'
    id = Column(Integer, primary_key=True)
    timestamp = Column(DateTime, unique=True, nullable=False)
    value = Column(Float, nullable=False)

class RealGDPPerCapitaQuarterly(Base):
    __tablename__ = 'real_gdp_per_capita_quarterly'
    id = Column(Integer, primary_key=True)
    timestamp = Column(DateTime, unique=True, nullable=False)
    value = Column(Float, nullable=False)

class RealGDPQuarterly(Base):
    __tablename__ = 'real_gdp_quarterly'
    id = Column(Integer, primary_key=True)
    timestamp = Column(DateTime, unique=True, nullable=False)
    value = Column(Float, nullable=False)

class RetailSalesMonthly(Base):
    __tablename__ = 'retail_sales_monthly'
    id = Column(Integer, primary_key=True)
    timestamp = Column(DateTime, unique=True, nullable=False)
    value = Column(Float, nullable=False)

class TreasuryYieldDaily(Base):
    __tablename__ = 'treasury_yield_daily'
    id = Column(Integer, primary_key=True)
    timestamp = Column(DateTime, unique=True, nullable=False)
    value = Column(Float, nullable=False)

class TreasuryYieldMonthly(Base):
    __tablename__ = 'treasury_yield_monthly'
    id = Column(Integer, primary_key=True)
    timestamp = Column(DateTime, unique=True, nullable=False)
    value = Column(Float, nullable=False)

class TreasuryYieldWeekly(Base):
    __tablename__ = 'treasury_yield_weekly'
    id = Column(Integer, primary_key=True)
    timestamp = Column(DateTime, unique=True, nullable=False)
    value = Column(Float, nullable=False)

class UnemploymentMonthly(Base):
    __tablename__ = 'unemployment_monthly'
    id = Column(Integer, primary_key=True)
    timestamp = Column(DateTime, unique=True, nullable=False)
    value = Column(Float, nullable=False)

# Database connection string
DATABASE_URI = 'postgresql+psycopg2://nikhilrazab-sekh@localhost:5432/cryptovaultdb'

# Create engine and bind the session
engine = create_engine(DATABASE_URI)
Session = sessionmaker(bind=engine)

# Create all tables in the database
Base.metadata.create_all(engine)

if __name__ == "__main__":
    print("Economic data tables have been created successfully.")
