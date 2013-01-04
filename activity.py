#!/usr/bin/python
# -*- coding: utf-8 -*-

import re
from datetime import datetime
from datetime import date
from datetime import time
from datetime import timedelta

def filter_lifelog(f):
    data = []
    active = False
    for line in f:
        if line.startswith("#"):
            if line.startswith("# >>> lifelog"):
                active = True
            else:
                active = False
        if active:
            yield line

pattern = re.compile(
        r'(?P<header>^ \* (?P<hour>\d{2})(?P<minute>\d{2}))'
        r'|'
        r'(?P<content>^   \* (?P<disc>.*$))'
        r'|'
        r'(?P<nomatch>.*)' #surpress groupdict fail
        )

def activies(f):
    delta = timedelta(0)
    for d in filter_lifelog(f):
        m = pattern.match(d)
        g = m.groupdict()
        if g.get('header'):
            delta = timedelta(hours=int(g["hour"]), minutes=int(g["minute"]))
        elif g.get("content"):
            yield delta, g['disc']
        else:
            pass

def sum_dict(iter):
    r = {}
    for k, v in iter:
        e = r.get(k, None)
        if e is None:
            e = []
        e.append(v)
        r[k] = e
    return r


def make_fname(d):
    return '{0:/home/nori/howm/%Y/%m/%Y-%m-%d-000000.txt}'.format(d)

def foo(since, until=None):
    assert isinstance(since, date)
    Aday = timedelta(days=1)
    result = {}
    if until is None:
        until = date.today()
    while since <= until:
        with file(make_fname(since), 'r') as f:
            yield [(datetime.combine(since, time()) + d, a) for d, a in activies(f)]
        since += Aday

for v in sorted(sum(foo(date(2012, 12, 21)), []), key=lambda p: p[0]):
    for t in v:
        print t 

