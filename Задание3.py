def calculate_final_price(amount: int, discount_card: bool, holidays: bool) -> float:
    """
    Calculates the total price based on accrued discounts.

    :param amount: int
    :param discount_card: bool
    :param holidays: bool
    :return: float
    """

    discount = 0

    if amount > 30000:
        discount += 10
    elif amount > 20000:
        discount += 7
    elif amount > 15000:
        discount += 5
    elif amount > 5000:
        discount += 3

    if discount_card:
        discount += 5

    if holidays:
        discount += 3

    discount = min(discount, 15)

    final_price = amount * (1 - discount / 100)
    return round(final_price, 2)

print(calculate_final_price(98877655, True, True))
