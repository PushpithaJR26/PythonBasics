'''class Example:
    def add(self,a=1,b=2,c=0):
        return a+b+c
          
obj = Example()
print(obj.add(1,2))
print(obj.add(1,2,3))
print(obj.add(1))'''

class Example:
    def add(self, a=1, b=2, c=0):
        if a!=0 and b!=0 and c!=0:
            return a+b+c
        elif a!=0 and b!=0 and c==0:
            return a+b
        else:
            return a
        
obj = Example()
print(obj.add())     
print(obj.add( 2, 3))  
print(obj.add(1))      
