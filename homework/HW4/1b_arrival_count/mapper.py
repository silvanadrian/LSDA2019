#!/usr/bin/env python3
import sys

def preprocess(line):
    return line.strip().split(",")

for line in sys.stdin:

    flight = preprocess(line)

    if flight[8] == "":
        flight[8] = 0

    try:
        airline_id = int(flight[1])
        arr_delay = float(flight[8])
        if arr_delay > 0:
            arr_delay = 1
        else:
            arr_delay = 0
    except ValueError:
        continue
    print('%s\t%s' % (airline_id, arr_delay))
