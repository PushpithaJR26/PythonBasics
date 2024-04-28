def sum_of_odd_elements(lst):
    total_sum = 0
    for num in lst:
        if num % 2 != 0:
            total_sum += num
    return total_sum

# Accept list of integers from the user
input_list = [int(x) for x in input("Enter list of integers separated by spaces: ").split()]

# Calculate and print the total sum of odd elements
print("Total sum of odd elements:", sum_of_odd_elements(input_list))
