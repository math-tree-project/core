def increment_function(i):

    """
    >>> increment_function(3)
    4
    """
    return i+1

if __name__ == '__main__':
    print("THIS WILL NOT BE PRINTED WHEN THIS MODULE IS IMPORTED")

    import doctest
    doctest.testmod(verbose=True)