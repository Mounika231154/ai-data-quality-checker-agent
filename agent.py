from tools import check_data_quality


class DataQualityAgent:

    def analyze(self, file):
        report = check_data_quality(file)

        issues = []

        if report["Missing Values"] > 0:
            issues.append(
                f"Found {report['Missing Values']} missing values."
            )

        if report["Duplicate Rows"] > 0:
            issues.append(
                f"Found {report['Duplicate Rows']} duplicate rows."
            )

        if not issues:
            issues.append("No major data quality issues found.")

        return {
            "report": report,
            "issues": issues
        }