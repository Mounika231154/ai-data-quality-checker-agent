# ai-data-quality-checker-agent
An AI-powered agent for detecting and analyzing data quality issues in CSV and Excel files.

📊 AI Data Quality Checker Agent

An AI-powered data quality checking agent that analyzes CSV datasets and identifies common data quality problems.

Features

- Detect missing values
- Detect duplicate rows
- Analyze dataset structure
- Calculate data quality score
- Generate data-cleaning recommendations
- Upload and analyze CSV files

Technologies

- Python
- Pandas
- Streamlit

Project Structure

AI-Data-Quality-Checker-Agent/
│
├── app.py
├── data_quality_checker.py
├── requirements.txt
├── README.md
│
└── sample_data/
    └── sample.csv

How It Works

1. Upload a CSV file.
2. The agent reads the dataset.
3. It checks for missing values and duplicate records.
4. It calculates a data quality score.
5. It displays the detected issues.
6. It provides recommendations for improving the dataset.

Example

The agent can identify issues such as:

- Missing values
- Duplicate records
- Incomplete datasets

Future Improvements

- Detect invalid email addresses
- Detect incorrect data types
- Add AI-generated explanations
- Generate downloadable quality reports
- Add more data validation rules