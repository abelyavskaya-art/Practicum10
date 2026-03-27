def fibonacci(n: int) -> list:
    """
    Generates a sequence of Fibonacci numbers.

    :param n: number of items
    :return: list of Fibonacci numbers
    """
    if n <= 0:
        return []
    elif n == 1:
        return [1]

    sequence = [1, 1]
    for i in range(2, n):
        sequence.append(sequence[i - 1] + sequence[i - 2])
    return sequence

num = int(input())
print(' '.join(map(str, fibonacci(num))))
