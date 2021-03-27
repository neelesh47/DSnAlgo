def pair_sum(arr, k):
    if len(arr)<2:
        return 
    seen = set()
    output = set()
    for num in arr:
        target = k - num
        if target not in seen:
            
            seen.add(num)
        else:
            output.add((min(num,target),max(num,target)))
    return output

print(pair_sum( [-5, 1, -40, 20, 6, 8, 7 ],15))