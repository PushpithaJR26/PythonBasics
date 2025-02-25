class Parent:
    def show(self):
        print("Parent Class")
class Child(Parent):
    def show(self):
        super().show()
        print("Child Class")
class Grandchild(Child):
    def show(self):
        super().show()
        print("Grandchild Class")
obj=Grandchild()
obj.show()




