# -*- coding: utf-8 -*-
"""
Created on Wed Jan  7 11:18:46 2026

@author: aengstrom
"""

from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path

@dataclass
class Peak:
    name: str
    amount: float
    rt: float
    area: int
    rf: int
    column: str
    
@dataclass 
class Totals:
    name: str 
    amount: float 
    area: int
    
@dataclass
class ChromatogramRun:
    site: str
    filename: str
    acquisition_time: datetime
    process_time: datetime
    sample_name: str
    sample_number: datetime
    sample_type: str
    source_path: Path
    peaks: list[Peak] = field(default_factory = list)
    totals: list[Totals] = field(default_factory = list)