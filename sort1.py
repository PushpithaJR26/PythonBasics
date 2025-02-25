lst = [44, 33, 3, 49, 54, 77, 999]
sums = [lst[i] + lst[i+1] for i in range(len(lst)-1)]
sorted_sums = sorted(sums)
print("Sums of consecutive numbers:", sums)
print("Sorted sums:", sorted_sums)