def findTotalOccurrences(listOfNumbers,target):
    result = 0
    n =len(listOfNumbers)
    for index in range(n):
        if listOfNumbers[index] == target:
            result = result + 1
    return result
 listOfNumbers = [12,34,21,-12,34,55,56,34,12]
 target = 34
 result = findTotalOccurrences(listOfNumbers,target)
 print("Total number of occurrences are:",result)
 list2 =[12,23,54,56,4,3,2,123,45,23]
 target2=23
 result2= findTotalOccurrences(list2,target2)
 print(result2)

