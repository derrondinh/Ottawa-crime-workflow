import pandas as pd

# file paths
input_file = "data/clean/Bike_Crime_Cleaned.csv"
output_file = "data/transformed/Bike_Crime_Transformed.csv"

# Load the cleaned data
df = pd.read_csv(input_file)

# Ensure column names are correct
if "Neighbourhood" not in df.columns:
    raise ValueError("Column 'Neighbourhood' not found in dataset.")

# Aggregate thefts by neighborhood
aggregated_by_neighborhood = df.groupby("Neighbourhood").size().reset_index(name="Total_Thefts")

# Save transformed data
aggregated_by_neighborhood.to_csv(output_file, index=False)

print(f"Data transformation completed! Saved to {output_file}.")