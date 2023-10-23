def prime_number(number):
    counter = 0

    for divider in range(2, number):
        if number % divider == 0:
            counter = counter + 1

    if counter == 0:
        return True
    else:
        return False


n = int(input())
result = []

if n == 0:
    print('')
elif n == 1:
    print('')
else:
    for nums in range(2, n + 1):
        if prime_number(nums) is True:
            result.append(nums)

    for element in result:
        print(element, end=' ')
