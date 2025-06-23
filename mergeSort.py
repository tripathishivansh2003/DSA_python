def mergesort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr)//2
    left = mergesort(arr[:mid])
    right = mergesort(arr[mid:])

    return merge(left,right)

def merge(left,right):
    merged = []
    (i,j) = (0,0)
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i+=1
        else:
            merged.append(right[j])
            j+=1
        
    merged.extend(left[i:])
    merged.extend(right[j:])

    return merged

arr = [10,45,23,87,33,45,12]
array = mergesort(arr)
print(array)
