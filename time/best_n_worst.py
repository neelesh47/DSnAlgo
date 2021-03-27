def matcher(lst,match):
    for item in lst:
        if item == match:
            return True
    return False

print(matcher([1,2,3,4,5],1)) #Best case O(1)
print(matcher([1,2,3,4,5],6)) #Worst case O(n)
