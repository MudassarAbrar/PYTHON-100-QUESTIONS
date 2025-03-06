'''
Question 73
Please write a binary search function which searches an item in a sorted list. The function should return the index of element to be searched in the list.

Hints: Use if/elif to deal with conditions.
'''


def binary_search_function(item,sorted_list):
    min = 0
    max = len(sorted_list)-1
    
    while min <= max:
        mid = (min + max)//2#gets middles index
        
        if sorted_list[mid] == item:
            return mid
        elif sorted_list[mid] < item:
            min = mid + 1
        else :
            max = mid - 1
            
    return -1
        

sorted_list = [1, 3, 5, 7, 9, 11, 13]
item = 7
print(binary_search_function(item,sorted_list))