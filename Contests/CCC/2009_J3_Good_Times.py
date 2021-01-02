from datetime import datetime, timedelta


def convert_time(val):
    d = datetime(year=2, month=1, day=1, hour=int(ottawa_time[:2]), minute=int(ottawa_time[2:]))
    convert = d + timedelta(hours=val)
    if convert.hour == 0:
        return '{0:02d}'.format(convert.minute)
    else:
        return str(convert.hour) + '{0:02d}'.format(convert.minute)


ottawa_time = '{0:04d}'.format(int(input()))

print(convert_time(0) + ' in Ottawa')
print(convert_time(-3) + ' in Victoria')
print(convert_time(-2) + ' in Edmonton')
print(convert_time(-1) + ' in Winnipeg')
print(convert_time(0) + ' in Toronto')
print(convert_time(1) + ' in Halifax')
print(convert_time(1.5) + ' in St. John\'s')
