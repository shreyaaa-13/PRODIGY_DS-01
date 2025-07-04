import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load and clean data
df = pd.read_csv("Task-01.csv", on_bad_lines='skip')
df.columns = df.columns.str.strip()

df_pop = df[["Country Name", "2024"]].dropna()
top_10 = df_pop.sort_values(by="2024", ascending=False).head(10)
top_10.columns = ["Country", "Population"]

# Plot
plt.figure(figsize=(12, 6))
plt.bar(top_10["Country"], top_10["Population"], color='orchid')
plt.title("Top 10 Most Populous Countries (2024)", fontsize=14)
plt.xlabel("Country")
plt.ylabel("Population")
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
