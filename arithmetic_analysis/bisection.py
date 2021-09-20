from typing import Callable

# Wikipedia: https://en.wikipedia.org/wiki/Bisection_method

def bisection(function: Callable[[float], float], a: float, b: float, precision: float = 10 ** -7) -> float:
    """
    finds where function becomes 0 in [a,b] using bolzano
    >>> bisection(lambda x: x ** 3 - 1, -5, 5)
    1.0000000149011612
    >>> bisection(lambda x: x ** 3 - 1, 2, 1000)
    Traceback (most recent call last):
    ...
    ValueError: could not find root in given interval.
    >>> bisection(lambda x: x ** 2 - 4 * x + 3, 0, 2)
    1.0
    >>> bisection(lambda x: x ** 2 - 4 * x + 3, 2, 4)
    3.0
    >>> bisection(lambda x: x ** 2 - 4 * x + 3, 4, 1000)
    Traceback (most recent call last):
    ...
    ValueError: could not find root in given interval.
    """
    start: float = a
    end: float = b
    # check if a or b is a root for the function
    if function(a) == 0:  
        return a
    elif function(b) == 0:
        return b
    elif (function(a) * function(b) > 0):  
        # if none of these are roots and they are both positive or negative,
        # then this algorithm can't find the root
        raise ValueError("could not find root in given interval.")
    else:
        mid: float = start + (end - start) / 2.0
        while abs(start - mid) > precision:  # until precision is enough
            if function(mid) == 0:
                return mid
            elif function(mid) * function(start) < 0:
                end = mid
            else:
                start = mid
            mid = start + (end - start) / 2.0
        return mid


def f(x: float) -> float:
    return x ** 3 - 2 * x - 5


if __name__ == "__main__":
    print(bisection(f, 1, 1000))

    import doctest

    doctest.testmod()
