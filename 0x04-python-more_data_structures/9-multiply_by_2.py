#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    if a_dictionary is not None:
        b_dictionary = {}
        temp = {}
        for key, value in a_dictionary.items():
            new_val = value * 2
            temp = {key: new_val}
            b_dictionary.update(temp)
        return (b_dictionary)
    return None
