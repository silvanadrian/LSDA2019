#!/usr/bin/env python3
import sys
import re

def preprocess(line):
    return line.split(",")

for line in sys.stdin:
    if re.match(".FL_DATE.", line):
        continue
    flight = preprocess(line)
    airline_id = int(flight[1])
    flight_distance = float(flight[10])
    print('%s\t%s' % (airline_id, flight_distance))
