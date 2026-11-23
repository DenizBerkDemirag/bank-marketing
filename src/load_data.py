import sys
import pandas as pd
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT_DIR / "data" / "raw" / "bank-full.csv"

def load_data():

    if not DATA_DIR.exists():
        raise FileNotFoundError(f"File not found: {DATA_DIR}")
    df = pd.read_csv(DATA_DIR, sep=';')
    return df