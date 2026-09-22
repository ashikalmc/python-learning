#function
def my_function():
  print("Hello from a function")

my_function()

def get_greeting():
  return "Hello from a function"

message = get_greeting()
print(message)

# function defination
def cal_sum(a,b): #parameters
  sum = a+b
  print(sum)
  return sum
#function call
cal_sum(12,3) #arguments
cal_sum(12,13)
cal_sum(22,33)

def cal_avg(a,b,c):
  return a+b+c/3
avg = cal_avg(22,33,45)
print(avg)

def greeding():
   print("hello Ashika")

greeding()

def greeding():
   print("hello Ashika")
name = greeding()
print(name) #none

print("Hello Ashika", end="")
print("lamichhane")

#user-define function
def cal_sum(a=1,b=2):
  sum = a+b
  print(sum)
  return sum

# cal_sum()
# def cal_sum(b,a=2): #default value
#   sum = a+b
#   print(sum)
#   return sum

# cal_sum()

#Q1 WAP to print the length of the list (list is the parameter)
name = ["Ashika","Riju","Sushma","Amit"]
def name_list(list):
  print(len(list))

print(len(name))

#Q2 WAP to print the element of the list in single line (list is the parameter)
favFlower = ["Rose","Sunflower","Lilly","Tulip","Lotus"]
def flower(list):
  print(list)

print(favFlower)

#Q3 WAP to find factorial of n (n is the parameter)
def fact(n):
  if  n <= 1:
   return n
  else:
    return fact(n - 1) + fact(n - 2)
print(fact(2))
