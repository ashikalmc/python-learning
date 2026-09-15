#List
marks = [75,98,90,58]
print(marks)
print(type(marks))
print(marks[1])
print(len(marks))

#list slicing
name = ["Ashika","Ram","Sita","Hari"]
print(name)
print(name [1:3])

#list function
num = [1,5,2,3]
print(num.append(7)) #add element at the end
print(num.sort()) #ascending order
print(num.sort(reverse = True)) #decencding order
print(num.reverse()) #reverse
print(num.insert(0,9))  #insert element at index

#list method
fruits = ["Apple","Mango","banana","Apple","Orange","Straberry"]
print(fruits.pop(2))
print(fruits.remove("Apple"))

#TUPLES
tup = (55,23,65,12)
print(tup)
print(type(tup))
print(tup[0])

#single value
num = (9,)
print(num)

#method
digit = (9,1,3,9)
print(digit)
print(digit.index(9))
print(digit.count(9))

#Q1.Wap to ask the user to enter their 3 favorite movies and store them in a list
movie1 = input("enter 1st movie : ")
movie2 = input("enter 2st movie : ")
movie3 = input("enter 3st movie : ")

movies = [movie1 , movie2 , movie3]
print(movies)

movies.append(input("enter 1st movie : "))
movies.append(input("enter 2st movie : "))
movies.append(input("enter 3st movie : "))
print(movies)

#Q2. WAP to check if a list contain palindrome of element
num1 = [1,2,1]
num2 = [1,2,3]
num1_copy = num1.copy()
num1_copy.reverse()
if(num1 == num1_copy):
    print("it is palindrom")
else:
    print("not a palindrom")

#Q3 WAP to cound the number of student with the A grade in the following tupile
grade = ("A","C","A","D","B")
print("The total num of student with A grade is :",grade.count("A"))

#Q4 Store the above value in a list and sort them from A to D
grade = ["A","C","A","D","B"]
grade.sort()
print(grade)