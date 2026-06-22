import pandas as pd
from sqlalchemy import create_engine

class DataIngestion:

    def load_csv(self, file_path):
        df = pd.read_csv(file_path)
        return df

    def load_postgres(self, db_url, table_name):
        engine = create_engine(db_url)
        df = pd.read_sql(table_name, engine)
        return df