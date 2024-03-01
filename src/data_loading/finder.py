import os

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
    
    # Base path from the script's location to the 'raw_collected_data'
    base_path = os.path.join(os.path.dirname(__file__), '..', '..', 'raw_collected_data')
    
    # Check each directory for the file
    for directory in directories:
        potential_path = os.path.join(base_path, directory, csv_file_name)
        if os.path.exists(potential_path):
            # File found, return the relative path
            return potential_path
    
    # File not found in the predefined directories, return a message or raise an error
    return f"File {csv_file_name} not found in known directories."

# Example usage
djia_data_daily = get_file_path('djia_data_daily.csv')
gold_data_daily = get_file_path('gold_data_daily.csv')
sp_500_data_daily = get_file_path('s&p_500_data_daily.csv')

print(djia_data_daily)
print(gold_data_daily)
print(sp_500_data_daily)
