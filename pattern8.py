row=4
count=0
for i in range(1,row-1):
    for j in range(i):
        print(chr(65+count),end=" ")
        count+=1
    print()