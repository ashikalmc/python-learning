#while loop
count = 0
while count <= 5 :
    print ("Hello Ashika",count) 
    count = count + 2

#Q1 Print number fom 1 to 100
# i = 1
# while i < 100 :
#     print(i)
#     i += 1
    
#Q2 Print number fom 100 to 1

j = 100
while j > 1 :
    print(j)
    j -= 1

#Q3 Print the multiplication table of a number n
n = 5
while n <= 50 :
    print (n) 
    n = n + 5
num = int(input("Enter a number :"))    
number = 1
while number <= 10 :
    print (number*num) 
    number += 1

#Q4 print the element from the list by using a list [1,4,9,16, 25, 36 ,49,81,100]
element = [1,4,9,16,25,36,49,81,100]
idx = 0
while idx < len(element):
    print(element[idx])
    idx += 1

#Q5 Search for a x in a tupile using loop :(1,4,9,16,25,36,49,64,81,100)
tup = (1,4,9,16,25,36,49,64,81,100)
x = 64
i =  0
while  i < len(tup):
      if(tup[i] == x) :
          print("x found",i)
          i += 1

 #break

cal = 1
while cal <= 5 :
    if(cal == 3):
        break
    print(cal)
    call += 1 


num = 0
while num <= 5 :
    if(num%2 == 0):
        num +=1
        continue #skip
    print(num)
    num += 1


#for loop
num = [1,2,3,4,5]
for val in num :
    print(val)

color = ("red","blue","green","white","pink","black","yellow")
for elements in color:
    print(elements)

str = "askika"
for char in str:
    print(char)

name = input("enter your name :")
for detail in name:
    print(detail)

#for loop with else
fruit = ("mango","orange","apple","straberry","banana")
for eat in fruit:
    print(eat)
else:
    print("Done")

fullName = "ashika lamichhane"
for nam in fullName:
    if(nam == "l"):
        print("l if found !!")
        break
    print(nam)
else:
    print("work done")

#Q1 print the following list using a loop : [1,4,6,16,25,36,49,64,81,100]

list = [1,4,6,16,25,36,49,64,81,100]
for num in list:
    print(list)

#Q2 search for a number x in this tuple using loop : (1,4,9,16,25,36,49,64,81,100)
x = 100
tup = (1,4,9,16,25,36,49,64,81,100) 
idx = 0
for search in tup:
    if(search == x):    
        print("x found",idx)
        break
        idx += 1

#Range in loop start, stop, step
seq = range(10)
for i in seq:
    print(i)
for j in range(5):
    print(j)
for even in range(2,10,2):
    print(even)
#Q1 print number from 1 to 100
for num in range(1,101):
    print(num)
#Q2 print number from 100 to 1
for reverse in range(100,0,-1):
  print(reverse)
#Q3 print the multiplication table of number n
n = int(input("enter a number of n :"))
for mul in range(1,11):
    print(n*mul)

#pass

for number in range(1,11):
    pass

print("hello World")

# WAP to find the factorial of first number n using for loop
n = int(input("enter a first n number"))
fact = 1
for i in range(1, n+1):
    fcat *= 1
    print("factorial is ", fact)


# WAP to find the sum of first number n using while loop
n = 5
sum = 0 
i = 1
while i <= 5:
     sum += i
     print(sum)