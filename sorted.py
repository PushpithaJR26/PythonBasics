def unique_sorted_tuple(numbers):
    unique_numbers = sorted(set(numbers))  
    return tuple(unique_numbers)  
input_numbers = [4, 4, 44, 44]
output = unique_sorted_tuple(input_numbers)
print(output)  

