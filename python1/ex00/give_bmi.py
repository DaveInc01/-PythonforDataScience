def give_bmi(height: list[int | float],
             weight: list[int | float]) -> list[int | float]:
    ''', take 2 lists of integers or floats in input and
    returns a listof BMI values'''
    if len(weight) != len(height):
        print("list parameters should be equal")
        return
    try:
        is_list_numbers(height)
        is_list_numbers(weight)
    except TypeError as err:
        print(err)
        return
    newlist = [int | float]
    newlist = [m / pow(h, 2) for m, h in zip(weight, height)]
    return (newlist)


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    '''accepts a list of integers or floats and an integer
    representing a limit as parameters.
    Returns a list of booleans'''
    try:
        is_list_numbers(bmi)
    except TypeError as err:
        print(err)
        return
    newlist = [x > limit for x in bmi]
    return newlist


def is_list_numbers(mylist: list[int | float]):
    '''take list and check if there is only int or float elements'''
    for el in mylist:
        if type(el) is float or type(el) is int:
            continue
        else:
            raise TypeError("Only integers and floats are allowed")
