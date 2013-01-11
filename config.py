#!/usr/bin/python
# -*- coding: utf-8 -*-

import os

settings = {
    'Kongoh': {
      'comment': 'for NotePC',
      'output':"/home/nori/Desktop/work/activity-tool/test.pdf",
      'font': {
        'name': "Takao Gothic",
        'path': '/usr/share/fonts/truetype/takao-gothic/TakaoGothic.ttf',
        },
      'report': {
        'test': ''

        },
      },
    'akagi': {
      'comment': 'for Desktop at home',
      'output':"/home/nori/Desktop/work/activity-tool/test.pdf",
      'font': {
        'name': "IPA Gothic",
        'path': '/usr/share/fonts/ipa-gothic/ipag.ttf',
        },
      'report': {
        'test': "/home/nori/Desktop/work/pdf/forDayCare/test.pdf",
        },
      },
    }

config = settings[os.uname()[1]]

