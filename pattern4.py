row=4
count=1
for i in range(1,row+1):
    print(" "*(row-i),end=" ")
    for j in range(i):
        print(count,end=" ")
        count+=1
    print()

