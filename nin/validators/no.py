#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import date
from generic import calculate_age

def is_valid(nin):
    nin = sanitize(nin)
    if len(nin) != 11:
        return False

    nin = humanize(nin)

    return True
    # Not implemented yet

def get_age(nin):
    nin = sanitize(nin)
    if len(nin) != 11:
        return None

    nin = humanize(nin)

    try:
        born = date(year=int(nin['year']), day=int(nin['day']), month=int(nin['month']))
    except Exception:
        return None

    return calculate_age(born)

def humanize(nin):
    day = nin[0:2]
    month = nin[2:4]
    year = nin[4:6]
    individual = nin[6:9]
    control = nin[9:11]

    if int(individual) < 500:
        year = str(int(year) + 1900)
    else:
        year = str(int(year) + 2000)

    return locals()

def sanitize(nin):
    return nin.strip()
