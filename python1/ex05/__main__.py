import numpy as np
import sys
from load_image import ft_load
import pimp_image as p


def main():
    '''loads an image'''
    if len(sys.argv) != 2:
        print("Usage exception: __main__.py path/to/image")
        return
    array = ft_load(sys.argv[1])
    if not array:
        return
    array = np.array(array)
    try:
        p.ft_invert(array)
        # p.ft_red(array)
        # p.ft_green(array)
        # p.ft_blue(array)
        # p.ft_grey(array)
    except Exception as err:
        print(f"Filter Exception: {err}")
        return


if __name__ == '__main__':
    main()
