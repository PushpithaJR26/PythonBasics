# Sortings 
 
# 1. Bubble sort 
# 2. Selection sort 
# 3. Insertion sort 
# 4. Merge sort 
# 5. Quick sort 
 
def performInsertionSort(nums):
    n = len(nums)
    # [12, 3, 10, 18, 9, 200, 167]
    # n = 5
    # 1 2 3 4
    for index in range(1, n):
        temp = nums[index]
        position = index - 1 
        while position >= 0 and nums[position] > temp:
            nums[position + 1] = nums[position]
            position -= 1 
 
        nums[position + 1] = temp 
        print(nums)
 
#   Before sorting:
# [12, 2, 34, 20, 56, 43, 45, 100, 89, 50]
 
# [2, 12, 34, 20, 56, 43, 45, 100, 89, 50]
# [2, 12, 34, 20, 56, 43, 45, 100, 89, 50]
# [2, 12, 20, 34, 56, 43, 45, 100, 89, 50]
# [2, 12, 20, 34, 56, 43, 45, 100, 89, 50]
# [2, 12, 20, 34, 43, 56, 45, 100, 89, 50]
# [2, 12, 20, 34, 43, 45, 56, 100, 89, 50]
# [2, 12, 20, 34, 43, 45, 56, 100, 89, 50]
# [2, 12, 20, 34, 43, 45, 56, 89, 100, 50]
# [2, 12, 20, 34, 43, 45, 50, 56, 89, 100]
 
# After sorting:
# [2, 12, 20, 34, 43, 45, 50, 56, 89, 100] 
 
 
 
 
 
 
nums = [12, 2, 34, 20, 56, 43, 45, 100, 89, 50]
 
print("Before sorting:")
print(nums)
 
# logic to perform sorting 
 
performInsertionSort(nums)
 
print("After sorting:")
print(nums)
 
 
