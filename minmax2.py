def max_sum(lst,k):
    consecutive_sums = [sum(lst[i:i+k]) for i in range(len(lst)-k+1)]
    print("Consecutive sums:",consecutive_sums)
    max_sum=max(consecutive_sums)
    print("Maximum sum:",max_sum)
lst = [44,33,3,47,54,77,999]
k =2 
max_sum(lst, k)
