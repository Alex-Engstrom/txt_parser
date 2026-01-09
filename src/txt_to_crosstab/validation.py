# -*- coding: utf-8 -*-
"""
Created on Wed Jan  7 11:34:08 2026

@author: aengstrom
"""

from .config import TXT_COMPOUNDS
class ValidationError(Exception):
    pass

REQUIRED_MARKERS = [
    "Instrument",
    "Filename",    
    "Acquisition Time",
    "Process Time",
    "Sample Name",
    "Sample number",
    "Method",
    "Sequence",
    "Front Signal",
    "Peak Number"
]
REQUIRED_MARKERS.extend(TXT_COMPOUNDS)

def validate_required_markers(lines: list[str]) -> None:
    '''Checks if the required markers are present in the .txt file'''
    missing = [m for m in REQUIRED_MARKERS if not any(m in l for l in lines)]
    if missing:
        raise ValidationError(f"Missing required markers: {missing}")
        
def validate_txt_file(lines: list[str])-> None:
    validate_required_markers(lines)

    
        
    