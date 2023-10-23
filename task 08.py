def time_convertation(moment):
    try:
        date = moment.split(' ')[0]
        time = moment.split(' ')[1]

        date1 = date.split('/')

        if (len(date1[0]) == 2) and (int(date1[0]) <= 12) and (int(date1[0]) > 0):
            if len(date1[1]) == 2 and int(date1[1]) <= 31:
                if len(date1[2]) == 4:
                    new_date = date1[1] + '.' + date1[0] + '.' + date1[2][2:]

        time1 = time.split(':')

        if (len(time1[0]) == 2) and (int(time1[0]) <= 23):
            if (len(time1[1]) == 2) and (int(time1[1]) <= 59):
                if (len(time1[2]) == 2) and (int(time1[2]) <= 59):
                    if int(time1[0]) == 0:
                        hours = '12 AM'

                    elif (int(time1[0]) > 0) and (int(time1[0]) < 12):
                        hours = time1[0] + ' AM'

                    elif (int(time1[0]) > 11) and (int(time1[0]) < 24):
                        hours = str(int(time1[0]) - 12) + ' PM'
                    new_time = hours.split(' ')[0] + ':' + time1[1] + ':' + time1[2] + ' ' + hours.split(' ')[1]

        print(new_date + ' ' + new_time)

    except Exception:
        print('Неверно введены данные')


time_convertation('12/30/2008 14:55:23')
