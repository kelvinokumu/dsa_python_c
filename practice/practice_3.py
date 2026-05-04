import numbers
import random

def max_min(numbers):
    minimum = numbers[0]
    for num in  numbers:
        if num < minimum:
            minimum = num
        #print(f"Current min {minimum}")
        #print("Python3")

    return minimum


def getValues():
    list = random.sample(range(50, 100), 5)
    print(list)
    list_a = list[1]
    print(list_a)
    result = max_min(list)
    print(f"value is {result}")

getValues()
