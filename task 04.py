def make_payment(p):
    if (p >= 20) and (p <= 1000):
        print('Успех')
    else:
        print('Повторить попытку')


payment = int(input())
make_payment(payment)
