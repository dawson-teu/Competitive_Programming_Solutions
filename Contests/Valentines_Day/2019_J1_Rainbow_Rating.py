def category(r):
    if r < 1000:
        print("Newbie")
    elif r < 1200:
        print("Amateur")
    elif r < 1500:
        print("Expert")
    elif r < 1800:
        print("Candidate Master")
    elif r < 2200:
        print("Master")
    elif r < 3000:
        print("Grandmaster")
    elif r < 4000:
        print("Target")
    else:
        print("Rainbow Master")


n = int(input())
ratings = [int(input()) for i in range(n)]

for rating in ratings:
    category(rating)
