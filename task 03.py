def purchase(price, card, special_day):
    discount = 0

    if price > 30000:
        discount = 0.1
    elif price > 20000:
        discount = 0.07
    elif price > 15000:
        discount = 0.05
    elif price > 5000:
        discount = 0.03

    if card is True:
        discount = discount + 0.05

    if special_day is True:
        discount = discount + 0.05

    if discount > 0.15:
        discount = 0.15

    total_cost = round((price * (1 - discount)), 2)
    return total_cost


print(purchase(8792929.22, True, False))
