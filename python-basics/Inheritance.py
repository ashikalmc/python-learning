class Car:
    color = "Red"
    @staticmethod
    def start():
        print("Car Started!!")

    @staticmethod
    def stop():
        print("Car Stoped!!")

class Ford(Car):
    def __init__(self,brand):
        self.brand = brand
car1 = Ford("Roboto")
print(Ford.start())
print(Ford.color)

class Roboto(Ford):
    def  __init__(self,type):
        self.type = type

#Multiple  Inheritance
class A:
    vara = "Hello"
class B:
    varb = "Everyone"
class C(A, B):
    varc = "What's going on?"

person1 = C() 
print(person1.vara)
print(person1.varc)

