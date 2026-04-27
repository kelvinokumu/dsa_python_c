import random


def max_min (numbers):
    min=numbers[0]
    for num in numbers:
        if num < min:
            # if num > min:
            min=num
    print("Min:", min)
    return min  

def getValues():
  list = random.sample(range(50,100), 10)
#   list = [10, 20, 5, 15, 25, 30, 2, 8, 12, 18]
  print(list)
  list_a = list[:5]
  print("List A:", list_a)
  
#   result = max_min(list)
#   print("Result:", result)
  
getValues()
