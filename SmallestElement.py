def findSmallestElement(numbers):
    result = 1000000
    n =len(numbers)
    for index in range(n):
        if numbers[index] < result:
            result = numbers[index]
    return result

numbers = [12,34,21,34,55,56,34]
result = findSmallestElement(numbers)
print("Smallest element is:",result)


