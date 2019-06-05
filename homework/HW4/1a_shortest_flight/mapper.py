#!/usr/bin/env python3
import sys
import re

def preprocess(line):
    return line.strip().split(",")

for line in sys.stdin:
    flight = preprocess(line)
    try:
    	airline_id = int(flight[1])
    	flight_distance = float(flight[10])
    except ValueError:
    	continue
    print('%s\t%s' % (airline_id, flight_distance))
