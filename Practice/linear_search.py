import random
import result


def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

def get_values():
    values = random.sample(range(1, 100), 10)  # Generate a list of 10 unique random integers between 1 and 99
    print("Generated array:", values)
    target = int(input("Enter the target element: "))

    result = linear_search(values, target)

    if result != -1:
        print(f"Element found at index: {result}")
    else:
        print("Element not found in the array.")

get_values()