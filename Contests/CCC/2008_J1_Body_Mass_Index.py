w = float(input())
h = float(input())

val = w / (h ** 2)
if val < 18.5:
    print("Underweight")
elif val <= 25.0:
    print("Normal weight")
else:
    print("Overweight")
