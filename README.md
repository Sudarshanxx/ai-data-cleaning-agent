# 🤖 AI Data Cleaning & Preprocessing Agent

## 📌 Project Overview

The AI Data Cleaning & Preprocessing Agent is an intelligent data quality tool that automates the process of cleaning, validating, and preprocessing datasets.

The system allows users to upload CSV files, automatically detect data quality issues, clean the data, and download the processed dataset.

This project demonstrates the use of Python, Streamlit, Pandas, FastAPI, and PostgreSQL for building a production-style data engineering solution.

---

## 🚀 Features

### Data Ingestion

* Upload CSV datasets
* Read large datasets using Pandas
* Dataset preview

### Data Cleaning

* Remove duplicate records
* Handle missing values
* Standardize text fields
* Remove leading/trailing spaces
* Convert text to lowercase
* Handle invalid numeric values

### Data Analysis

* Dataset statistics
* Row count
* Column count
* Duplicate count
* Missing value analysis

### Data Export

* Download cleaned dataset as CSV

### Database Integration

* PostgreSQL connectivity
* Store cleaned datasets
* Future support for automatic database cleaning

---

## 🏗️ Project Architecture

User Upload CSV
↓
Streamlit Dashboard
↓
Pandas Data Processing
↓
Data Cleaning Engine
↓
Data Validation
↓
Clean Dataset Output
↓
CSV Download / PostgreSQL Storage

---

## 🛠️ Technology Stack

### Frontend

* Streamlit

### Backend

* Python

### Data Processing

* Pandas
* NumPy

### API Framework

* FastAPI
* Uvicorn

### Database

* PostgreSQL

### Machine Learning (Future Scope)

* Scikit-Learn

---

## 📂 Project Structure

```text
Euron_AI_agent_data_cleaning/
│
├── app/
│   └── app.py
│
├── scripts/
│   ├── backend.py
│   ├── ai_agent.py
│   ├── data_cleaning.py
│   ├── preprocessing.py
│   ├── data_ingestion.py
│   └── main.py
│
├── employees.csv
├── requirements.txt
├── README.md
└── ai_data_cleaning_env/
```

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/your-username/ai-data-cleaning-agent.git
cd ai-data-cleaning-agent
```

### Create Virtual Environment

```bash
python -m venv ai_data_cleaning_env
```

### Activate Environment

Windows:

```bash
ai_data_cleaning_env\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Streamlit Application

```bash
streamlit run app.py
```

Application URL:

```text
http://localhost:8501
```

---

## ▶️ Running FastAPI Backend

```bash
uvicorn backend:app --reload
```

Swagger Documentation:

```text
http://localhost:8000/docs
```

---

## 📊 Example Dataset

```csv
id,name,age,city,salary
1,Alice,25,New York,50000
2,Bob,,Los Angeles,60000
3,Charlie,28,Chicago,70000
4,David,35,Houston,
5,Eve,40,San Francisco,90000
5,Eve,40,San Francisco,90000
```

---

## 🔍 Cleaning Operations Performed

* Duplicate Detection
* Duplicate Removal
* Missing Value Detection
* Missing Value Imputation
* Text Standardization
* Numeric Data Validation
* Invalid Value Handling

---

## 🎯 Future Enhancements

* AI-powered cleaning suggestions using LLMs
* Automated database cleaning
* Excel (.xlsx) support
* Data Quality Scoring
* Outlier Detection
* Great Expectations Integration
* Scheduled Cleaning Jobs
* Multi-user Authentication
* Cloud Deployment

---

## 📈 Use Cases

* Data Engineering
* Business Intelligence
* ETL Pipelines
* Data Quality Management
* Analytics Preparation
* Enterprise Reporting

---


