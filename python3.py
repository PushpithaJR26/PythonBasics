fileObj1 = open("groups.txt","r")
fileObj2 = open("names.txt","w")
fileObj2.write(fileObj1.read())
fileObj3 = open("newNames.txt","w")
fileObj3.write(fileObj1.read())
print(fileObj3.read())
 
# below 3 lines are responsible to print output line by line
print(fileObj3.readline())
print(fileObj3.readline())
print(fileObj3.readline())
 
fileObj2.close()
fileObj1.close()