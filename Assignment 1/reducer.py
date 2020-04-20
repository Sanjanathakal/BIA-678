#!/usr/bin/env python3

import sys

last_word = None
curr_counter = highest_occurred = 0
lowest_occurred = float("inf")
switch = False
max_seen = min_seen = set()

for curr in sys.stdin:
    bigram, count = curr.split("\t")

    if (switch and last_word and bigram != last_word):
        print("%s\t%d" % (last_word, curr_counter))
        switch = False

    if(bigram==last_word):
        curr_counter += int(count)
    elif(not last_word):
        last_word = bigram
        curr_counter = 1
    else:
        if (curr_counter > highest_occurred):
            max_seen = {last_word}
            highest_occurred = curr_counter
        elif (curr_counter == highest_occurred):
            max_seen.add(last_word)

        if(curr_counter<lowest_occurred):
            min_seen = {last_word}
            lowest_occurred = curr_counter
        elif(curr_counter == lowest_occurred):
            min_seen.add(last_word)

        last_word = bigram
        curr_counter = 1
        switch = True

print("Minimum occurred Bigrams: ",min_seen,"\nMaximum Occurred Bigrams: ",max_seen)
