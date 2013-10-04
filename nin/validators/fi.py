#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import date
from generic import calculate_age

control_characters = ('0', '1', '2', '3', '4', '5', '6', '7',
    '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I',
    'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
    'U', 'V', 'W', 'X', 'Y'
)

def is_valid(nin):
    nin = sanitize(nin)
    if len(nin) != 11:
        return False

    nin = humanize(nin)

    if int(nin['year']) < 1800:
        return False

    try:
        date(year=int(nin['year']), day=int(nin['day']), month=int(nin['month']))
    except Exception:
        return False


    return True # For now

    control_digits = float(int(''.join([nin['day'], nin['month'], nin['year'][2:4], nin['control_digits']])))

    return nin['control_char'] == control_characters[int(control_digits % 31.)]

def get_age(nin):
    nin = sanitize(nin)
    if len(nin) != 11:
        return None

    nin = humanize(nin)

    if int(nin['year']) < 1800:
        return None

    try:
        born = date(year=int(nin['year']), day=int(nin['day']), month=int(nin['month']))
    except Exception:
        return None

    return calculate_age(born)

def humanize(nin):
    day = nin[0:2]
    month = nin[2:4]
    year = nin[4:6]
    century = nin[6:7]
    control_digits = nin[7:10]
    control_char = nin[10:11]

    if century == '+':
        year = str(int(year) + 1800)
    elif century == '-':
        year = str(int(year) + 1900)
    elif century == 'A':
        year = str(int(year) + 2000)

    return locals()

def sanitize(nin):
    return nin.strip()
