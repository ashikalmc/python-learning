class Student:
    name = "Ashika"

s1 = Student()
print(s1.name)    

class Car:
    color = "red"
    model = "mercedes"

cars = Car()
print(cars.color)    
print(cars.model)    

#Constructor

class Student:
    college_name = "Bernhardt College"
    def __init__(self, name,marks):
        self.name = name
        self.marks = marks
        print("Add new name in DB..")
s1 = Student("Ashika" ,98)
print(s1.name ,s1.marks)  
s2 = Student("Riju" ,75)
print(s2.name,s2.marks)  
s3 = Student("Nishika" ,67)
print(s3.college_name)
class Student:
    #default Constructor
    def __init__(self):
        pass
    #Parameterzied Constructor
    def __init__(self, name,marks):
        self.name = name
        self.marks = marks
        print("Add new name in DB..")
s1 = Student("Ashika" ,98)
print(s1.name ,s1.marks)  
s2 = Student("Riju" ,75)
print(s2.name,s2.marks)  
s3 = Student("Nishika" ,67)
print(s3.name ,s3.marks)  


#Method
# def hello(self):
#     print("Welcome All",self.name)
# s1.hello()

# Q1. Create a student class that takes marks of 3 subject as argument in constructor. then create a method that print an average.

class Student:
    def __init__(self, marks, name):
        self.marks = marks
        self.name = name
        print("marks of three subject")

        def avg_marks(self):
            sum = 0
            for val in self.marks:
                sum += val
                print("Hi",self.name , "You Score", sum/3)
s1 = Student([98,60,76], "Ram")

class Student:
    @staticmethod
    class hello():
        print("Hope you are there")

s1 = Student()


