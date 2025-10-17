import pandas as pd
import matplotlib.pyplot as plt

url = "https://raw.githubusercontent.com/datasets/global-temp/master/data/monthly.csv"
df = pd.read_csv(url)
df['Date'] = pd.to_datetime(df['Date'])
yearly = df.groupby(df['Date'].dt.year)['Mean'].mean()

plt.figure(figsize=(10,5))
yearly.plot(title="Global Average Temperature by Year (°C anomaly)")
plt.xlabel("Year")
plt.ylabel("Temp anomaly (°C)")
plt.grid(True)
plt.savefig("temperature_trend.png")
plt.show()
