# -*- coding: utf-8 -*-
"""
Created on Wed Jan  7 12:39:10 2026

@author: aengstrom
"""
from datetime import datetime
from .config import FULL_TIME_FORMAT, SHORT_TIME_FORMAT
def parse_full_datetime(dt: str)-> datetime:
    return datetime.strptime(dt, FULL_TIME_FORMAT)

def parse_short_datetime(dt: str)-> datetime:
    return datetime.strptime(dt, SHORT_TIME_FORMAT)
    