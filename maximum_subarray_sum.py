"""
The maximum sum subarray problem consists in finding the maximum sum of a contiguous subsequence in an array or list of integers:

maxSequence([-2, 1, -3, 4, -1, 2, 1, -5, 4])
# should be 6: [4, -1, 2, 1]
Easy case is when the list is made up of only positive numbers and the maximum sum is the sum of the whole array. If the list is made up of only negative numbers, return 0 instead.

Empty list is considered to have zero greatest sum. Note that the empty list or array is also a valid sublist/subarray.
"""


def maxSequence(arr):
    print arr
    max = 0
    if arr:
        for index in range(len(arr)+1):
            for idx in range(len(arr)+1):
                if index < idx and max < sum(arr[index:idx]):
                    max = sum(arr[index:idx])
        return max
    else:
        return 0
