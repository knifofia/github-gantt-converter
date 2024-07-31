from datetime import datetime

import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.dates import DateFormatter, DayLocator

# Load the TSV file
file_path = "Gantt.tsv"

# Read the TSV file into a DataFrame
df = pd.read_csv(file_path, sep="\t")

# Convert dates to datetime
df["Start date"] = pd.to_datetime(df["Start date"], format="%b %d, %Y")
df["End date"] = pd.to_datetime(df["End date"], format="%b %d, %Y")

# Plotting the Gantt chart
fig, ax = plt.subplots(figsize=(10, 6))

# Creating bars for each task
for idx, row in df.iterrows():
    ax.barh(
        row["Title"],
        (row["End date"] - row["Start date"]).days,
        left=row["Start date"],
        align="center",
    )

# Formatting the date on the x-axis
date_form = DateFormatter("%b %d")
ax.xaxis.set_major_formatter(date_form)
ax.xaxis.set_major_locator(DayLocator(interval=10))

plt.xlabel("Date")
plt.ylabel("Task")
plt.title("Gantt Chart")
plt.grid(True)
plt.tight_layout()

# Save the figure as an image
plt.savefig("out/gantt_chart_from_tsv.png")

plt.show()
