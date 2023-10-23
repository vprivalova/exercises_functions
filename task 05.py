def phone_card():
    cost = int(input())

    if cost == 5 or cost == 10:
        total_cost = cost
    elif cost == 25:
        total_cost = cost + 3
    elif cost == 50:
        total_cost = cost + 8
    elif cost == 10:
        total_cost = cost + 20
    else:
        total_cost = 'Некорректная стоимость карты'

    return total_cost


print(phone_card())
