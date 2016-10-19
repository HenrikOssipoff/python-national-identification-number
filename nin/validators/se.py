#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

from datetime import date

from .generic import calculate_age

break_year = 2000


def is_valid(nin):
    nin = sanitize(nin)
    if len(nin) not in (10, 11, 12, 13):
        return False

    try:
        nin = humanize(nin)
    except ValueError:
        return False

    return True
    # Not implemented yet


def get_age(nin):
    nin = sanitize(nin)
    if len(nin) not in (10, 11, 12, 13):
        return None

    nin = humanize(nin)

    try:
        born = date(year=int(nin['year']), day=int(
            nin['day']), month=int(nin['month']))
    except Exception:
        return None

    return calculate_age(born)


def humanize(nin):
    if '-' not in nin and '+' not in nin:
        if len(nin) == 10:
            nin = '-'.join([nin[:6], nin[6:]])
        elif len(nin) == 12:
            nin = '-'.join([nin[2:8], nin[8:]])
    else:
        if len(nin) == 13:
            nin = '-'.join([nin[2:8], nin[9:]])
    year = nin[0:2]
    month = nin[2:4]
    day = nin[4:6]
    century = nin[6:7]
    control = nin[7:10]
    gender = nin[10:11]

    year_prefix = '19'
    if int(year) <= (date.today().year - break_year) and century == '-':
        year_prefix = '20'

    year = year_prefix + year

    return locals()


def sanitize(nin):
    return nin.strip()
