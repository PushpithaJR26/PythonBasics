'''def concatenate_lists(lst1,lst2):
    result=[]
    for i in range(max(len(lst1),len(lst2))):
        result.append(lst1[i]+lst2[i])
    return result
print(concatenate_lists(['H','D','y'],['i','i','j']))'''

def cumulative_sum(list):
    result=[]
    total=0
    for num in list:
        total+=num
        result.append(total)
    return result

print(cumulative_sum([1,2,3,4]))