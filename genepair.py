def generate_pairs(lst):
    return [(lst[i], lst[i+1]) for i in range(len(lst)-1)]
numbers = [1, 2, 3]
output = generate_pairs(numbers)
print(output)

def generate_pairs(lst):
    return [(lst[i],lst)]