import zipfile
import os
import pandas as pd
import re

# Function to extract load timestamp from zip file name using regular expressions
def extract_timestamp(zip_file_name):
    match = re.search(r'(\d{4})(\d{2})(\d{2})(\d{2})(\d{2})(\d{2})', zip_file_name)
    if match:
        timestamp = '-'.join(match.groups()[:3]) + ' ' + ':'.join(match.groups()[3:])
        return timestamp
    else:
        return None

# Function to add load timestamp column to DataFrame
def add_load_timestamp(df, timestamp):
    df['load_timestamp'] = timestamp
    return df

# Extract the zip file
zip_file_path = '/home/nineleaps/Desktop/pr/20240305124003123456_Extract 2.zip'
with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
    zip_ref.extractall('/home/nineleaps/Desktop/pr')

# Extract load timestamp
timestamp = extract_timestamp(zip_file_path)

# Read and process sample.csv
sample_csv_path = '/home/nineleaps/Desktop/pr/sample.csv'
sample_df = pd.read_csv(sample_csv_path)
sample_df = add_load_timestamp(sample_df, timestamp)

# Read and process sample2.csv
sample2_csv_path = '/home/nineleaps/Desktop/pr/sample2.csv'
sample2_df = pd.read_csv(sample2_csv_path)
sample2_df = add_load_timestamp(sample2_df, timestamp)

# Save the modified DataFrames back to CSV files
sample_df.to_csv(sample_csv_path, index=False)
sample2_df.to_csv(sample2_csv_path, index=False)

# Print the DataFrames
print("Sample DataFrame:")
print(sample_df)
print("\nSample2 DataFrame:")
print(sample2_df)
