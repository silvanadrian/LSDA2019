#!/usr/bin/env python3
import sys
import re

def preprocess(line):
    return line.split(",")

for line in sys.stdin:
    try:
        flight = preprocess(line)
        airline_id = int(flight[1])
        if flight[8] is "":
            arr_delay = 0.0
        else:
            arr_delay = float(flight[8])
            if arr_delay < 0.0:
            	continue
    except ValueError:
    	continue

    print('%s\t%s' % (arr_delay, airline_id))
