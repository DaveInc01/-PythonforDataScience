from numpy import array
import matplotlib.pyplot as plt


def ft_invert(array) -> array:
    '''Inverts the color of the image received.'''
    lenx, leny, lenz = array.shape
    for x in range(lenx):
        for y in range(leny):
            array[x][y] = [255 - val for val in array[x][y]]
    print(print(f"The shape of image is: {array.shape}"))
    print(array)
    plt.imshow(array)
    plt.show()
    return array


def ft_red(array) -> array:
    '''Red filter apply to the image received.'''
    lenx, leny, lenz = array.shape
    for x in range(lenx):
        for y in range(leny):
            r, g, b = array[x][y]
            new_g = int(g * 0.1)
            new_b = int(b * 0.1)
            array[x, y] = [r, new_g, new_b]
    print(print(f"The shape of image is: {array.shape}"))
    print(array)
    plt.imshow(array)
    plt.show()
    return array


def ft_green(array) -> array:
    '''Green filter apply to the image received.'''
    lenx, leny, lenz = array.shape
    for x in range(lenx):
        for y in range(leny):
            r, g, b = array[x][y]
            array[x, y] = [r - r, g, b - b]
    print(print(f"The shape of image is: {array.shape}"))
    print(array)
    plt.imshow(array)
    plt.show()
    return array


def ft_blue(array) -> array:
    '''Blue filter apply to the image received.'''
    lenx, leny, lenz = array.shape
    for x in range(lenx):
        for y in range(leny):
            r, g, b = array[x][y]
            array[x, y] = [0, 0, b]
    print(print(f"The shape of image is: {array.shape}"))
    print(array)
    plt.imshow(array)
    plt.show()
    return array


def ft_grey(array) -> array:
    '''Grey filter apply to the image received.'''
    lenx, leny, lenz = array.shape
    for x in range(lenx):
        for y in range(leny):
            r, g, b = array[x][y]
            array[x, y] = [g, g, g]
    print(print(f"The shape of image is: {array.shape}"))
    print(array)
    plt.imshow(array)
    plt.show()
    return array
