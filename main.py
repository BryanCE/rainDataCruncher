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

# flattens json data to make it nicer for dataframes
df = pd.json_normalize(rain_data, 'Month_Data', ['Grid_ID'])
#df = pd.json_normalize(rain_data)
print("DataFrame:\n")
print(df.head())
print("\n\n")


# Monthly average rainfall
monthly_avg_rainfall = df.groupby("Month")["Total_Rainfall_mm"].mean()
print("Monthly Average Rainfall:\n")
print(monthly_avg_rainfall)
print("\n\n")

# Monthly average rainfall
avg_rainfall_by_grid = df.groupby("Grid_ID")["Total_Rainfall_mm"].mean()
print("Average Rainfall by Grid:\n")
print(avg_rainfall_by_grid)
print("\n\n")








if __name__ == '__main__':
    # Example plot: average monthly rainfall
    plt.figure(figsize=(10, 6))
    monthly_avg_rainfall.plot(kind='line')
    plt.title("Average Rainfall by Grid")
    plt.xlabel("Grid ID")
    plt.ylabel("Average Rainfall (mm)")
    plt.show()
    print("Hy")