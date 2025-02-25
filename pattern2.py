def print_pattern(n):
    num=1
    for i in range(1,n+1):
        print(" "*(n-i),end=" ")
        for j in range(i):
            print(num,end=" ")
            num+=1
        print()

rows=4
print_pattern(rows)