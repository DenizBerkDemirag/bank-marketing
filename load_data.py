import pandas as pd
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent

def load_data():

    file_dir = ROOT_DIR / "data" / "raw" / "bank-full.csv"
    df = pd.read_csv(file_dir, sep=';')
    return df