from datetime import datetime
import time
import re
from exceptions import DateException


def check_date(date_string):
    pattern = re.compile('(?P<day>\d{1,2})[.](?P<month>\d{1,2})[.](?P<year>\d{1,4})')
    mat = pattern.match(date_string)
    if int(mat.group('year')) >= 1:
        if int(mat.group('year'))/4 == int(mat.group('year'))/4.0\
          and int(mat.group('year'))/100 != int(mat.group('year'))/100.0:
            visokosn=1
        else:
            visokosn=0
        if int(mat.group('month')) in (1, 3, 5, 7, 8, 10, 12)\
          and int(mat.group('day')) in (1-31)\
          or int(mat.group('month')) in (4,6,9,11)\
          and int(mat.group('day')) <= 30 or int (mat.group('month')) == 2\
          and visokosn == 1 and int(mat.group('day')) <= 29\
          or int (mat.group('month')) == 2 and visokosn == 0\
          and int(mat.group('day')) <= 28:
            return time.strptime(date_string, "%d.%m.%Y")
        else:
            raise DateException("Invalid Format!")
    else:
        raise DateException("Invalid Format!")


