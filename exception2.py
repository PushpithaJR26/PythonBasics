print("starting line")
a = [11,22,33,77,99,55,43,6]
try:
    a= 10/5
    print(a[3])
    #print(y)
except ZeroDivisionError:
    print("Exception raised due to zero division error")
except IndexError:
    print("Exception raised due to index  out of range")
except NameError:
    print("Exception raised due to undefined variable")
except :
    print("Some exception raised")
else:
    print("no exception raised,everything workes perfect")
finally:
    print("this is a finnal block")
print("outside the block")
