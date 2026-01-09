# -*- coding: utf-8 -*-
"""
Created on Wed Jan  7 11:19:13 2026

@author: aengstrom
"""
'''Convert ChromatogramRun objects to pandas dataframe'''
import pandas as pd
from .models import ChromatogramRun
from .config import TXT_COMPOUNDS, TOTALS
from .parse_txt import parse_txt_file
def run_to_df_amt(run:ChromatogramRun)->pd.DataFrame:
    sample_type = run.sample_type
    sample_time = run.sample_number
    peaks = run.peaks
    totals = run.totals
    peak_dict = {pk.name : pk.amount for pk in peaks}
    #Capitalize to match MAX formatting
    peak_dict = {key.capitalize(): item for key, item in peak_dict.items()}
    totals_dict = {tl.name : tl.amount for tl in totals}
    TNMHC = totals_dict["Plot UnID"]+totals_dict["BP UnID"] + totals_dict["PLOT Targets"] + totals_dict["BP Targets"]
    TNMTC = totals_dict["PLOT Targets"] + totals_dict["BP Targets"]
    combined_dict = peak_dict.copy()
    #Add totals to peak dict
    combined_dict['TNMHC'] = float(f"{TNMHC:.4f}")
    combined_dict['TNMTC'] = float(f"{TNMTC:.4f}")
    #Add date and sample type to combined dict
    combined_dict['DATE/TIME'] = sample_time
    combined_dict['sample_type'] = sample_type.lower()
    df = pd.DataFrame([combined_dict]).set_index('DATE/TIME')
    return df
    

