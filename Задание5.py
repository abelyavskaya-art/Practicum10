def calculate_card_value() -> int | None:
    """
    Calculates the total value of the gift card, taking into account the bonus.

    Asks the user for card value and adds bonus points
    Depending on the amount selected.

    :return: total card amount (nominal + bonus) or None if entered incorrectly
    :rtype: int or None
    """

    amount = int(input())

    if amount == 5 or amount == 10:
        total = amount
    elif amount == 25:
        total = amount + 3
    elif amount == 50:
        total = amount + 8
    elif amount == 100:
        total = amount + 20
    else:
        print("")
        return None

    print(f"The final amount of the card : {total}")
    return total
