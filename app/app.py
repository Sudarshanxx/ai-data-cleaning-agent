import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="AI Data Cleaning Agent V1",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 AI Data Cleaning & Preprocessing Agent v1")

uploaded_file = st.file_uploader(
    "Upload CSV File",
    type=["csv"]
)

if uploaded_file is not None:

    try:
        df = pd.read_csv(uploaded_file)

        st.subheader("📊 Original Dataset")
        st.dataframe(df)

        st.subheader("📈 Dataset Information")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric("Rows", len(df))

        with col2:
            st.metric("Columns", len(df.columns))

        with col3:
            st.metric("Duplicates", int(df.duplicated().sum()))

        st.subheader("🔍 Missing Values")
        st.dataframe(df.isnull().sum())

        if st.button("🧹 Clean Data"):

            cleaned_df = df.copy()

            # Remove duplicates
            cleaned_df = cleaned_df.drop_duplicates()

            # Clean data
            for col in cleaned_df.columns:

                numeric_col = pd.to_numeric(
                    cleaned_df[col],
                    errors="coerce"
                )

                if numeric_col.notna().sum() > 0:

                    cleaned_df[col] = numeric_col.fillna(
                        numeric_col.mean()
                    )

                else:

                    cleaned_df[col] = (
                        cleaned_df[col]
                        .fillna("Unknown")
                        .astype(str)
                        .str.strip()
                        .str.lower()
                    )

            st.success("✅ Data Cleaned Successfully")

            st.subheader("🧹 Cleaned Dataset")
            st.dataframe(cleaned_df)

            csv = cleaned_df.to_csv(index=False)

            st.download_button(
                label="📥 Download Cleaned CSV",
                data=csv,
                file_name="cleaned_data.csv",
                mime="text/csv"
            )

    except Exception as e:
        st.error(f"Error: {str(e)}")

else:
    st.info("📂 Upload a CSV file to begin.")