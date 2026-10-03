import pandas as pd


def check_data_quality(file):
    df = pd.read_csv(file)

    report = {
        "Rows": len(df),
        "Columns": len(df.columns),
        "Missing Values": int(df.isnull().sum().sum()),
        "Duplicate Rows": int(df.duplicated().sum()),
        "Columns": list(df.columns)
    }

    return report