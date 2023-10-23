def letter_counter(line):
    vowels = 'ёуеыаоэяию'
    consonants = 'йцкнгшщзхъфвпрлджчсмтьб'

    vowels_cnt = 0
    consonants_cnt = 0

    for letter in line:
        if letter.lower() in vowels:
            vowels_cnt = vowels_cnt + 1

        elif letter.lower() in consonants:
            consonants_cnt = consonants_cnt + 1

    print('Гласных: ', vowels_cnt, 'Согласных: ', consonants_cnt)


statement = input()
letter_counter(statement)
