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

