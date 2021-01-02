num = input()
if (num[:3] == "800") or (num[:3] == "909") or (num[6] == num[9] and num[7] == num[8]) or (num[3] == num[4] and num[4]
                                                                                           == num[5]):
    print("yes")
else:
    print("no")
