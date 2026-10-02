import streamlit as st
import pandas as pd

st.set_page_config(page_title="AI Data Quality Checker", page_icon="📊")

st.title("📊 AI Data Quality Checker Agent")

uploaded_file = st.file_uploader(
    "Upload CSV or Excel File",
    type=["csv", "xlsx"]
)

if uploaded_file is not None:

    # Read file
    if uploaded_file.name.endswith(".csv"):
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.read_excel(uploaded_file)

    st.subheader("Dataset Preview")
    st.dataframe(df.head())

    # Missing values
    missing_values = df.isnull().sum().sum()

    # Duplicate rows
    duplicate_rows = df.duplicated().sum()

    # Total cells
    total_cells = df.shape[0] * df.shape[1]

    # Quality score
    issue_count = missing_values + duplicate_rows

    if total_cells > 0:
        quality_score = max(
            0,
            round((1 - issue_count / total_cells) * 100, 2)
        )
    else:
        quality_score = 100

    st.subheader("Data Quality Report")

    col1, col2, col3 = st.columns(3)

    col1.metric("Missing Values", missing_values)
    col2.metric("Duplicate Rows", duplicate_rows)
    col3.metric("Quality Score", f"{quality_score}%")

    # Detailed report
    st.subheader("Missing Values by Column")
    st.write(df.isnull().sum())

    st.subheader("Duplicate Rows")
    st.write(duplicate_rows)

    if quality_score >= 90:
        st.success("Excellent Data Quality ✅")
    elif quality_score >= 70:
        st.warning("Moderate Data Quality ⚠️")
    else:
        st.error("Poor Data Quality ❌")
