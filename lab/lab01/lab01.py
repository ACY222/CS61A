def digit(n, k):
    """Return the digit that is k from the right of n for positive integers n and k.
    >>> digit(3579, 2)
    5
    >>> digit(3579, 0)
    9
    >>> digit(3579, 10)
    0
    """
    # better methods
    return n // pow(10m k) % 10

    # my methods
    index, num = 0, 0
    while index <= k:
        n, num = n // 10, n % 10
        index += 1
    return num


def middle(a, b, c):
    """Return the number among a, b, and c that is not the smallest or largest.
    Assume a, b, and c are all different numbers.

    >>> middle(3, 5, 4)
    4
    >>> middle(30, 5, 4)
    5
    >>> middle(3, 5, 40)
    5
    >>> middle(3, 5, 40)
    5
    >>> middle(30, 5, 40)
    30
    """
    # better methods
    return a + b + c - min(a, b, c) - max(a, b, c)
    # my methods
    seq = [a, b, c]
    for x in seq:
        if x != min(seq) and x != max(seq):
            return x


def falling(n, k):
    """Compute the falling factorial of n to depth k.

    >>> falling(6, 3)  # 6 * 5 * 4
    120
    >>> falling(4, 3)  # 4 * 3 * 2
    24
    >>> falling(4, 1)  # 4
    4
    >>> falling(4, 0)
    1
    """
    "*** YOUR CODE HERE ***"
    # better methods
    total, stop = 1, n-k
    while n > stop:
        total, n = total * n, n - 1
    return total
    # my methods
    res, size = 1, 0
    while size < k:
        res, n, size = res * n, n - 1, size + 1
    return res


def divisible_by_k(n, k):
    """
    >>> a = divisible_by_k(10, 2)  # 2, 4, 6, 8, and 10 are divisible by 2
    2
    4
    6
    8
    10
    >>> a
    5
    >>> b = divisible_by_k(3, 1)  # 1, 2, and 3 are divisible by 1
    1
    2
    3
    >>> b
    3
    >>> c = divisible_by_k(6, 7)  # There are no integers up to 6 divisible by 7
    >>> c
    0
    """
    "*** YOUR CODE HERE ***"
    count = 0
    for factor in range(1, n + 1):
        if factor % k == 0:
            print(factor)
            count += 1
    return count



def sum_digits(y):
    """Sum all the digits of y.

    >>> sum_digits(10) # 1 + 0 = 1
    1
    >>> sum_digits(4224) # 4 + 2 + 2 + 4 = 12
    12
    >>> sum_digits(1234567890)
    45
    >>> a = sum_digits(123) # make sure that you are using return rather than print
    >>> a
    6
    """
    "*** YOUR CODE HERE ***"
    # another method
    total = 0
    while y > 0:
        total, y = total + y % 10, y // 10
    return total
    # my method
    if y < 10:
        return y
    else:
        return sum_digits(y // 10) + y % 10


def double_eights(n):
    """Return true if n has two eights in a row.
    >>> double_eights(8)
    False
    >>> double_eights(88)
    True
    >>> double_eights(2882)
    True
    >>> double_eights(880088)
    True
    >>> double_eights(12345)
    False
    >>> double_eights(80808080)
    False
    """
    "*** YOUR CODE HERE ***"
    # my method is better!
    if '88' in str(n):
        return True
    else:
        return False
    # another method
    prev_eight = False
    while n > 0:
        last_digit = n % 10
        if last_digit == 8 and prev_eight:
            return True
        elif last_digit == 8:
            prev_eight = True
        else:
            prev_eight = False
        n = n // 10
    return False
