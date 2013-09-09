#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import datetime
import dateutils

def sanitize(nin):
    # Sanitize
    if type(nin) is int:
        nin = str(nin)
    
    m = re.match('(\d{6})[- ]*(\d{4})', nin)
    if m is None or len(m.groups()) != 2:
        raise TypeError
   
    return '{0}{1}'.format(m.groups()[0], m.groups()[1])

def is_valid(nin):
    try:
        sanitize(nin)
    except:
        return False
    return True

def get_age(nin):
    # Should sanitize first
    nin = sanitize(nin)

    year_part = int(nin[4:6])
    day_part = nin[0:2]
    month_part = nin[2:4]
    century = None

    #Century indicator
    i = int(nin[6:7])

    if i in (0,1,2,3):
        century = '19'
    elif i == 4 and year_part < 37:
        century = '20'
    elif i == 4 and year_part > 36:
        century = '19'
    elif i in (5,6,7,8) and year_part < 58:
        century = '20'
    elif i in (5,6,7,8) and year_part > 57:
        century = '18'
    elif i == 9 and year_part < 38:
        century = '20'
    else:
        century = '19'
   
    #Get year from nin again, because we need it as a string
    year = int('{0}{1}'.format(century, nin[4:6]))
    date = datetime.date(year, int(month_part), int(day_part))
    today = datetime.date.today()

    ts = dateutils.relativedelta(today, date)
    return ts.years


