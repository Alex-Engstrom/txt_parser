# -*- coding: utf-8 -*-
"""
Created on Wed Jan  7 11:19:24 2026

@author: aengstrom
"""
import csv
from pathlib import Path
from .config import SITENAMES, COMPOUND_TO_AQS_CODE 

def find_txt_files(root: Path)-> list[Path]:
    return sorted(root.glob("*.tx1"))   

def write_csv(df, site: str, path: Path):
    write_df = df.copy()
    #replace 0 with ""
    write_df = write_df.replace(0,"")
    first_header = [""]
    first_header.extend([f"{col.upper()}({SITENAMES[site]}) PPBC" for col in df.columns])
    second_header = [""]
    second_header.extend([compound.capitalize() if compound not in ['TNMTC','TNMHC'] else compound for compound in df.columns.tolist()])
    third_header = ["DATE/TIME"]
    third_header.extend([COMPOUND_TO_AQS_CODE.get(compound) for compound in df.columns.tolist()])
    with open(path, "w", newline ="") as f:
        writer = csv.writer(f)
        
        # Write header rows
        writer.writerow(first_header)
        writer.writerow(second_header)
        writer.writerow(third_header)
        
        # Write data rows
        for idx, row in write_df.iterrows():
            writer.writerow([idx] + row.tolist())
            
        