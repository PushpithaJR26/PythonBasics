def rotate_list(lst, n):
    n = n % len(lst) 
    return lst[n:] + lst[:n]
print(rotate_list([1, 2, 3, 4, 5], 6))

