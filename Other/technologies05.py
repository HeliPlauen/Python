
# Testing documentation!!!!

def summary(a, b):

    """
    >>> [summary(x, x) for x in range(10)]
    [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
    >>> [summary(x, x) for x in range(10)]
    [0, 2, 4, 6, 8, 1111, 12, 14, 16, 18]
    >>> summary(10, 20)
    30
    >>> summary(10, 20)
    31
    >>> summary(1)
    Typerror: summary()  missing 1 required positional argument: "b" 
    """

    return a + b


if __name__ == "__main__":
    import doctest
    doctest.testmod()