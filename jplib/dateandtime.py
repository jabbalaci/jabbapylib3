#!/usr/bin/env python3

"""
Stuff related to date and time.

# from jplib import dateandtime
# from jplib.dateandtime import get_timestamp_from_year_to_second
# from jplib.dateandtime import get_unix_date
# from jplib.dateandtime import get_time
"""

import calendar
import time
from datetime import datetime, timedelta
from time import strftime

MIN = 60            # 1 minute is 60 sec.
HOUR = 60 * MIN
DAY = 24 * HOUR
WEEK = 7 * DAY
MONTH = 30 * DAY
YEAR = 365 * DAY


def get_timestamp_from_year_to_second(separator=False, date=None):
    """A compact timestamp.

    Example: 20110523_234401 . date can be a datetime object.
    If date is not specified, the current date and time (now) will be used."""
    if date:
        now = date
    else:
        now = datetime.now()
    date = datetime.date(now)
    time = datetime.time(now)
    #return "%d-%02d-%02d @ %02dh%02d%02d" % (date.year, date.month, date.day, time.hour, time.minute, time.second)
    template = "{year}{month:02}{day:02}_{hour:02}{minute:02}{second:02}"
    if separator:
        template = "{year}_{month:02}_{day:02}_{hour:02}{minute:02}{second:02}"
    return template.format(year=date.year, month=date.month, day=date.day, hour=time.hour, minute=time.minute, second=time.second)


def get_date_from_year_to_day(separator=True):
    """A simplified timestamp.

    Example: 2011_10_29 or 20111029."""
    now = datetime.now()
    date = datetime.date(now)
    if separator:
        return "{year}_{month:02}_{day:02}".format(year=date.year, month=date.month, day=date.day)
    else:
        return "{year}{month:02}{day:02}".format(year=date.year, month=date.month, day=date.day)


def get_time():
    """
    Current time (HHMM).

    The return value is a string.
    """
    now = datetime.now()
    time = datetime.time(now)
    return "{hour:02}{minute:02}".format(hour=time.hour, minute=time.minute)


def datetime_to_unix_timestamp(date):
    """Convert a datetime to Unix timestamp.

    date is a datetime object, the return value is an int."""
    # http://stackoverflow.com/questions/2775864/python-datetime-to-unix-timestamp
    return int(time.mktime(date.timetuple()))


def unix_timestamp_to_datetime(timestamp):
    """Convert a Unix timestamp to datetime.

    The return value is a datetime object."""
    # http://stackoverflow.com/questions/3682748/converting-unix-timestamp-string-to-readable-date-in-python
    return datetime.fromtimestamp(timestamp)


def get_unix_date():
    """Same output as Unix's date command.

    Example: Fri Apr  6 14:23:27 CEST 2012"""
    return strftime("%a %b %e %H:%M:%S %Z %Y")


def is_leap_year(year):
    """Returns True if year is a leap year, otherwise False."""
    return calendar.isleap(year)


def sec_to_hh_mm_ss(seconds, as_str=True):
    """
    Convert a time given in seconds to H:MM:SS format.

    If as_str is True, the return value is a string.
    If as_str is False, the return value is a tuple (H:MM:SS).
    """
    s = str(timedelta(seconds=int(round(seconds))))
    if as_str:
        return s
    else:
        return tuple([int(x) for x in s.split(':')])


def humanize_time(secs):
    """
    Convert seconds to hh:mm:ss format.
    """
    secs = int(secs)
    mins, secs = divmod(secs, 60)
    hours, mins = divmod(mins, 60)
    return '{h:02d}:{m:02d}:{s:02d} (hh:mm:ss)'.format(h=hours, m=mins, s=secs)

#############################################################################

if __name__ == "__main__":
    print(get_timestamp_from_year_to_second(separator=True))
    print(get_date_from_year_to_day())
    now = datetime.now()
    print(datetime_to_unix_timestamp(now))
    ts = 1111111111
    dt = unix_timestamp_to_datetime(ts)
    print(dt)
    print(get_timestamp_from_year_to_second(date=dt))
    print(get_unix_date())
    print(is_leap_year(2012))
    print(sec_to_hh_mm_ss(3596.26))
    print(get_time())
    print(humanize_time(13648))
