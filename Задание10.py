def print_special_numbers(A: int, B: int) -> None:
    """
    Prints in ascending order all numbers from A to B,
    which consist only of the digits 1, 3, 4, 8, 9.

    :param int A: left edge of range
    :param int B: right edge of range
    :return: None
    """

    if A > B:
        A, B = B, A

    allowed_digits = ['1', '3', '4', '8', '9']

    for num in range(A, B + 1):
        num_str = str(num)

        if all(digit in allowed_digits for digit in num_str):
            print(num)

print_special_numbers(100, 150)
