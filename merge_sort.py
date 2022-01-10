import random

comparisons_msort = 0

def merge_sort(l):
    global comparisons_msort
    new = []
    h = int(len(l)/2)

    if len(l) < 2:
        return l

    else:
        left = merge_sort(l[:h])
        right = merge_sort(l[h:])

        while (len(left) > 0) and (len(right) > 0):
            if left[0] < right[0]:
                new.append(left.pop(0))
            else:
                new.append(right.pop(0))
            comparisons_msort += 1

        new += left
        new += right  
        return new
    
if __name__ == "__main__":
    l = [random.randint(1,100) for i in range(0,10)]
    #l = [6,8,6,9,4,10,72,126,16,2,81,375,61,732]
    merge_sort(l)
    print(comparisons_msort)
