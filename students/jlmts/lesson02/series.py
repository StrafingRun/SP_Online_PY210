#!/usr/bin/env python3

"""
exercise 2.4: fibonacci series
joli umetsu
python210
"""

def fibonacci(n):
    """ compute the nth Fibonacci number """
    # define zeroth default value in Fibonacci sequence (F0 = 0)
    if n == 0:
        return 0
    # define first default value in Fibonacci sequence (F1 = 1)
    elif n == 1:
        return 1
    # Fn = F(n-1) + F(n-2)
    else:
        return fibonacci(n-1) + fibonacci(n-2)
        

def lucas(n):
    """ compute the nth Lucas number """
    # define zeroth default value in Lucas sequence (L0 = 2)
    if n == 0:
        return 2
    # define first default value in Lucas sequence (L1 = 1)
    elif n == 1:
        return 1
    # Ln = L(n-1) + L(n-2)
    else:
        return lucas(n-1) + lucas(n-2)


def sum_series(n, n0=0, n1=1):
    """
    compute the nth value of a summation series.

    :param n0=0: value of zeroth element in the series
    :param n1=1: value of first element in the series

    This function should generalize the fibonacci() and the lucas(),
    so that this function works for any first two numbers for a sum series.
    Once generalized that way, sum_series(n, 0, 1) should be equivalent to fibonacci(n).
    And sum_series(n, 2, 1) should be equivalent to lucas(n).

    sum_series(n, 3, 2) should generate antoehr series with no specific name
    """
    if n == 0:
        return n0
    elif n == 1:
        return n1
    else:
        return sum_series(n-1,n0,n1) + sum_series(n-2,n0,n1)
    
    
if __name__ == "__main__":
    # run some tests
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    assert fibonacci(2) == 1
    assert fibonacci(3) == 2
    assert fibonacci(4) == 3
    assert fibonacci(5) == 5
    assert fibonacci(6) == 8
    assert fibonacci(7) == 13

    assert lucas(0) == 2
    assert lucas(1) == 1
    assert lucas(4) == 7

    # test that sum_series matches fibonacci
    assert sum_series(5) == fibonacci(5)
    assert sum_series(7, 0, 1) == fibonacci(7)

    # test if sum_series matched lucas
    assert sum_series(5, 2, 1) == lucas(5)

    # test if sum_series works for arbitrary initial values
    assert sum_series(0, 3, 2) == 3
    assert sum_series(1, 3, 2) == 2
    assert sum_series(2, 3, 2) == 5
    assert sum_series(3, 3, 2) == 7
    assert sum_series(4, 3, 2) == 12
    assert sum_series(5, 3, 2) == 19

    print("tests passed")