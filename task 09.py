def sec_counting(moment):
    months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    date = moment.split(' ')[0]
    time = moment.split(' ')[1]

    dates = date.split('/')
    times = time.split(':')

    result = 0

    result = result + int(times[2]) + int(times[1])*60 + (int(times[0]) - 1)*60*60 + int(dates[1])*24*60*60

    for index in range(int(dates[0]) - 1):
        result = result + months[index]*24*60*60

    return result


print(sec_counting('04/30/2008 14:55:23'))
