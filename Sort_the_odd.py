"""
You have an array of numbers.
Your task is to sort ascending odd numbers but even numbers must be on their places.

Zero isn't an odd number and you don't need to move it. If you have an empty array, you need to return it.

Example

sort_array([5, 3, 2, 8, 1, 4]) == [1, 3, 2, 8, 5, 4]
"""

def sort_array(source_array):
    res = []
    odd_lst = [var for var in sorted(source_array) if var % 2 == 1]
    for var in source_array:
        if var % 2 == 0:
            res.append(var)
        else:
            res.append(odd_lst.pop(0))
            
    return res
    # Return a sorted array.
