import sys
import math

low = 1
high = 2000000000
for i in range(31):
    guess = math.floor((low + high) / 2)
    print(guess)

    sys.stdout.flush()

    response = input()
    if response == 'FLOATS':
        high = guess - 1
    elif response == 'SINKS':
        low = guess + 1
    elif response == 'OK':
        break
