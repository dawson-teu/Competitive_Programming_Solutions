start = int(input())
interval = int(input())
message = int(input())
time = start
checked = False
for i in range(3):
    time += interval
    if time >= message:
        print(time)
        checked = True
        break
if not checked:
    print("Who knows...")
