#!/usr/bin/python
# -*- coding: utf-8 -*-

from bisect import bisect_left

from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta


from report import build #view
from activity import foo, sum_dict
from config import config


xs = sum(foo(date(2012, 12, 21), date(2012, 12, 30)), [])
ys = sum_dict(xs).items()

data = sorted(ys, key=lambda p: p[0])
keys = [r[0] for r in data]

def bar(start, d, h):
    t = datetime.combine(start, time()) + d + h
    idx = bisect_left(keys, t)
    print 'query:', t
    print 'reply:'
    print data[idx][0]
    r = '\n'.join(data[idx][1])
    print r
    return r

build(config['output'], date(2012, 12, 23),bar)
