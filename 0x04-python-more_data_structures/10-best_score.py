#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    best_value = flot('-inf')
    for key, value in a_dictionary.items():
        if value > best_value:
            best_value == value
    return best_value
