'''
Quick Sort algorithm
--------------------
1. Select a pivot
2. move all items greater than pivot on the right
3. move all items smaller than pivot on the left
4. temporarily sorted list = left_list + pivot + right_list
5. apply quick sort function recursively to left_lift and to right_list
6. until done: base case for recursion is a 2-item list
'''

import random

comparisons_qsort = 0

def quick_sort(ls):
    global comparisons_qsort
    # define base case here (if ls is 2 items, then return...)
    if len(ls) < 2:
        return ls
    
    pivot = ls[0]
    left = []
    right = []
    for i in range(1, len(ls)):
        if ls[i] > pivot:
            right.append(ls[i])
        else:
            left.append(ls[i])
        comparisons_qsort += 1
    # the new list is now left + pivot + right
    # return = left + [pivot] + right

    return quick_sort(left) + [pivot] + quick_sort(right)

