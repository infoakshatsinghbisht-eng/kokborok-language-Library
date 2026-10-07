# -*- coding: utf-8 -*-
"""Kokborok Lunar-Solar Calendar, Seasons, and Kokborok Day."""

from ..constants import KOKBOROK_MONTHS, DAYS_OF_WEEK, SEASONS, KOKBOROK_DAY

def get_months():
    return KOKBOROK_MONTHS

def get_days():
    return DAYS_OF_WEEK

def get_seasons():
    return SEASONS

def get_kokborok_day_info():
    return {
        "date": "19 January",
        "name": "Kokborok Sal (Kokborok Day)",
        "commemoration": "Celebrates the official language recognition of Kokborok by the Government of Tripura in 1979."
    }
