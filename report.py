#!/usr/bin/python
# -*- coding: utf-8 -*-

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib.styles import getSampleStyleSheet

from reportlab.rl_config import defaultPageSize


from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.platypus import PageTemplate
from reportlab.platypus import Table


PAGE_HEIGHT = defaultPageSize[1]
PAGE_WIGTH = defaultPageSize[0]
styles = getSampleStyleSheet()

Title = "Hello Template"
pageinfo = "platypus example"

from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
pdfmetrics.registerFont(TTFont('IPA Gothic',
    '/usr/share/fonts/ipa-gothic/ipag.ttf'))


DAYS = ('Sun', 'Mon', 'Thu', 'Wed', 'Tue', 'Fri', 'Sat')
DAYS_JP = tuple(u'日月火水木金土')


def week():
    hours = list(range(5, 29))
    corner = ['hour/day']
    col_headers = DAYS_JP
    rows_headers = corner + hours

    xs = []
    for d in col_headers:
        x = ["%s"%(d,)] + ["%s %d00"%(d, h) for h in hours]
        xs.append(x)
    data = [rows_headers] + xs

    t = Table(zip(*data))

    t.setStyle([
            ('FONT', (0,0), (-1,-1), 'IPA Gothic'),
            ('TEXTCOLOR', (1,0), (1,0), colors.red),
            ('TEXTCOLOR', (7,0), (7,0), colors.blue)])
    return t


doc = SimpleDocTemplate("/home/nori/Desktop/work/pdf/forDayCare/test.pdf", pagesize=A4)
content = [Spacer(1, 20*mm)]

style = styles["Normal"]

content.append(week())

content.append(Spacer(1, 5*mm))
doc.build(content)


