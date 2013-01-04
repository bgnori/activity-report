#!/usr/bin/python
# -*- coding: utf-8 -*-

from bisect import bisect

from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta


from report import build
from activity import foo

data = sorted(sum(foo(date(2012, 12, 21)), []), key=lambda p: p[0])
keys = [r[0] for r in data]

def bar(start, d, h):
    t = datetime.combine(start, time()) + d + h
    idx = bisect(keys, t)
    #print data[idx]
    return data[idx][1]

build("/home/nori/Desktop/work/pdf/forDayCare/test.pdf", 
        date(2012, 12, 23),
        bar)

