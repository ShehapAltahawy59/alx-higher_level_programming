#!/usr/bin/python3
def common_elements(set_1, set_2):
    set_3 = set_1.intersection(set_2)
    return set(x for x in set_1.union(set_2) if x not in set_3)
