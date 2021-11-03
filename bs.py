def bs(lst,key):
    l = 0
    h = len(lst)-1
    while(l<=h):
        m = (l + h)//2
        if lst[m] == key:
            return m+1
        elif lst[m] > key:
            h = m-1
        else:
            l = m+1
    return False
print(bs([12,34,56,78,100],78))
print(bs([12,34,56,78,100],105))
