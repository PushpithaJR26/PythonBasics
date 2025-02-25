def sublists_sum(lst,target):
    result= []
    for i in range(len(lst)):
        sum = 0
        for j in range(i,len(lst)):
            sum += lst[j]
            if sum ==target:
                result.append(lst[i:j+1])  
    return result


print(sublists_sum([1, 2, 3, 4, 5], 5))
