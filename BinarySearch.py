def bSearch(v, l):
    if l == []:
        return False
    
    m = len(l) // 2

    if int(l[m]) == v:
        return True
    
    if v < int(l[m]):
        return bSearch(v, l[:m])
    else:
        return bSearch(v, l[m+1:])

# Input section
l = input("Enter the elements of the list with space: ").split()
v = int(input("Enter the number to be searched: "))
l = list(map(int, l))  # Convert input list to integers
l.sort()
print(bSearch(v, l))
