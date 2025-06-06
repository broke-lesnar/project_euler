limit = 4_000_000


def fibonacci(n_terms):
    last = 1
    next = 2

    for _ in range(n_terms - 2):
        last, next = next, last + next
        if next <= limit:
            yield next
        else:
            break


if __name__ == '__main__':
    nth_term = 35
    answer = list(fibonacci(nth_term))

    # because our dumbass list doesn't have 1, 2 in it.
    # lol idek how to fix it. but hey, it works!!!
    sum = 2
    for n in answer:
        if n % 2 == 0:
            sum += n
    print(sum)
