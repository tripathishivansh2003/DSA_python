def SelectionSort(l):
    n = len(l)
    if n < 1:
        return l
    
    for i in range(n):
        mpos=i
        for j in range(i+1,n):
            if l[mpos] > l[j]:
                mpos = j
        (l[i],l[mpos]) = (l[mpos],l[i])
    return l

l = input("Enter the elements of the list with space: ").split()
l = list(map(int, l))  # Convert input list to integers
l.sort()
print(SelectionSort(l))
