from datetime import datetime, timedelta

a = input()
a = [int(a.split(" ")[i]) for i in range(2)]
b = input()
b = [int(b.split(" ")[i]) for i in range(2)]
time = input()
year, month, day, hour, minute, second = [int(time.split(":")[i]) for i in range(6)]

date = datetime(year, month, day, hour, minute, second) + timedelta(seconds=abs(b[0] - a[0]) + abs(b[1] - a[1]))
string = ""
string += '{0:04d}'.format(date.year) + ":"
string += '{0:02d}'.format(date.month) + ":"
string += '{0:02d}'.format(date.day) + ":"
string += '{0:02d}'.format(date.hour) + ":"
string += '{0:02d}'.format(date.minute) + ":"
string += '{0:02d}'.format(date.second)
print(string)
