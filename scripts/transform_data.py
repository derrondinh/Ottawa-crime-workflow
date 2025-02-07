import pandas as pd

# file paths
input_file = "data/clean/Bike_Crime_Cleaned.csv"
output_file = "results/transformed_data.csv"

# Load the cleaned data
df = pd.read_csv(input_file)

# aggregate thefts by neighborhood
aggregated_by_neighbourhood = df.groupby("Neighbourhood").size().reset_index(name="Total_Thefts")

# save transformed data
aggregated_by_neighbourhood.to_csv(output_file, index=False)

print(f"Data transformation completed! Saved to {output_file}.")