def ls(lst,key):
    for i in range(len(lst)):
        if lst[i] == key:
            return i+1
    return -1
print(ls([34,78,27,89,276,128,289,45,49,89],45))
