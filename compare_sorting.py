from pylab import plot, show, legend
import random
import quick_sort as qs
import merge_sort as ms
import selection_sort as ss


def compare_sorting_algorithms():
                            
    max_size = 100  # numbers between 0 and 100
    min_list_size = 10
    max_list_size = 30
    runs = 100
    merge_sort_comps = []
    quick_sort_comps = []
    selection_sort_comps = []
        
    for n in range(0, runs-1):
        l = [random.randint(0, max_size) for i in range(min_list_size, max_list_size)]
        qs.quick_sort(l)
        quick_sort_comps.append(qs.comparisons_qsort)
        qs.comparisons_qsort = 0
 
        ms.merge_sort(l)
        merge_sort_comps.append(ms.comparisons_msort)
        ms.comparisons_msort = 0

        ss.selection_sort(l)
        selection_sort_comps.append(ss.comparisons_ssort)
        ss.comparisons_ssort = 0
    
    print (runs, " runs of lists between ", min_list_size, " and ", max_list_size, ". Numbers between 0 and ", max_size)
    print ("Merge sort total comparisons: ", sum(merge_sort_comps))
    print ("Quick sort total comparisons: ", sum(quick_sort_comps))
    print ("Selection sort total comparisons: ", sum(selection_sort_comps))
    print ("Merge sort average comparisons: ", int(sum(merge_sort_comps)/len(merge_sort_comps)))
    print ("Quick sort average comparisons: ", int(sum(quick_sort_comps)/len(quick_sort_comps)))
    print ("Quick sort average comparisons: ", int(sum(selection_sort_comps)/len(selection_sort_comps)))
    print ()

    
    '''
    print("Merge sort comparisons: ", merge_sort_comps)
    print("Quick sort comparisons: ", quick_sort_comps)
    print("Selection sort comparisons: ", ss.comparisons_ssort)
    '''
    
    x = [n for n in range(1, runs)]
    plot (x, quick_sort_comps, x, merge_sort_comps, x, selection_sort_comps)
    legend(['Quick Sort','Merge Sort','Selection Sort'])
    show()

if __name__ == "__main__":
    compare_sorting_algorithms()
        
        
        
    
