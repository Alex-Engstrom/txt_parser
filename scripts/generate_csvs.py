# -*- coding: utf-8 -*-
"""
Created on Wed Jan  7 14:13:56 2026

@author: aengstrom
"""

from pathlib import Path
from txt_to_crosstab.process_txt_to_csv import process_txt_to_csv

site = 'LP'

txt_folder = Path(r"C:\Users\aengstrom\Documents\Python\txt_parser\data\raw\202510LP_pre")
csv_output_folder = Path(r"C:\Users\aengstrom\Documents\Python\txt_parser\data\output\202510LPv1_post")

process_txt_to_csv(site = site, txt_folder = txt_folder, csv_output_folder = csv_output_folder)
