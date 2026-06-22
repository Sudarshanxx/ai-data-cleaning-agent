from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler

class Preprocessing:

    def encode_categorical(self, df):

        le = LabelEncoder()

        for col in df.select_dtypes(include='object'):

            df[col] = le.fit_transform(df[col])

        return df

    def scale_features(self, df):

        scaler = StandardScaler()

        numeric_cols = df.select_dtypes(include=['int64','float64']).columns

        df[numeric_cols] = scaler.fit_transform(df[numeric_cols])

        return df