import streamlit as st
from agent import DataQualityAgent

st.set_page_config(
    page_title="AI Data Quality Checker",
    page_icon="🧹"
)

st.title("🧹 AI Data Quality Checker Agent")
st.write("Upload a CSV file to analyze its data quality.")

uploaded_file = st.file_uploader(
    "Upload your CSV file",
    type=["csv"]
)

if uploaded_file is not None:

    st.success("File uploaded successfully!")

    if st.button("🔍 Analyze Data"):

        agent = DataQualityAgent()
        result = agent.analyze(uploaded_file)

        st.subheader("📊 Data Quality Report")

        report = result["report"]

        st.write("**Rows:**", report["Rows"])
        st.write("**Columns:**", report["Columns"])
        st.write("**Missing Values:**", report["Missing Values"])
        st.write("**Duplicate Rows:**", report["Duplicate Rows"])

        st.subheader("⚠️ Issues Found")

        for issue in result["issues"]:
            st.write("•", issue)
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
