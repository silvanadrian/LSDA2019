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
        try:
            airline_id = int(flight[1])
            if flight[8] is "":
                arr_delay = 0.0
            else:
                arr_delay = float(flight[8])
        except ValueError:
            continue
        print('%s\t%s' % (airline_id, arr_delay))
