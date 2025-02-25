row =4
count=1
for i in range(row):
    for j in range(row):
        if i==0 or i==row-1 or j==0 or j==row-1:
            print("x",end=" ")
        else:
            for k in range(count,count+1):
                print(count,end=" ")
            count=count+1
    print()