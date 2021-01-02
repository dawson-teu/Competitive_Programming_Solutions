from datetime import datetime, timedelta


def format_date(d):
    string = ""
    string += str(d.year)
    string += '/' + '{0:02d}'.format(int(d.month))
    string += '/' + '{0:02d}'.format(int(d.day))
    string += ' ' + '{0:02d}'.format(int(d.hour))
    string += ':' + '{0:02d}'.format(int(d.minute))
    string += ':' + '{0:02d}'.format(int(d.second))
    return string


s = int(input())

line = input()
date, time = line.split(" ")
year, month, day = [int(date.split("/")[i]) for i in range(3)]
hour, minute, second = [int(time.split(":")[i]) for i in range(3)]

final_date = datetime(year, month, day, hour, minute, second) - timedelta(seconds=(s * 60 * 60))
print(format_date(final_date))
