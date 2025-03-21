

def ft_filter(func, list: list)-> list:
    '''filter(function or None, iterable) --> filter object
    Return an iterator yielding those items of iterable for which function(item)
    is true. If function is None, return the items that are true'''
    
    newlist = [x for x in list if func(x)]
    return newlist
