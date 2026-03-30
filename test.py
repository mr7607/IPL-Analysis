import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("orange_cap.csv")

# Calculate runs from boundaries
df['runs_from_4s'] = df['Fours'] * 4
df['runs_from_6s'] = df['Sixes'] * 6

# Runs from others (1s, 2s, 3s)
df['runs_other'] = df['Runs'] - (df['runs_from_4s'] + df['runs_from_6s'])

# Select top 10 batsmen
top = df.sort_values(by='Runs', ascending=False).head(10)

# Plot stacked bar chart
plt.figure()

plt.bar(top['Batsman'], top['runs_from_4s'], label='4s')
plt.bar(top['Batsman'], top['runs_from_6s'],
        bottom=top['runs_from_4s'], label='6s')
plt.bar(top['Batsman'], top['runs_other'],
        bottom=top['runs_from_4s'] + top['runs_from_6s'],
        label='Others')

plt.title("Run Distribution of Top Batsmen (IPL)")
plt.xlabel("Batsmen")
plt.ylabel("Runs")
plt.xticks(rotation=30)
plt.legend()

plt.show()