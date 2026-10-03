import pandas as pd
import re


def check_data_quality(df):
    report = {}

    # Basic information
    report["rows"] = len(df)
    report["columns"] = len(df.columns)

    # Missing values
    missing = df.isnull().sum()
    report["missing_values"] = missing[missing > 0].to_dict()

    # Duplicate rows
    report["duplicate_rows"] = int(df.duplicated().sum())

    # Invalid values
    invalid_values = {}

    for column in df.columns:
        if df[column].dtype == "object":
            invalid_values[column] = int(
                df[column].isna().sum()
            )

    report["invalid_values"] = invalid_values

    # Quality score
    total_cells = df.shape[0] * df.shape[1]

    missing_count = int(df.isnull().sum().sum())
    duplicate_count = int(df.duplicated().sum())

    issues = missing_count + duplicate_count

    if total_cells > 0:
        score = max(0, 100 - (issues / total_cells * 100))
    else:
        score = 0

    report["quality_score"] = round(score, 2)

    return report