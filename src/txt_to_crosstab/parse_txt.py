# -*- coding: utf-8 -*-
"""
Created on Wed Jan  7 11:18:59 2026

@author: aengstrom
"""

from pathlib import Path
import logging
from .models import ChromatogramRun, Peak, Totals
from .validation import validate_txt_file, ValidationError
from .config import TOTALS, TXT_COMPOUNDS
from .parse_time import parse_full_datetime, parse_short_datetime
from .parse_filename import parse_filename
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG) 

def parse_txt_file(path: Path) -> ChromatogramRun:
    
    lines = path.read_text().splitlines() 
    
    validate_txt_file(lines)
    metadata = {}
    peaks = []
    totals = []
    # --- parse metadata ---
    for line in lines:
        if line.startswith("Front Signal"):
            break
        if "\t" in line:
            k, v = line.split("\t", 1)
            metadata[k.strip()] = v.strip()
    # --- parse signals ---
    current_signal = None
    for line in lines:
        if line.startswith("Front Signal"):
            current_signal = "PLOT"
            continue
        if line.startswith("Back Signal"):
            current_signal = "BP"
            continue

        if current_signal and line and line[0].isdigit():
            parts = line.split("\t")
            if len(parts) >= 6:
                _, name, amt, rt, area, rf = parts[:6]
                if name in TOTALS:
                    totals.append(
                        Totals(
                            name=name,
                            amount=float(amt),
                            area = int(area)
                            )
                        )  
                else:
                    peaks.append(
                        Peak(
                            name=name,
                            amount=float(amt),
                            rt=float(rt),
                            area=int(area),
                            rf=int(rf),
                            column=current_signal,
                        )
                    )
    return ChromatogramRun(
        site=metadata["Instrument"].split("-")[1],
        filename=metadata["Filename"],
        acquisition_time=parse_full_datetime(metadata["Acquisition Time"]),
        process_time=parse_full_datetime(metadata["Process Time"]),
        sample_name = metadata["Sample Name"],
        sample_number=parse_short_datetime(metadata["Sample number"]),
        sample_type = parse_filename(metadata["Filename"])["sample_type"],
        source_path=path,
        peaks=peaks,
        totals = totals
    )
        


        