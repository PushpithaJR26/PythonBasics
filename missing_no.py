def missing_numbers(list):
    return [num for num in range(list[0],list[-1]+1)if num not in list]

print(missing_numbers([1,2,4,6,7])) 
