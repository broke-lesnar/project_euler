from functools import lru_cache
from math import sqrt, ceil


@lru_cache(maxsize=None)
def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    for i in range(2, ceil(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


if __name__ == '__main__':
    print(is_prime(61))
    print(is_prime(5))
    print(is_prime(2303804))
    print(is_prime(600851475143))
    print(is_prime(6857))
