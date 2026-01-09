# -*- coding: utf-8 -*-
"""
Created on Wed Jan  7 11:19:42 2026

@author: aengstrom
"""
import argparse
from pathlib import Path
from .process_txt_to_csv import process_txt_to_csv

def main()-> None:
    parser = argparse.ArgumentParser(prog="txt-to-crosstab",
                                     description="Convert chromatogram TXT files to crosstab CSVs")
    
    parser.add_argument(
        "--site",
        required=True,
        help="Site code (e.g. RB)",
    )
    
    parser.add_argument(
        "--input",
        type=Path,
        required=True,
        help="Folder containing raw TXT files",
    )
    
    parser.add_argument(
        "--output",
        type=Path,
        required=True,
        help="Output folder for generated CSVs",
    )
    
    args = parser.parse_args()
    
    process_txt_to_csv(site = args.site, 
                       txt_folder = args.input,
                       csv_output_folder = args.output)
    
if __name__ == "__main__":
    main()
