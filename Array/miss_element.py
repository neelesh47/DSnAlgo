def finder(arr1,arr2):
    arr1.sort()
    arr2.sort()
    #print(arr1)
    for i,j in zip(arr1,arr2):
        if i !=j:
            return j 
    return arr2[-1]

print(finder([3,4,1],[1,2,3,4]))