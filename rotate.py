def rotate_left(arr, d):
    n = len(arr)
   
    d = d % n
    
    temp = arr[:d]
   
    for i in range(d, n):
        arr[i - d] = arr[i]
    
    for i in range(d):
        arr[n - d + i] = temp[i]


arr = [1, 2, 3, 4, 5]
d = 2
rotate_left(arr, d)
print("Rotated array:", arr)  # Output: [3, 4, 5, 1, 2]
