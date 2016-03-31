#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from collections import OrderedDict

rates = {}

for line in open('rates.csv'):
    date, rate = line.strip().split(',')
    rate = float(rate)
    date = date[-4:]+'-'+date[3:5]+'-'+date[:2]
    rates[date] = rate


by_category = {}

#print 'date\tsumm\twhat\tusd_rate\tsum_usd'
for line in sys.stdin:

    try:
        date, summ, what = line.split(' - ')[:3]
    except:
        continue

    what = what.split('.', 1)[0]
    summ = float(summ.replace(' ', '').strip('p').strip('р'))

    #print date, '\t', summ,'\t', what, '\t', rates[date], '\t', summ / rates[date]
    if what not in by_category:
        by_category[what] = 0.
    by_category[what] += summ / rates[date]

keys = by_category.keys()
keys.sort(key = by_category.get)

for key in keys:
    print key,'\t', by_category[key]