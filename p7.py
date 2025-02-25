row=6

count=0
for i in range(1,row+1):
    print(" "*(row-i),end=" ")
    for j in range(i):
        print(chr(65+count),end=" ")
        count+=1
    print()