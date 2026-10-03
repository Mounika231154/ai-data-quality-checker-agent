import pandas as pd


def check_data_quality(df):

    report = {}

    # Number of rows and columns
    report["rows"] = len(df)
    report["columns"] = len(df.columns)

    # Missing values
    missing = df.isnull().sum()

    report["missing_values"] = {
        column: int(count)
        for column, count in missing.items()
        if count > 0
    }

    # Duplicate rows
    report["duplicate_rows"] = int(
        df.duplicated().sum()
    )

    # Calculate quality score
    total_cells = df.shape[0] * df.shape[1]

    missing_count = int(
        df.isnull().sum().sum()
    )

    duplicate_count = int(
        df.duplicated().sum()
    )

    total_issues = missing_count + duplicate_count

    if total_cells > 0:
        score = 100 - (
            total_issues / total_cells * 100
        )
    else:
        score = 0

    report["quality_score"] = round(
        max(0, score), 2
    )

    return report().sum())

    issues = missing_count + duplicate_count

    if total_cells > 0:
        score = max(0, 100 - (issues / total_cells * 100))
    else:
        score = 0

    report["quality_score"] = round(score, 2)

    return report