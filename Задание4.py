def make_payment(P: int) -> None:
    """
    Process the credit card payment.

    :param P: Payment amount
    :type P: int
    :return: function returns nothing, results on screen
    :rtype: None
    """

    credit_limit = 1000
    min_payment = 20

    if min_payment <= P <= credit_limit:
        print("Успех")
    else:
        print("Повторить попытку")

payment = int(input("Введите сумму платежа: "))
make_payment(payment)
