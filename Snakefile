rule get_data:
    output: "data/raw/Bike_Crime_Data.csv"
    script: "scripts/download_data.py"
rule clean_data:
    input: "data/raw/Bike_Crime_Data.csv"
    output: "data/clean/Bike_Crime_Cleaned.csv"  
    script: "scripts/clean_data.py"
    