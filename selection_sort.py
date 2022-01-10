comparisons_ssort = 0

import random

def selection_sort(l):
    def smallest(l):
        global comparisons_ssort
        s = 0
        for i in range(1, len(l)):
            comparisons_ssort += 1
            if l[i] < l[s]:
               s = i
        return s
    

    l2 = l[:]
    new_list = []
    smallest_index = 0
    for i in range(0, len(l2)):

        smallest_index = smallest(l2)
        new_list.append(l2[smallest_index])
        l2.pop(smallest_index)
    return new_list

if __name__ == "__main__": 
    l = [6,1,8,2,7,9,56,256,3,27,25,81]
    #l = [random.randint(1,01
    print (selection_sort(l))
    print (str(comparisons_ssort) + " Operations")


