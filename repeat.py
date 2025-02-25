l1=(44,33,3,49,54,77,999,88888)
for num in l1:
     if(num%11==0 or (100<=num<=999)):
          print(num)

          
numbers = [44, 33, 3, 49, 54, 77, 999,4444,88888]
output = [num for num in numbers if num % 11 == 0 or (100 <= num <= 999)]
print(output)



    
    