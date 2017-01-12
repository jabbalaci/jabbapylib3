# coding: utf-8

from io import StringIO

from jplib.number import number_to_words as ntw
from six.moves import xrange


def test_number_to_words():
    assert ntw.convert(1) == 'one'
    assert ntw.convert(10) == 'ten'
    assert ntw.convert(100) == 'one hundred'
    assert ntw.convert(977) == 'nine hundred and seventy-seven'
    assert ntw.convert(1000) == 'one thousand'
    #
    buf = StringIO()
    for i in xrange(1, 1000+1):
        print(ntw.convert(i), file=buf)
    s = buf.getvalue()
    s = s.replace(' ', '').replace('-', '').replace('\n', '')
    assert len(s) == 21124
