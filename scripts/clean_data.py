import pandas as pd

# Input and output file paths
input_file = "data/raw/Bike_Crime_Data.csv"
output_file = "data/clean/Bike_Crime_Data_Cleaned.csv"

try:
    # Load dataset
    df = pd.read_csv(input_file)

    # Drop rows where ID or Occurred Date is missing
    df.dropna(subset=["ID", "Occurred Date"], inplace=True)

    # Drop duplicate rows
    df.drop_duplicates(inplace=True)

    # Convert Occurred Date column to datetime format
    df["Occurred Date"] = pd.to_datetime(df["Occurred Date"], errors="coerce")

    # Save cleaned data
    df.to_csv(output_file, index=False)
    print(f"Cleaned data saved to {output_file}")

except FileNotFoundError:
    print(f"Error: {input_file} not found. Ensure the file is in the correct location.")
except Exception as e:
    print(f"An error occurred: {e}")