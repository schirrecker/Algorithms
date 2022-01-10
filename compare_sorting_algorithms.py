import random
import quick_sort as qs
import merge_sort as ms
import selection_sort as ss

l = [random.randint(1,100) for i in range(0,10)]
#l = [6,8,6,9,4,10,72,126,16,2,81,375,61,732]

def compare_sorting_algorithms():
    print("Say the name of a sorting algorithm to use it, and done to finish")
    sorting_algorithms = []
    output = ""
    while output.lower() != "done":
        output = input("Sorting algorithm: ")
        if output.lower() == "merge sort":
            sorting_algorithms.append("merge sort")
        elif output.lower() == "quick sort":
            sorting_algorithms.append("quick sort")
        else:
            print("Invalid sorting algorithm")
                            
    nr1 = input("Minimum size of elements in list: ")
    nr2 = input("Maximum size of elements in list: ")
    ls1 = input("Minimum list length: ")
    ls2 = input("Maximum list length: ")
    runs = int(input("How many times to run: "))
    nr1 = int(nr1)
    nr2 = int(nr2)
    ls1 = int(ls1)
    ls2 = int(ls2)
    
    for i in range(0, runs-1):
        l = [random.randint(nr1,nr2) for i in range(ls1+1,ls2+1)]
        if "quick sort" in sorting_algorithms:
            qs.quick_sort(l)
            print("Quick sort: ", qs.comparisons_qsort)
            qs.comparisons_qsort = 0
 
        if "merge sort" in sorting_algorithms:
            ms.merge_sort(l)
            print("Merge sort: ", ms.comparisons_msort)
            ms.comparisons_msort = 0

        print("")

compare_sorting_algorithms()
        
        
        
    
