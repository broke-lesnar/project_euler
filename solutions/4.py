"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""


def find_largest_palindrome(n):
    """
    n is the number of digits both numbers will have
    l and s largest and smallest n-digit numbers, respectively
    op is to count number of operations
    """
    l = int('9' * n)
    s = int('1' + '0' * (n-1))
    answer = []
    op = 0
    for i in range(l, s, -1):
        for j in range(l, s, -1):
            p = str(i * j)
            if p == p[::-1]:
                op += 1
                answer.append(int(p))
    return (op, max(answer))


if __name__ == '__main__':
    print(find_largest_palindrome(3))
    # print(find_largest_palindrome(2))
