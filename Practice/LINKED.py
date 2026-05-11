
import random


list = random.sample(range( 10), 5)
print(list)
print(f"Start at index 2: {list[2:]}")#stop at index 2
print(f"Start at index 3: {list[3:]}")#stop at index 3

list.append(5)
list.append(10)
list.append(15)
list.append(20)


list_a = list[1:]#get last index
print("List A:", list_a)