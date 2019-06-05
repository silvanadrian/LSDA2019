#!/usr/bin/env python3
import sys

shortest_distance = sys.maxsize
old_air_id = None

print('ID\tShortest Distance')
for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) != 2:
        continue

    airline_id, distance = data
    try :
        airline_id = int(airline_id)
        distance = float(distance)
    except ValueError:
        continue

    if (old_air_id is not None) and (old_air_id != airline_id):
        print('%s\t%s' % (old_air_id, shortest_distance))
        shortest_distance = sys.maxsize
        old_air_id = None

    old_air_id = airline_id
    if (distance < shortest_distance):
        shortest_distance = distance

if old_air_id is not None:
    print('%s\t%s' % (old_air_id, shortest_distance))
