print("starting line")
try:
    a = [11,22,33]
    print(a[2])
except:
    print("index error")
else:
    print("no exception raised,everything workes perfect")
finally:
    print("this is a finnal block")
print("outside the block")
