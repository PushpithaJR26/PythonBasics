arr = [9, 4, 9, 6, 7, 4]
count = {}
for num in arr:
    if num in count:
        count[num] += 1
    else:
        count[num] = 1

for num in arr:
    if count[num] == 1:
        print("The first non-repeating element is:", num)
        break
else:
    print("No non-repeating element found in the array.")
