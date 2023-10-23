def selecting_numbers(a, b):
    sign = '13489'
    if a > b:
        start = b
        end = a
    else:
        start = a
        end = b

    result = []
    counter = 0

    for number in range(start, end + 1):
        for nums in str(number):
            if nums in sign:
                counter = counter + 1
        if counter == len(str(number)):
            result.append(number)

        counter = 0

    result.sort()

    for element in result:
        print(element, end=' ')


selecting_numbers(105, 59)
