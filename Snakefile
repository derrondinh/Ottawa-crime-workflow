rule get_data:
    output: "data/raw/Bike_Crime_Data.csv"
    script: "scripts/download_data.py"
rule clean_data:
    input: "data/raw/Bike_Crime_Data.csv"
    output: "data/clean/Bike_Crime_Cleaned.csv"  
    script: "scripts/clean_data.py"
rule transform_data:
    input: "data/clean/Bike_Crime_Cleaned.csv"
    output: "data/transformed/Bike_Crime_Transformed.csv"
    script: "scripts/transform_data.py"
rule analyze_data:
    input: "data/transformed/Bike_Crime_Transformed.csv"
    output: 
        "results/plots/bike_theft_by_neighbourhood.png",
        "results/reports/Bike_Crime_Report.txt"
    script: "scripts/analyze_data.py"