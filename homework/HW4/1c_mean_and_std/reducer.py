#!/usr/bin/env python3
import math
import sys

def add(array, x):
    array[0] += 1

    # self.new_m = self.old_m + (x - self.old_m) / self.n
    array[2] = array[1] + (x - array[1]) / array[0]
    array[4] = array[3] + (x - array[1]) * (x - array[2])

    array[1] = array[2]
    array[3] = array[4]
    return array

def mean(array):
    return array[2] if array[0] else 0.0

def variance(array):
    return array[4] / (array[0] - 1) if array[0] > 1 else 0.0

def std(array):
    return math.sqrt(variance(array))

dict = dict()
for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) != 2:
        # Something has gone wrong. Skip this line.
        continue

    airline_id = int(data[0])
    delay = float(data[1])
    if airline_id not in dict.keys():
        # n / old_m / new_m / old_s / new_s
        dict[airline_id] = [1,delay,delay,0,0]
    else:
        dict[airline_id] = add(dict[airline_id],delay)

print('ID\tMean\tStandard Deviation')
for airline_id, flight_distance in dict.items():
    print('%s\t%s\t%s' % (airline_id, mean(flight_distance),std(flight_distance)))
