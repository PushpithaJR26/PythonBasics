def performQuickSort(nums, left, right):
    # left = 0    right = 7 
    if left >= right:
        # whenever there are single length arrays, they are already sorted
        return 
    # [18, 10, 20, 15, 100, 90, 17]
    #  0   1    2   3   4   5    6
    pivotIndex = findPivotIndex(nums, left, right)
    # [10, 15, 17, 20, 100, 90, 18]
    print(nums)
 
    performQuickSort(nums, left, pivotIndex - 1)
    performQuickSort(nums, pivotIndex + 1, right)
 
#nums = [10, 5, 100, 50, 25, 80, 110, 108]
nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
# n = 8
n = len(nums)
print("Before sorting", nums)
 
performQuickSort(nums, 0, n - 1)
 
print("After sorting", nums)


