import pandas as pd
# Placeholder example: summary.py


def load_data(filepath):
    # Load CSV with Pandas
    print("==================================")
    print("Loading Data...")
    print("==================================")
    return pd.read_csv(filepath)


def clean_data(df):
    # Fill or drop missing values
    print("==================================")
    print("Cleaning Data...")
    print("==================================")
    df["temperature_C"] = df["temperature_C"].fillna(
        df["temperature_C"].mean())
    df["humidity_%"] = df["humidity_%"].fillna(df["humidity_%"].mean())
    df["wind_speed_kmph"] = df["wind_speed_kmph"].fillna(
        df["wind_speed_kmph"].mean())
    df["pressure_hPa"] = df["pressure_hPa"].fillna(df["pressure_hPa"].mean())
    df["visibility_km"] = df["visibility_km"].fillna(
        df["visibility_km"].mean())


def compute_summary(df):
    # Return dictionary of stats (mean, min, max) for selected numeric columns
    print("==================================")
    print("Generating Summary...")
    print("==================================")
    columns = ["temperature_C", "humidity_%",
               "wind_speed_kmph", "pressure_hPa", "visibility_km"]
    summary = {}

    for col in columns:
        summary[col] = {
            "mean": round(df[col].mean(), 2),
            "min": round(df[col].min(), 2),
            "max": round(df[col].max(), 2)
        }

    return summary


def save_summary(summary, output_path):
    # Write summary dict to a text file
    print("==================================")
    print("Saving Summary...")
    print("==================================")
    with open(output_path, 'w') as f:
        for feature, stats in summary.items():
            f.write(f"{feature}:\n")
            for stat_name, value in stats.items():
                f.write(f"  {stat_name}: {value}\n")
            f.write("\n")
    print("==================================")
    print("Summary saved successfully...")
    print("==================================")
