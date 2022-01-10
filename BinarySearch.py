from time import sleep

def higher(n1, n2):
    if n1 > n2:
        return True
    elif n1 < n2:
        return False

def create_num_list(n1, n2):
    l = []
    for i in range(n1, n2):
        l.append(i)
    return l

def bin_search(l, i):
    low = 0
    high = len(l)+1

    if not i in l:
        print("invalid input")
        return "invalid"

    s = high/2
    r = high/2
    iterations = 1
    print("Value is: " + str(i))
    while s != i:
        print("Searching is : " + str(s))
        if higher(i,s):
            s += int(r/2)
            r = r/2
        else:
            s -= int(r/2)
            r = r/2
        sleep(0.1)
        
        iterations += 1
        

    print("Completed in " + str(iterations) + " iterations.")
    return s

        

bin_search(create_num_list(1,1000),214)


