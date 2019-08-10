#!/usr/bin/env python3
import math
import sys

def add(array, x):
    array[0] += 1

    # new_m = old_m + (x - old_m) / n
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

calculations = [1,0.0,0.0,0,0]
old_air_id = None
print('ID\tMean\tStandard Deviation')
for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) != 2:
        continue

    airline_id, arr_delay = data
    try:
        airline_id = int(airline_id)
        arr_delay = float(arr_delay)
    except ValueError:
        continue

    if (old_air_id is not None) and (old_air_id != airline_id):
        print('%s\t%s\t%s' % (old_air_id,mean(calculations),std(calculations)))
        calculations = [1,arr_delay,arr_delay,0,0]
        old_air_id = None
    
    old_air_id = airline_id
    calculations = add(calculations,arr_delay)

if old_air_id is not None:
    print('%s\t%s\t%s' % (airline_id,mean(calculations),std(calculations)))