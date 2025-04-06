import matplotlib.pyplot as plt
import numpy as np
from rotate import ft_rotate


def ft_zoom(img: any, newWidth: int, newHeight: int) -> list:
    '''crop image with newWidth and newHeight and
    show it in graysclae'''
    origWidth, orgiHeight = img.size
    startX = (origWidth - newWidth) / 2
    startY = (orgiHeight - newHeight) / 2
    area = (startX, startY, startX + newWidth, startY + newHeight)
    # crop_image = img.crop(area)

    crop_image = img.crop(area).resize((400,  400)).convert("L")
    crop_image = np.array(crop_image).reshape(400, 400, 1)
    print(f"The shape of image is: {crop_image.shape} \
            or ({crop_image.shape[0]}, {crop_image.shape[1]})")
    print(crop_image)
    try:
        rotated = ft_rotate(crop_image)
    except Exception as err:
        print(f"rotate exception: {err}")
        return
    print(f"New shape after Transpose: {rotated.shape}")
    print(rotated)
    plt.imshow(rotated, cmap='gray')
    plt.show()
    return rotated
