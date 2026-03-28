def common_num(n: int) -> bool:
    """
    Checks whether the number is simple.
    :param n: int
    :return: bool
    """
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

N = int(input("Введите число N: "))

for num in range(1, N + 1):
    if common_num(num):
        print(num, end=" ")
print()
