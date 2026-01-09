# -*- coding: utf-8 -*-
"""
Created on Wed Jan  7 16:53:03 2026

@author: aengstrom
"""
from pathlib import Path
import pandas as pd
from txt_to_crosstab.config import COMPOUND_TO_AQS_CODE, SAMPLE_TYPES, SITENAMES
from txt_to_crosstab.io import find_txt_files, write_csv
from txt_to_crosstab.parse_txt import parse_txt_file
from txt_to_crosstab.transforms import run_to_df_amt

def process_txt_to_csv(site: str, txt_folder: Path, csv_output_folder: Path)->None:
    
    paths = find_txt_files(txt_folder)
    
    df = pd.concat(
        [run_to_df_amt(parse_txt_file(p)) for p in paths],
        ignore_index=False,
    )
    #Generate list of dataframes for each sampletype
    by_type = {}
    for sample_type in [letter.lower() for letter in SAMPLE_TYPES]:
        df_temp = df[df["sample_type"] == sample_type]
        df_temp = df_temp.drop("sample_type", axis = 1)
        by_type[sample_type] = df_temp
        
        
        
        
        
        
    for letter, data in by_type.items():    
        write_csv(data, site, csv_output_folder / f"amount_crosstab_run_[{letter.upper()}].csv")