import datetime
import time
import re
from exceptions import DateException


def check_date(date_string, delimiter='.', order='straight'):
    
    regexp = r'(?P<day>\d{1,2})[' + \
                delimiter + r'](?P<month>\d{1,2})[.](?P<year>\d{1,4})'
    pattern = re.compile(regexp)
    mat = pattern.match(date_string)
    year, day, month = ('', '', '')
    if mat:
        year = mat.group('year')
        if order == 'straight':
            day = mat.group('day')
            month = mat.group('month')
        else:
            day = mat.group('month')
            month = mat.group('day')
    else:
        raise DateException('Bad Date String')
    if len(mat.group('year')) == 2 and mat.goup('year')[0] == '0':
        year = '20' + year
    try:
        date_obj = datetime.date(int(year), int(month), int(day))
    except ValueError:
        raise DateException("Date is out of calendar range")
    return date_obj


