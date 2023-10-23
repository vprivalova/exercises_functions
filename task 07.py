def multiple(a, b, n):
    result = []
    for nmbr in range(1, n + 1):
        if nmbr % a == 0 and nmbr % b == 0:
            result.append(nmbr)
    result.sort()

    for elem in result:
        print(elem, end=' ')

