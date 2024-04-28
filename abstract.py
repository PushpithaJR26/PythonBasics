from abc import ABC, abstractmethod

class Box(ABC):
    @abstractmethod
    def printColour(self):
        pass

class Box2(Box):
    def printPrice(self):
        print("Price is 45k")

    def printColour(self):
        print("colour is black")

obj = Box2()
obj.printColour()
obj.printPrice()