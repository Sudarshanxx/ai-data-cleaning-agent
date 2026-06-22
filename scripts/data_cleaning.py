import pandas as pd

class DataCleaning:

    def remove_duplicates(self, df):
        return df.drop_duplicates()

    def handle_missing_values(self, df):

        for col in df.columns:

            if df[col].dtype == "object":
                df[col] = df[col].fillna(df[col].mode()[0])

            else:
                df[col] = df[col].fillna(df[col].mean())

        return df

    def standardize_text(self, df):

        for col in df.select_dtypes(include="object"):

            df[col] = df[col].str.strip()
            df[col] = df[col].str.lower()

        return df