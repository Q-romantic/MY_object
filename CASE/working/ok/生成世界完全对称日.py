import datetime


def get_date_list(start, end):
    date_list = []
    date = datetime.datetime.strptime(start, '%Y-%m-%d')
    end = datetime.datetime.strptime(end, '%Y-%m-%d')
    while date <= end:
        date_list.append(date.strftime('%Y-%m-%d'))
        date = date + datetime.timedelta(days=1)
    return date_list


def main():
    x = 0
    # for i in get_date_list('0001-01-01', '0001-01-10'):
    for date in get_date_list('0001-01-01', '9999-12-30'):
        # print(i)
        str_date = str(int(date.replace('-', '')))
        if str_date == str_date[::-1]:
            x += 1
            print(str_date, end='\t')
            if x % 15 == 0:
                print()
    print('\n共有：%s个' % x)


main()
