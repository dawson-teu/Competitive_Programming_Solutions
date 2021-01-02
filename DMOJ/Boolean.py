line = input().split(" ")
count = len(line) - 1
if count % 2 == 0:
    print(line[-1])
elif line[-1] == 'True':
    print('False')
else:
    print('True')
