from fastapi import FastAPI, UploadFile, File
import pandas as pd
from io import StringIO

app = FastAPI(
    title="AI Data Cleaning Agent",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "message": "AI Data Cleaning Agent Running"
    }


@app.post("/analyze")
async def analyze(file: UploadFile = File(...)):

    contents = await file.read()

    df = pd.read_csv(
        StringIO(contents.decode("utf-8"))
    )

    report = {
        "rows": len(df),
        "columns": len(df.columns),
        "missing_values": df.isnull().sum().to_dict(),
        "duplicates": int(df.duplicated().sum())
    }

    return report


@app.post("/clean-data")
async def clean_data(file: UploadFile = File(...)):

    contents = await file.read()

    df = pd.read_csv(
        StringIO(contents.decode("utf-8"))
    )

    original_rows = len(df)

    # Remove duplicates
    df = df.drop_duplicates()

    # Handle missing values
    for col in df.columns:

        if df[col].dtype == "object":

            if df[col].isnull().sum() > 0:
                df[col] = df[col].fillna("Unknown")

            df[col] = df[col].astype(str).str.strip().str.lower()

        else:

            if df[col].isnull().sum() > 0:
                df[col] = df[col].fillna(df[col].mean())

    cleaned_rows = len(df)

    return {
        "status": "success",
        "original_rows": original_rows,
        "cleaned_rows": cleaned_rows,
        "columns": list(df.columns),
        "data": df.to_dict(orient="records")
    }


@app.post("/clean-db")
def clean_db():

    return {
        "message": "Database Cleaning Endpoint Ready"
    }


@app.post("/clean-api")
def clean_api():

    return {
        "message": "API Data Cleaning Endpoint Ready"
    }