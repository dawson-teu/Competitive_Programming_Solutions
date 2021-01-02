filename = input().split(".")
if len(filename) > 1:
    ext = filename[1].lower()
else:
    ext = input().lower()
print("\"" + filename[0] + "\"" + " - " + ext)
