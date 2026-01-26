from pathlib import Path
import pandas as pd

REQUIRED_COLUMNS = [
    "recipe_id",
    "task_id",
    "temperature_c",
    "operator",
    "test_date",
]


def read_analog_test_excel(path: Path) -> pd.DataFrame:
    if path.suffix.lower() == ".xlsx":
        df = pd.read_excel(path, engine="openpyxl")
    elif path.suffix.lower() == ".xls":
        df = pd.read_excel(path, engine="xlrd")
    else:
        raise ValueError(f"Unsupported Excel format: {path}")

    missing = set(REQUIRED_COLUMNS) - set(df.columns)
    if missing:
        raise ValueError(f"Missing columns: {missing}")

    df = df[REQUIRED_COLUMNS].copy()

    df["test_date"] = df["test_date"].astype(str)

    return df
