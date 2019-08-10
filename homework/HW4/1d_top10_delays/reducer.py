#!/usr/bin/env python3
import math
import sys



dict = dict()
key = None
results = []
print('ID\tDelays')
for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) != 2:
        continue

    airline_id = int(data[0])
    delay = float(data[1])
    if key is None:
        key = airline_id
    if airline_id != key:
        list.sort(results, reverse=True)
        print('%s\t%s' % (key, results[:10]))
        dict[key] = results
        results = []
        key = airline_id


    results.append(delay)


if key is not None:
    list.sort(results, reverse=True)
    print('%s\t%s' % (airline_id, results[:10]))
