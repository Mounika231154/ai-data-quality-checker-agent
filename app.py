import streamlit as st
import pandas as pd
from data_quality_checker import check_data_quality

st.set_page_config(
    page_title="AI Data Quality Checker",
    page_icon="📊"
)

st.title("📊 AI Data Quality Checker Agent")

st.write(
    "Upload a CSV file and check its data quality automatically."
)

uploaded_file = st.file_uploader(
    "Upload your CSV file",
    type=["csv"]
)

if uploaded_file is not None:

    df = pd.read_csv(uploaded_file)

    st.subheader("📋 Dataset Preview")
    st.dataframe(df.head())

    report = check_data_quality(df)

    st.subheader("📊 Data Quality Report")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Rows", report["rows"])

    with col2:
        st.metric("Columns", report["columns"])

    with col3:
        st.metric(
            "Quality Score",
            f"{report['quality_score']}%"
        )

    st.subheader("⚠️ Missing Values")

    if report["missing_values"]:
        st.json(report["missing_values"])
    else:
        st.success("No missing values found.")

    st.subheader("🔁 Duplicate Rows")

    if report["duplicate_rows"] > 0:
        st.warning(
            f"{report['duplicate_rows']} duplicate rows found."
        )
    else:
        st.success("No duplicate rows found.")

    st.subheader("💡 Recommendations")

    if report["missing_values"]:
        st.write("→ Fill or remove missing values.")

    if report["duplicate_rows"] > 0:
        st.write("→ Remove duplicate records.")

    if not report["missing_values"] and report["duplicate_rows"] == 0:
        st.success(
            "Your dataset looks clean based on the checks performed."
        )"])

    with col3:
        st.metric(
            "Quality Score",
            f"{report['quality_score']}%"
        )

    st.subheader("⚠️ Missing Values")

    if report["missing_values"]:
        st.json(report["missing_values"])
    else:
        st.success("No missing values found.")

    st.subheader("🔁 Duplicate Rows")

    if report["duplicate_rows"] > 0:
        st.warning(
            f"{report['duplicate_rows']} duplicate rows found."
        )
    else:
        st.success("No duplicate rows found.")

    st.subheader("💡 Recommendations")

    if report["missing_values"]:
        st.write("→ Fill or remove missing values.")

    if report["duplicate_rows"] > 0:
        st.write("→ Remove duplicate records.")

    if not report["missing_values"] and report["duplicate_rows"] == 0:
        st.success(
            "Your dataset looks clean based on the checks performed."
        ) / total_cells) * 100, 2)
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
