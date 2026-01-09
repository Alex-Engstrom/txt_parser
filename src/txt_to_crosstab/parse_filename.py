# -*- coding: utf-8 -*-
"""
Created on Wed Jan  7 11:24:41 2026

@author: aengstrom
"""
from .config import FILENAME_FORMAT
import re
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG) 
def parse_filename(filename: str)->dict:
    pattern = FILENAME_FORMAT
    match = re.match(pattern, filename)
    if match:
        from_filename = match.groupdict()
    else:
        logger.error(f"Could not parse .dat file from filename: {filename.name}")
        return None
    return from_filename
        
    
