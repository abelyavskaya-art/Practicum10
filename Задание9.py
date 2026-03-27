def seconds_since_new_year(datetime_str: str) -> int:
    """
    Calculates the number of seconds since 01/01/YYYY 00:00:00.

    :param str datetime_str: string in format MM/DD/YYYY HR:MIN:SEC
    :return: int - number of seconds
    """
    try:
        date_part, time_part = datetime_str.strip().split()
        month, day, year = map(int, date_part.split('/'))
        hour, minute, second = map(int, time_part.split(':'))

        days_in_month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        if not (1 <= month <= 12 and 1 <= day <= days_in_month[month - 1]):
            raise ValueError("Некорректная дата")
        if not (0 <= hour <= 23 and 0 <= minute <= 59 and 0 <= second <= 59):
            raise ValueError("Некорректное время")

        # Количество дней от начала года
        days = sum(days_in_month[:month - 1]) + day - 1

        return days * 86400 + hour * 3600 + minute * 60 + second

    except (ValueError, IndexError):
        print("Ошибка: неверный формат. Ожидается: MM/DD/YYYY HR:MIN:SEC")
        return -1

print(seconds_since_new_year("09/06/2024 00:00:00"))
