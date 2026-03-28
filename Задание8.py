def convert_datetime(datetime_str: str) -> None:
    """
    Convert date and time from MM/DD/YYYY HR:MIN:SEC
    in DD.MM.YY HR:MIN:SEC (12-hour format with AM/PM)

    :param str datetime_str: Date and time string
    :return: None - function returns result or error message
    """
    try:
        date_part, time_part = datetime_str.strip().split()
        month, day, year = map(int, date_part.split('/'))
        hour, minute, second = map(int, time_part.split(':'))

        if not (1 <= month <= 12):
            print("Ошибка: месяц должен быть от 1 до 12")
            return

        days_in_month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if not (1 <= day <= days_in_month[month - 1]):
            print("Ошибка: неверное количество дней в месяце")
            return

        if year < 0 or year > 9999:
            print("Ошибка: неверное значение года")
            return

        if not (0 <= hour <= 23 and 0 <= minute <= 59 and 0 <= second <= 59):
            print("Ошибка: неверное значение времени")
            return

        # Преобразование в 12-часовой формат
        if hour == 0:
            hour_new, period = 12, "AM"
        elif hour < 12:
            hour_new, period = hour, "AM"
        elif hour == 12:
            hour_new, period = 12, "PM"
        else:
            hour_new, period = hour - 12, "PM"

        year_short = year % 100

        print(
            f"{day:02d}.{month:02d}.{year_short:02d} "
            f"{hour_new:02d}:{minute:02d}:{second:02d} {period}"
        )

    except ValueError:
        print("Ошибка: неверный формат.")
