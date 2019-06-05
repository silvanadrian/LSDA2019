#!/usr/bin/env python3
import sys

total_flights = 0
delayed_flights = 0
old_air_id = None
print('ID\tTotal\tDelayed\tPercentage')
for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) != 2:
        continue

    airline_id, arr_delay = data

    try:
        airline_id = int(airline_id)
        arr_delay = int(arr_delay)
    except ValueError:
        continue
    

    if (old_air_id is not None) and (old_air_id != airline_id):
        percentage = delayed_flights/total_flights*100
        print('%s\t%s\t%s\t%s' % (old_air_id,total_flights,delayed_flights,percentage))
        old_air_id = None
        delayed_flights = 0
        total_flights = 0

    old_air_id = airline_id
    delayed_flights += arr_delay
    total_flights += 1



if old_air_id is not None:
    percentage = delayed_flights/total_flights*100
    print('%s\t%s\t%s\t%s' % (airline_id,total_flights,delayed_flights,percentage))
