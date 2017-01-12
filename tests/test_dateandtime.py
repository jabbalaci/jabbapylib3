# coding: utf-8

import re
from datetime import datetime

from jplib import dateandtime as dat
from jplib import process


class TestDateAndTime(object):

    def setup_method(self, method):
        self.ts = 1111111111
        self.dt = datetime.fromtimestamp(self.ts)

    ##########

    def test_get_timestamp_from_year_to_second_01(self):
        res = dat.get_timestamp_from_year_to_second()
        assert re.search('^\d{8}_\d{6}$', res)

    def test_get_timestamp_from_year_to_second_02(self):
        res = dat.get_timestamp_from_year_to_second(separator=True)
        assert re.search('^\d{4}_\d\d_\d\d_\d{6}$', res)

    def test_get_timestamp_from_year_to_second_03(self):
        res = dat.get_timestamp_from_year_to_second(date=self.dt)
        assert res == '20050318_025831'

    def test_get_timestamp_from_year_to_second_04(self):
        res = dat.get_timestamp_from_year_to_second(separator=True, date=self.dt)
        assert res == '2005_03_18_025831'

    ##########

    def test_get_date_from_year_to_day(self):
        res = dat.get_date_from_year_to_day()
        assert re.search('^\d{4}_\d\d_\d\d$', res)
        #
        res = dat.get_date_from_year_to_day(separator=True)
        assert re.search('^\d{4}_\d\d_\d\d$', res)
        #
        res = dat.get_date_from_year_to_day(separator=False)
        assert re.search('^\d{8}$', res)

    ##########

    def test_get_time(self):
        res = dat.get_time()
        assert '0000' <= res <= '2359'

    ##########

    def test_datetime_to_unix_timestamp(self):
        res = dat.datetime_to_unix_timestamp(self.dt)
        assert res == 1111111111

    ##########

    def test_unix_timestamp_to_datetime(self):
        res = dat.unix_timestamp_to_datetime(self.ts)
        assert res.__str__() == '2005-03-18 02:58:31'

    ##########

    def test_get_unix_date(self):
        # Unix command 'date'
        date = process.get_simple_cmd_output('date').replace('\n', '')
        # pure Python 'date'
        python = dat.get_unix_date()
        assert date == python

    ##########

    def test_is_leap_year(self):
        assert dat.is_leap_year(1900) is False
        for year in (2000, 2004, 2012):
            assert dat.is_leap_year(year)

    ##########

    def test_sec_to_hh_mm_ss(self):
        value = 3596.26
        assert dat.sec_to_hh_mm_ss(value) == "0:59:56"
        assert dat.sec_to_hh_mm_ss(value, as_str=False) == (0, 59, 56)

    ##########

    def test_humanize_time(self):
        value = 13648
        assert dat.humanize_time(value) == "03:47:28 (hh:mm:ss)"
        assert dat.sec_to_hh_mm_ss(value, as_str=False) == (3, 47, 28)
