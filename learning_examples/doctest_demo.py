"""

>>> one_function()
1

>>> two_function()
2

>>> not_function(True)
False

>>> not_function(False)
True

>>> multiply(5,5)
25

>>> multiply(6,6)
36

"""

import doctest


def one_function():
    """

    >>> one_function()
    1

    """
    return 1

def two_function():
    """

    >>> two_function()
    2
    """
    return 2

def not_function(boo):
    """

    This functions lies
    to you when given Truth,
    and gives you False
    when True supplied,
    the opposite of False
    is True however.

    >>> not_function(True)
    False

    >>> not_function(False)
    True

    """
    return not boo


def multiply(a,b):

    """

    >>> multiply(4,4)
    16
    """

    return a*b

doctest.testmod(verbose=True)

