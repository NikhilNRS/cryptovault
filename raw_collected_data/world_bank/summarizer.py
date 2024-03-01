import pandas as pd
import glob

# Output file
output_file = 'examples_with_types.txt'

# Find all CSV files in the current directory
csv_files = glob.glob('./*.csv')

with open(output_file, 'w') as f:
    for file_path in csv_files:
        # Extract the file name from the path
        file_name = file_path.split('/')[-1]
        
        # Read the CSV file
        df = pd.read_csv(file_path, nrows=1)  # Read only the first row to speed up dtype inference
        
        # Write the file name to the output file
        f.write(f"File: {file_name}\n")
        
        # Iterate over columns to get names and inferred types
        for column in df.columns:
            # Pandas dtype
            pandas_dtype = df[column].dtype
            
            # Attempt to map pandas dtype to PostgreSQL type
            # This mapping is basic and might need adjustments for specific cases
            if pandas_dtype == 'int64':
                postgres_type = 'BIGINT'
            elif pandas_dtype == 'float64':
                postgres_type = 'DOUBLE PRECISION'
            elif pandas_dtype == 'bool':
                postgres_type = 'BOOLEAN'
            elif pandas_dtype == 'datetime64[ns]':
                postgres_type = 'TIMESTAMP'
            else:
                postgres_type = 'TEXT'  # Default to TEXT for types like 'object' which can be strings or mixed types
            
            # Write column name and PostgreSQL type to the output file
            f.write(f"{column}: {postgres_type}\n")
        
        f.write("\n")

print(f"Data types summary written to {output_file}")
