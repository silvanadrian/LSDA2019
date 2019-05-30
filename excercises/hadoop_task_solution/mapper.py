#!/usr/bin/env python3
import sys

punctuations = '''
_)(.;,!?"“”‘’[]:-—/
'''

def preprocess(word):

    word = word.strip().lower()

    if word.startswith("http://"):
        return ""

    word_new = ""
    for char in word:
        if char not in punctuations:
            word_new = word_new + char

    return word_new

def extract_html(word):

    word = word.strip().lower()

    if not word.startswith("http://"):
        return ""

    return word

# Where do these lines come from?
# This is done by Hadoop Streaming ...
for line in sys.stdin:

    # Remove whitespace and split up line
    # into words (whitespace as delimiter)
    line = line.strip()
    words = line.split()

    for word in words:

        word = preprocess(word)
        #word = extract_html(word)

        # The output is written to 'stdout' and will
        # be used as input by the reducers. Hadoop
        # Streaming will split up the work and will
        # feed these new lines to the reducers!
        if len(word) > 0:
            print('%s\t%s' % (word, 1))
