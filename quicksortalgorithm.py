import sys

limit = 2000
sys.setrecursionlimit(limit)

def quicksort(l):
    if len(l) < 2:
        return l
    else:
        pivot = l[0]
        less = [i for i in l[1:] if i <= pivot]
        greater = [i for i in l[1:] if i > pivot]

        return quicksort(less) + [pivot] + quicksort(greater)


l = [i for i in range(1, limit-100)]
print(quicksort(l))
