class DataCleaningAgent:

    def suggest_cleaning(self, df):

        report = {}

        report["rows"] = len(df)
        report["columns"] = len(df.columns)
        report["missing_values"] = df.isnull().sum().to_dict()
        report["duplicates"] = int(df.duplicated().sum())

        return report