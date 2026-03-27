def message_length(message: str) -> str:
    """
    Checks the length of a message and returns the entire message or its first 160 characters.

    :param str message: text of the post
    :return: str - entire message or first 160 characters
    """
    if len(message) <= 160:
        return message
    else:
        return message[:160]

mes = input()
print(message_length(mes))

