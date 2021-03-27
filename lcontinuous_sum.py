def l_cont_sum(arr):
    if len(arr)==0:
        return 0
    max_sum = current_sum = 0
    for i in arr[1:]:
        current_sum=max(current_sum,current_sum+i)
        max_sum=max(current_sum,max_sum)
    return max_sum

print(l_cont_sum([1,2,-1,1,4,10,10,-10,-1]))