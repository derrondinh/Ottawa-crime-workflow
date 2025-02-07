import pandas as pd

# File paths
input_file = "data/raw/Bike_Crime_Data.csv"
output_file = "data/clean/Bike_Crime_Cleaned.csv"

# Load dataset
df = pd.read_csv(input_file)

# Drop missing values in essential columns
df.dropna(subset=["ID", "Occurred Date"], inplace=True)

# Remove duplicates
df.drop_duplicates(inplace=True)

# Convert date columns to datetime
df["Occurred Date"] = pd.to_datetime(df["Occurred Date"], errors="coerce")
df["Reported Date"] = pd.to_datetime(df["Reported Date"], errors="coerce")

# Convert time columns to integers
df["Occurred Hour"] = pd.to_numeric(df["Occurred Hour"], errors="coerce").fillna(0).astype(int)
df["Reported Hour"] = pd.to_numeric(df["Reported Hour"], errors="coerce").fillna(0).astype(int)

# Round coordinates
df[["x", "y"]] = df[["x", "y"]].apply(pd.to_numeric, errors="coerce").round(6)

# Save cleaned data
df.to_csv(output_file, index=False)

print(f"Cleaned data saved to {output_file}")