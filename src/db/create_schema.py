from sqlalchemy import create_engine, text

# Database connection details
DATABASE_URI = 'postgresql+psycopg2://nikhilrazab-sekh@localhost:5432/cryptovaultdb'

# List of schemas to be created
schemas = [
    'alpha_vantage',
    'coinbase',
    'index_alpha_vantage',
    'marketstack',
    'sentiment',
    'world_bank'
]

def create_schemas(engine, schema_names):
    with engine.connect() as connection:
        for schema in schema_names:
            # Adjusted to use the text() construct for raw SQL execution
            create_schema_sql = text(f'CREATE SCHEMA IF NOT EXISTS "{schema}";')
            connection.execute(create_schema_sql)
            print(f'Schema "{schema}" created successfully.')

if __name__ == "__main__":
    engine = create_engine(DATABASE_URI)
    create_schemas(engine, schemas)
