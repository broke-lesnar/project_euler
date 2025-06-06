def sum_of_multiples(n):
    """
    Finds the sum of multiples of 3 or 5 below n.

    Example:
    n = 10 should return 23, since multiples we have are 3, 5, 6, 9 
    """

    s3 = 0
    s5 = 0
    for i in range(3, n):
        if i % 3 == 0:
            s3 += i
        elif i % 5 == 0:
            s5 += i
    return s3+s5


if __name__ == '__main__':
    print(sum_of_multiples(10))
