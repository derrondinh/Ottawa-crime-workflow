rule get_data:
    output: "data/raw/Bike_Crime_Data.csv"
    script: "scripts/download_data.py"
rule clean_data:
    input:
        "data/raw/crime_data.csv"
    output:
        "data/cleaned/crime_data_cleaned.csv"
    shell:
        "python scripts/clean_data.py"