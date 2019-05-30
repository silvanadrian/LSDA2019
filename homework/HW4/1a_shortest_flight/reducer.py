#!/usr/bin/env python3
import sys

dict = dict()
for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) != 2:
        # Something has gone wrong. Skip this line.
        continue

    airline_id, distance = data
    if airline_id not in dict.keys():
        dict[airline_id] = float(distance)
    if dict[airline_id] > float(distance):
        dict[airline_id] = float(distance)


for airline_id, flight_distance in dict.items():
    print('%s\t%s' % (airline_id, flight_distance))
