#!/usr/bin/env python3
import math
import sys



dict = dict()
key = None
results = []
for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) != 2:
        # Something has gone wrong. Skip this line.
        continue

    airline_id = int(data[0])
    delay = float(data[1])
    #if airline_id not in dict.keys():
    #    dict[airline_id] = [delay]
    #if airline_id == key:
    #    dict[airline_id].append(delay)
    if key is None:
        key = airline_id
    if airline_id != key:
        list.sort(results)
        dict[key] = results
        results = []
        key = airline_id

    results.append(delay)

dict[key] = results
print('ID\tMean\tStandard Deviation')
for airline_id, flight_distance in dict.items():
    print('%s\t%s' % (airline_id, flight_distance[:10]))
