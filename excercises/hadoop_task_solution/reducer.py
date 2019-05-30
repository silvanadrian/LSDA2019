#!/usr/bin/env python3
import sys

total_count = 0
old_word = None

# Input from stdin (handled via Hadoop Streaming)
for line in sys.stdin:

    # Remove whitespace and split up lines
    line = line.strip()
    line = line.split('\t')
    if len(line) != 2:
        continue

    # Get word and count
    word, count = line

    try:
        count = int(count)
    except ValueError:
        continue

    # This if-statement only works because Hadoop sorts 
    # the output of the mapping phase by key (here, by 
    # word) before it is passed to the reducers. Each 
    # reducer gets all the values for a given key. Each 
    # reducer might get the values for MULTIPLE keys.
    if (old_word is not None) and (old_word != word):
        print('%s\t%s' % (old_word, total_count))
        total_count = 0        

    old_word = word
    total_count += count

# We have to output the word count for the last word!
if old_word is not None:
    print('%s\t%s' % (old_word, total_count))
