def finder(arr1,arr2):
    result=0
    for num in arr1+arr2:
        result^=num
    return result

print(finder([3,4,1],[1,2,3,4]))