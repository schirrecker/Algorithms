import quick_sort as qs
import merge_sort as ms
import selection_sort as ss


l = [12, 1, 45, 2, 78, 11, 15, 56]

'''
print(qs.quick_sort(l))
print(ms.merge_sort(l))
print(ss.selection_sort(l))
'''

sorting_function = qs.quick_sort
print(sorting_function(l))

sorting_function = ms.merge_sort
print(sorting_function(l))
