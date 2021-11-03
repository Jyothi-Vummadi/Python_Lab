def ls_recur(lst,key):
    for i in range(len(lst)):
        if lst[i] == key:
            return i+1
        else:
            return(ls_recur(lst[i+1: ],key))
    return False
print(ls_recur([34,57,18,59,26,89,30,10],90))
