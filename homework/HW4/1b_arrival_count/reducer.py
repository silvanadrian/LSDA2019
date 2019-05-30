#!/usr/bin/env python3
import sys

dict = dict()
for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) != 2:
        continue

    airline_id, delay = data
    if airline_id not in dict.keys():
        # total / delayed
        dict[airline_id] = [1, 0]
        if float(delay) > 0:
            dict[airline_id][1] += 1
    else:
        dict[airline_id][0] += 1
        if float(delay) > 0:
            dict[airline_id][1] += 1


print('ID\tTotal\tDelayed\tPercentage')
for airline_id, delays in dict.items():
    total = delays[0]
    delayed = delays[1]
    percentage = delayed/total*100
    print('%s\t%s\t%s\t%s' % (airline_id,total,delayed,percentage))
