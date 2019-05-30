#!/usr/bin/env python3
import sys
import re

def preprocess(line):
    return line.split(",")

for line in sys.stdin:
    if re.match(".FL_DATE.", line):
        continue
    else:
        flight = preprocess(line)
        airline_id = int(flight[1])
        dep_delay = float(flight[6])
        print('%s\t%s' % (airline_id, dep_delay))
