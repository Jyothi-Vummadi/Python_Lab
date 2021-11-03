def bs_recur(lst,l,h,key):
    for i in range(h+1):
        if lst[i] == key:
            return i+1
        elif lst[i] > key:
            return bs_recur(lst[ :i-1],l,i-1,key)
        else:
            return bs_recur(lst[i+1: ],i+1,h,key)
    return False
print(bs_recur([23,78,100,123,456],0,4,123))
