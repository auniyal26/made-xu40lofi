import os
import pandas as pd
import kaggle
import re
import shutil

# Define Kaggle datasets to download
datasets = [
    {"owner": "sarfarazsheikh", "dataset": "temperature-change-in-indian-states-19022020"},
    {"owner": "aditya2803", "dataset": "india-floods-inventory"},
    {"owner": "ramjasmaurya", "dataset": "exports-and-imports-of-india19972022"}
]

# Define data directory
data_dir = 'data'

# Clear data directory if it exists
if os.path.exists(data_dir):
    shutil.rmtree(data_dir)

# Create data directory
os.makedirs(data_dir)

# Function to clean file names
def clean_file_name(file_name):
    file_name = re.sub(r'[^\w\s-]', '', file_name)  # Remove special characters
    file_name = re.sub(r'\s+', '_', file_name)  # Replace spaces with underscores
    return file_name

# Download datasets from Kaggle
for dataset in datasets:
    print(f"Downloading dataset: {dataset['owner']}/{dataset['dataset']}")
    kaggle.api.dataset_download_files(f"{dataset['owner']}/{dataset['dataset']}", path=data_dir, unzip=True)

# Rename files to remove double extensions
for file in os.listdir(data_dir):
    if file.endswith('.csv.csv'):
        os.rename(os.path.join(data_dir, file), os.path.join(data_dir, file.replace('.csv.csv', '.csv')))

# Clean and save each dataset as CSV
for file in os.listdir(data_dir):
    if file.endswith('.csv'):
        print(f"Processing file: {file}")  # Debug statement
        try:
            df = pd.read_csv(os.path.join(data_dir, file), encoding='utf-8')
            print(f"Read {file} with utf-8 encoding")  # Debug statement
        except UnicodeDecodeError:
            df = pd.read_csv(os.path.join(data_dir, file), encoding='ISO-8859-1')
            print(f"Read {file} with ISO-8859-1 encoding")  # Debug statement

        # Perform data cleaning based on file
        if 'mean_temperature_data' in file.lower():
            # Filter rows for 12 months of the year
            df = df[df['Period'].isin(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])]
            # Drop incomplete rows
            df.dropna(inplace=True)
        elif 'india_floods_inventory' in file.lower():
            # Drop rows without latitude and longitude values
            df = df.dropna(subset=['Latitude', 'Longitude'])
            # Rename column "Event Souce ID" to "Event Source ID"
            df = df.rename(columns={"Event Souce ID": "Event Source ID"})
            # Remove UEI column if exists
            if 'UEI' in df.columns:
                df = df.drop(columns=['UEI'])
        elif 'exports_and_imports' in file.lower():
            # Drop incomplete rows
            df.dropna(inplace=True)

        # Save cleaned dataset as CSV, replacing the original file
        cleaned_csv_path = os.path.join(data_dir, file)
        df.to_csv(cleaned_csv_path, index=False)
        print(f"Cleaned data saved as CSV: {cleaned_csv_path}")

# Rename cleaned files as specified
rename_mapping = {
    'mean_temperature_data': 'INDTemperature.csv',
    'india_floods_inventory': 'INDFloods.csv',
    'exports_and_imports': 'INDImportExport.csv'
}

for file in os.listdir(data_dir):
    for key, new_name in rename_mapping.items():
        if key in file.lower().replace(' ', '_'):
            old_path = os.path.join(data_dir, file)
            new_path = os.path.join(data_dir, new_name)
            os.rename(old_path, new_path)
            print(f"Renamed {file} to {new_name}")
            break

# Verify the renamed file exists before proceeding
ind_import_export_path = os.path.join(data_dir, 'INDImportExport.csv')

if os.path.exists(ind_import_export_path):
    # Load the CSV file
    df = pd.read_csv(ind_import_export_path, encoding='utf-8')
    print("Loaded INDImportExport.csv for replacement.")

    # Replace "till now" with "2023" in the entire DataFrame
    df = df.apply(lambda x: x.replace('till now', '2023') if isinstance(x, str) else x)

    # Save the modified DataFrame back to CSV
    df.to_csv(ind_import_export_path, index=False, encoding='utf-8')
    print("Replacement of 'till now' with '2023' in INDImportExport.csv completed.")
else:
    print("File INDImportExport.csv does not exist.")
