import pandas as pd
import matplotlib.pyplot as plt
import os

# File paths
input_file = "data/transformed/Bike_Crime_Transformed.csv"
output_plot = "results/plots/bike_theft_by_neighbourhood.png"
report_file = "results/reports/Bike_Crime_Report.txt"

# Load transformed data
df = pd.read_csv(input_file).sort_values("Total_Thefts", ascending=False)

# Get overall stats
total_neighbourhoods = df["Neighbourhood"].nunique()
total_thefts = df["Total_Thefts"].sum()
most_affected = df.iloc[0]  # Neighborhood with the highest theft count
least_affected = df.iloc[min(19, len(df) - 1)]  # Neighborhood with the lowest count in top 20

# Select top 20 neighborhoods
df_top = df.head(20).copy()

# Select bottom 10 neighborhoods
df_least = df.tail(10).copy()

# Shorten long neighborhood names for better visualization
df_top["Neighbourhood"] = df_top["Neighbourhood"].apply(lambda x: ' '.join(x.split()[:3]))  # Keep first 3 words

# Create and save bar plot
plt.figure(figsize=(15, 8))  # Increased size for better spacing
plt.bar(df_top["Neighbourhood"], df_top["Total_Thefts"], color="steelblue")

# Improve text formatting
plt.xticks(rotation=30, ha="right", fontsize=11)  # More readable rotation
plt.xlabel("Neighbourhood", fontsize=12, labelpad=10)
plt.ylabel("Total Bike Thefts", fontsize=12, labelpad=10)
plt.title("Top 20 Neighbourhoods for Bike Thefts", fontsize=14, pad=15)

# Adjust margins and spacing
plt.subplots_adjust(bottom=0.35)  # More space for labels
plt.savefig(output_plot, dpi=300, bbox_inches="tight")  # Ensure full image is saved
plt.close()

# Generate report content
report_content = f"""
Bike Theft Analysis Report
==========================================
Summary:
- Total neighborhoods analyzed: {total_neighbourhoods}
- Total reported bike thefts: {total_thefts}
- Most affected neighborhood: {most_affected['Neighbourhood']} ({most_affected['Total_Thefts']} thefts)
- Least affected neighborhood: {least_affected['Neighbourhood']} ({least_affected['Total_Thefts']} thefts)

Top 10 Most Affected Neighborhoods:
{df_top.head(10).to_string(index=False)}

Top 10 Least Affected Neighborhoods:
{df_least.to_string(index=False)}

Key Observations:
- Thefts are highly concentrated in certain neighborhoods.
- Some neighborhoods experience significantly lower bike theft incidents.
- Further analysis could include trends over time or seasonal variations.
"""

# Save summary report
with open(report_file, "w") as f:
    f.write(report_content)

print(f"Analysis complete! Saved to:\n- {output_plot}\n- {report_file}")