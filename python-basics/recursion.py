def countdown(n):
  if n <= 0:
    print("Done!")
  else:
    print(n)
    countdown(n - 1)

countdown(5)

def factorial(n):
  # Base case
  if n == 0 or n == 1:
    return 1
  # Recursive case
  else:
    return n * factorial(n - 1)

print(factorial(5))

def fibonacci(n):
  if n <= 1:
    return n
  else:
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(7))
#recursive function
def show(n):
  if (n == 0): #basecase
    return
  print(n)
  show(n-1)
  print("End call stack")

show(5)

def fact(n):
  if(n==0 or n==1):
    return 1
  else:
    return n*fact(n-1)

print(fact(5))

#Q1 WAP to calculate the sum of first n natural number by using recursion.
def cal_sum(n):
  if(n==0):
    return 0
  print(n)
  return cal_sum(n-1) + n
print(cal_sum(5))

#Q2 Write a recursive function to print all element of list
def print_list(list,idx=0):
  if(idx == len(list)):
    return
  print(list[idx])
  print_list(list,idx+1)

color = ["red","orange","yellow"]
print_list(color)