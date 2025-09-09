
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder

def load_data(path: str) -> pd.DataFrame:
    """Load dataset from CSV."""
    return pd.read_csv(path)

def preprocess_data(df: pd.DataFrame, target: str):
    """Preprocess dataset: encode categorical, scale numerical, split train/test."""
    X = df.drop(columns=[target])
    y = df[target]

    # Encode categorical
    for col in X.select_dtypes(include=["object"]).columns:
        le = LabelEncoder()
        X[col] = le.fit_transform(X[col].astype(str))

    # Scale numerical
    scaler = StandardScaler()
    X[X.select_dtypes(include=["int64", "float64"]).columns] = scaler.fit_transform(
        X.select_dtypes(include=["int64", "float64"])
    )

    return train_test_split(X, y, test_size=0.2, random_state=42)
