📊 AI Data Quality Checker Agent

An automated data quality checking tool that analyzes CSV files and identifies common data quality issues such as missing values and duplicate records.

🚀 Features

- 📁 Upload CSV datasets
- 🔍 Detect missing values
- 🔁 Detect duplicate rows
- 📊 Display dataset information
- 💯 Calculate an overall data quality score
- 💡 Provide data-cleaning recommendations
- 🖥️ Simple Streamlit interface

🛠️ Technologies Used

- Python
- Pandas
- Streamlit
- GitHub

📂 Project Structure

AI-Data-Quality-Checker-Agent/
│
├── app.py
├── data_quality_checker.py
├── requirements.txt
├── README.md
│
└── sample_data/
    └── sample.csv

⚙️ Setup

1. Clone the repository

git clone https://github.com/Mounika231154/ai-data-quality-checker-agent.git

2. Open the project folder

cd ai-data-quality-checker-agent

3. Install the required libraries

pip install -r requirements.txt

▶️ Usage

Run the Streamlit application:

streamlit run app.py

The application will open in your browser.

Steps

1. Open the application.
2. Upload a CSV file.
3. The agent analyzes the dataset.
4. Review the data quality report.
5. Check missing values and duplicate records.
6. Follow the recommendations provided by the agent.

📄 Sample Dataset

A sample CSV file is available in:

sample_data/sample.csv

The sample dataset contains intentional missing values and duplicate records for testing.

📊 Sample Output

Example:

DATA QUALITY REPORT

Rows: 8
Columns: 4

Quality Score: 81.25%

Missing Values:
Age: 2
Email: 2

Duplicate Rows:
1

Recommendations:
→ Fill or remove missing values.
→ Remove duplicate records.

🔮 Future Improvements

- Detect invalid email addresses
- Detect incorrect data types
- Detect unusual or inconsistent values
- Generate detailed data-quality reports
- Add AI-generated explanations
- Export the quality report
- Add more validation rules

👨‍💻 Author
Meganath KM

GitHub:
https://github.com/Meganath-KM
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