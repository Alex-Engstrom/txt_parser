# -*- coding: utf-8 -*-
"""
Created on Wed Jan  7 16:43:18 2026

@author: aengstrom
"""
from pathlib import Path
import pandas as pd
from txt_to_crosstab.process_txt_to_csv import process_txt_to_csv
TEST_DIR = Path(__file__).parent
DATA_DIR = TEST_DIR / "data"

RAW_TXT = DATA_DIR / "raw_txt"
EXPECTED = DATA_DIR / "expected_csv"

def normalize_df(df: pd.DataFrame, float_decimals: int = 3) -> pd.DataFrame:
    df = df.copy()

    # Drop index column if it's auto-generated
    if "Unnamed: 0" in df.columns:
        df = df.drop(columns=["Unnamed: 0"])

    # Normalize numeric columns
    for col in df.columns:
        def try_float(x):
            try:
                return round(float(x), float_decimals)
            except (ValueError, TypeError):
                return x
        df[col] = df[col].map(try_float)

    # Normalize DATE/TIME as string to match expected CSV
    if "DATE/TIME" == df.index.name:
        try:
            df.index = pd.to_datetime(df.index, errors="coerce")
            # Format to match expected CSV
            df.index = df.index.dt.strftime("%m/%d/%Y %#H:%M")
        except Exception:
            pass  # leave as-is if formatting fails

    # Sort columns for consistent comparison
    df = df.sort_index(axis=1)

    return df

def test_generated_csv_matches_expected(tmp_path):
    """
    End-to-end golden file test.
    """
    #run test txt
    process_txt_to_csv(site = 'RB', txt_folder = RAW_TXT, csv_output_folder = tmp_path)
    
    expected_csvs = [path.name for path in list(EXPECTED.iterdir())]
    created_csvs = [path.name for path in list(tmp_path.iterdir())]
    assert sorted(expected_csvs) == sorted(created_csvs)  
    # Load both CSVs
    for filename in created_csvs:  

        df_actual = pd.read_csv(Path(tmp_path) / filename, index_col=0, skiprows = 2)
        df_expected = pd.read_csv(EXPECTED / filename, index_col=0, skiprows = 2)

        df_actual = normalize_df(df_actual)
        df_expected = normalize_df(df_expected)

        # Assert equality
        pd.testing.assert_frame_equal(
            df_actual,
            df_expected,
            check_dtype=False,
            atol=1e-2
        )