from PIL import Image
import numpy as np


def ft_load(path: str) -> list:
    '''function loads an image,
    prints its format, and its pixels
    content in RGB format'''
    try:
        img = Image.open(path)
    except Exception:
        print("The file can't be opened")
        return
    if img.format.upper() != "JPG" and img.format.upper() != "JPEG":
        print("Only JPG or JPEG formats")
        return
    print(f"The shape of image is: {np.array(img).shape}")
    return img
