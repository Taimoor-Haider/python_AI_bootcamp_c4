# Placeholder example: main.py
import argparse
from scripts import summary

parser = argparse.ArgumentParser()
parser.add_argument('--input', type=str, required=True)
parser.add_argument('--output', type=str, required=True)
args = parser.parse_args()

# Workflow
# 1. Load data
df = summary.load_data("./data/hourly_weather_10_days.csv")
# 2. Clean data
summary.clean_data(df)
# 3. Compute summary
summary_res = summary.compute_summary(df)
# 4. Save output
summary.save_summary(summary_res, "./output/results.txt")
