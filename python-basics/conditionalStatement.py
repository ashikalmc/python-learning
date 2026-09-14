#if-elif-else statement
#VOTE
age = int(input("Enter your age :",))
if(age >= 18):
    print("you are valid for vote")
elif(age <= 18):
    print("you are not eligiable for vote")
else:
    print("invalid, enter again")

#GREAD

marks = float(input("Enter your marks : ",))
if(marks>=90):
    print("A+",marks)
elif(marks > 90 and marks >= 80):
    print("B+",marks)
elif(marks > 80 and marks >= 70):
    print("C+",marks)
elif(marks > 70 and marks >= 60):
    print("D+",marks)
else:
    print("You have to study !!")

#driving

drivingAge = int(input("Enter your age : ",))
if(age >= 18):
    if(age>=80):
        print("Be safe")
    else:
        print("you can drive")
else:
    print("You cannot drive")

#Q1 click the number enter by the user is odd or even
num = int(input("Enter a number : "))
if(num % 2 == 0):
    print("even number")
else:
    print("odd number")
    
#Q2 find the greatest of 3 numbers enter by the user

firstNum = int(input("Enter a First number : "))
secondNum = int(input("Enter a Second number : "))
thirdNum = int(input("Enter a Third number : "))
if(firstNum >= secondNum and firstNum >= thirdNum):
    print("first number is greatest")
elif(secondNum >=firstNum and secondNum >= thirdNum):
    print("second number is greatest")
else:
    print("third number is greatest")

#Q3 cheak if the number is multiply by 7 or not

number = int(input("Enter a number : "))
if(number % 7 == 0):
    print("The number can be multiplyed")
else:
    print("The number cannot be multiplyed")

