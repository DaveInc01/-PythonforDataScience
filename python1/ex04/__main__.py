import sys
from load_image import ft_load
from zoom import ft_zoom


def main():
    '''loads an image'''
    if len(sys.argv) != 2:
        print("Usage exception: __main__.py path/to/image")
        return
    img = ft_load(sys.argv[1])
    if not img:
        return
    try:
        ft_zoom(img, 400, 400)
    except Exception as err:
        print(f"zoom Exception: {err}")
        return


if __name__ == '__main__':
    main()
