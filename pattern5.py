row=4
count=1
i=1
while i<=row:
    print(" "*(row-i),end=" ")
    j=0
    while j<i:
        print(count,end=" ")
        count+=1
        j+=1
    print()
    i+=1