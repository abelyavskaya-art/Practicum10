def print_common_multiples(A: int, B: int, N: int) -> None:
    """
    Returns all common multiples of A and B that do not exceed N.

    :param A: first number
    :type A: int
    :param B: Second number
    :type B: int
    :param N: Top lookup
    :type N: int
    :return: function returns nothing, result is displayed
    :rtype: None
        """
    for num in range(max(A, B), N + 1):
        if num % A == 0 and num % B == 0:
            print(num)

A, B, N = int(input()), int(input()), int(input())

print_common_multiples(A, B, N)
