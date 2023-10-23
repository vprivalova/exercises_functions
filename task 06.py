def message(line):
    if len(line) < 160:
        return line
    else:
        return line[:162]


text = input()
print(message(text))
