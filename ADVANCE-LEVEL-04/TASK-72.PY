'''
Question 72
Please write a binary search function which searches an item in a sorted list. The function should return the index of element to be searched in the list.

Hints: Use if/elif to deal with conditions.
'''

def binary_search_function(item,sorted_list:list):
    low = 0
    high = len(sorted_list) - 1

    while low <= high:
        mid = (low + high) // 2  # Find the middle index
        if sorted_list[mid] == item:
            return mid  # Item found, return its index
        elif sorted_list[mid] < item:
            low = mid + 1  # Adjust the lower bound
        else:
            high = mid - 1  # Adjust the upper bound

    return -1  


sorted_list = [1, 3, 5, 7, 9, 11, 13]
item = 7
print(binary_search_function(item,sorted_list))