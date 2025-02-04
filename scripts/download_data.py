import shutil
import os

# Define paths
source_file = "/Users/derron/Documents/GitHub/Ottawa-crime-workflow/Bike_Theft_Open_Data_3884822422354997826.csv" 
destination_folder = "data/raw"
destination_file = os.path.join(destination_folder, "Bike_Crime_Data.csv")

# Ensure the destination directory exists
os.makedirs(destination_folder, exist_ok=True)

# Copy the file
try:
    shutil.copy(source_file, destination_file)
    print(f"Dataset successfully copied to {destination_file}")
except FileNotFoundError:
    print(f"Error: {source_file} not found. Ensure the file is in the correct location.")
except Exception as e:
    print(f"An error occurred: {e}")