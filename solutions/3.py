"""
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143?
"""

from is_prime import is_prime


def find_factors(n):
    result = 0
    for i in range(2, n + 1):
        if n % i == 0 and is_prime(i):
            result = i
    return result


if __name__ == '__main__':
    # n = 59898
    n = 5989887
    # n = 59898878
    # n = 600851475143
    answer = find_factors(n)
    print(answer)
