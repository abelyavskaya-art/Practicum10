def common_num(n: int) -> bool:
    """Проверяет, является ли число простым."""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

num = int(input())
print(common_num(num))
