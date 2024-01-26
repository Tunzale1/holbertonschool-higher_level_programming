#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
num = abs(number) % 10
i = -1 * num
if number < 0:
    if num == 0:
        print(f"Last digit of {number} is {i} and is 0")
    elif num < 9:
        print(f"Last digit of {number} is {i} and is less than 6 and not 0")
else:
    if num > 5:
        print(f"Last digit of {number} is {num} and is greater than 5")
    elif num == 0:
        print(f"Last digit of {number} is {num} and is 0")
    elif num < 6:
        print(f"Last digit of {number} is {num} and is less than 6 and not 0")
