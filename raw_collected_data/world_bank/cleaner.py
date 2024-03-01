import glob
import pandas as pd
import re

# Define the pattern to match all CSV files in the current directory
pattern = './*.csv'

# Use glob to find all csv files matching the pattern in the current directory
csv_files = glob.glob(pattern)

# Function to clean column names
def clean_column_name(column):
    # Replace '%' with 'prcnt'
    column = column.replace('%', 'prcnt')
    # Replace spaces with '_'
    column = column.replace(' ', '_')
    # Remove special characters except underscore
    column = re.sub(r'[^a-zA-Z0-9_\n\.]', '', column)
    # Convert to lowercase
    return column.lower()

# Loop through each found CSV file
for file_path in csv_files:
    # Read the CSV file
    df = pd.read_csv(file_path)
    # Convert and clean column names
    df.columns = [clean_column_name(c) for c in df.columns]
    # Overwrite the original file with updated column names
    df.to_csv(file_path, index=False)

print("All CSV headers have been cleaned, converted to lowercase, and files are overwritten.")
