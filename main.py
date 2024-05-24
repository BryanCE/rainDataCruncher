import json
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose
import re
import matplotlib.pyplot as plt

filename = 'rainfall_2022.json'
year = int(re.search(r'\d{4}', filename).group())


# Load JSON data
with open(filename, 'r') as f:
    rain_data = json.load(f)

# Flatten the JSON structure
flat_data = []
for entry in rain_data:
    grid_id = entry["Grid_ID"]
    for month_data in entry["Month_Data"]:
        flat_data.append({
            "Grid_ID": grid_id,
            "Month": month_data["Month"],
            "Total_Rainfall_mm": month_data["Total_Rainfall_mm"]
        })

# Create DataFrame
df = pd.DataFrame(flat_data)

# Perform analysis
# Summary statistics
summary_stats = df.describe()

# Monthly average rainfall
monthly_avg_rainfall = df.groupby("Month")["Total_Rainfall_mm"].mean()








if __name__ == '__main__':
    # Example plot: average monthly rainfall
    plt.figure(figsize=(10, 6))
    monthly_avg_rainfall.plot(kind='bar')
    plt.title("Average Monthly Rainfall")
    plt.xlabel("Month")
    plt.ylabel("Average Rainfall (mm)")
    plt.show()
    print("Hy")