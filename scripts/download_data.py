import shutil
import os

import shutil

# input and output file paths
input_file = "Bike_Theft_Open_Data_3884822422354997826.csv"
output_file = "data/raw/Bike_Crime_Data.csv"

# Copy the file
shutil.copy(input_file, output_file)
print(f"Copied to {output_file}")