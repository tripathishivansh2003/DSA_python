def bubbleSort(lis):
    for i in range(len(lis)-1):
        for j in range(len(lis)-i-1):
            if lis[j] > lis[j+1]:
                lis[j] , lis[j+1] = lis[j+1] , lis[j]
    
    return lis

print(bubbleSort([10,99,32,4,9,55,23,77]))