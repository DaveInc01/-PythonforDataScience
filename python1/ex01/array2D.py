import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    ''' takes as parameters a 2D array,
    prints its shape, and returns a
    truncated version of the array based
    on the provided start and end arguments'''
    try:
        np_family = np.array(family)
    except Exception as error:
        print(error)
        return
    rowlen, columnlen = np_family.shape
    print(f"My shape is : ({rowlen}, {columnlen})")
    np_family = np_family[start:end, :]
    rowlen, columnlen = np_family.shape
    print(f"My new shape is : ({rowlen}, {columnlen})")
    return np_family
