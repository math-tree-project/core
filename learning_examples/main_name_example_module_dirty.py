def decrement_function(i):
    """

    >>> decrement_function(3)
    2
    """
    return i - 1


print("THIS WILL BE PRINTED WHEN THIS MODULE IS IMPORTED")
import doctest
doctest.testmod(verbose=True)