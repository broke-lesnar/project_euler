"""
The sum of the squares of the first ten natural numbers is 385.
The square of the sum of the first ten natural numbers is 3025.
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025-385 = 2640
Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""


def find_difference(n: int) -> int:
    return ((n * (n + 1)) // 2)**2 - (n * (n + 1) * (2 * n + 1)) // 6


if __name__ == '__main__':
    print(find_difference(10))
    print(find_difference(100))
