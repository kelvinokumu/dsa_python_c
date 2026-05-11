# Binary Search




# def binary_search(arr, target):
#     low, high = 0, len(arr) - 1

#     while low <= high:
#         mid = (low + high) // 2

#         if arr[mid] == target:
#             return mid
#         elif arr[mid] < target:
#             low = mid + 1
#         else:
#             high = mid - 1

#     return -1


# print(binary_search([1,2,3,4,5], 3))

"""Binary Recursive Search"""



def binary_search_recursive(values, target, low, high):
    if low > high:
        return -1
    mid = (low + high) // 2
    if values[mid] == target:
        return mid
    elif values[mid] > target:
        return binary_search_recursive(values, target, low, mid - 1)
    else:
        return binary_search_recursive(values, target, mid + 1, high)
    

values = range(1, 11)  # Example sorted array from 1 to 10
target = 3
result = binary_search_recursive(values, target, 0, len(values) - 1)
print(result)