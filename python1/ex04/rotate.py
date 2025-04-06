

def ft_rotate(arr: list) -> list:
    '''rotate array counterclockwise direction'''
    arr = arr.reshape(400, 400)
    rotated = arr.copy()
    x, y = arr.shape
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            rotated[i][j] = arr[j][x - i - 1]
    return rotated
