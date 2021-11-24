#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list is not None:
        tot = 0
        freq = 0

        for tup in my_list:
            (weight, occurrence) = tup
            tot += (weight * occurrence)
            freq += occurrence
        return (tot/freq) if freq > 0 else 0
    else:
        return (0)
