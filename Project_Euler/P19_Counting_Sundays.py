total = 2  # January 1, 1901, is a Tuesday
count = 0
months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
for i in range(1901, 2001):
    if i % 4 == 0 and (not i % 100 == 0 or i % 400 == 0):
        months[1] = 29
    else:
        months[1] = 28
    for month in months:
        total = ((total % 7) + (month % 7)) % 7  # we keep a running count of the day and update it every month
        if total == 0:  # a value of 0 is equivalent, mod 7, to a Sunday
            count += 1
print(count)
