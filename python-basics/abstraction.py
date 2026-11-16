# #Abstraction

# class Car:
#     def __init__(self):
#      self.acc = False
#      self.brk = False
#      self.clauth = False
    
#     def start(self):
#         self.acc = True
#         self.clauth = True
#         print("Now Go !!")

# car1 = Car()
# car1.start()

# #Create a class called Account and 2 attributes balance and account no.create method for debit , credit and printing the balance

# class Account:
#    def __init__(self, accountno, balance):
#       self.accountno = accountno
#       self.balance = balance

#     #debit balance
#      def debit(self, amount):
#         self.balance -= amount
#         print("RS.",amount,"Was Debited form your Account")
#         print("Your Total Amount is now:",self.get_balance)
#     #Credit balance
#      def credit(self, amount):
#         self.balance += amount
#         print("RS.",amount,"Was Credit form your Account")
#         print("Your Total Amount is now:",self.get_balance)

#     def get_balance(self):
#       return self.balance


# Customer1 = Account(100, 139000)
# Customer1.debit(13900)
# Customer1.credit(13000)
# Customer1.credit(20000)
# print(Customer1.accountno)
# print(Customer1.balance)


#Del Keyword
class  Student:
    def __init__(self, name):
      self.name = name

s1 = Student("Ashika")
del s1
# print(s1)

#Public & Private

# class Account:
#    def __init__(self, acc_pass, acc_no):
#       self.acc_pass = acc_pass
#       self.__acc_no = acc_no

#     def reset_pass(self):
#       print(self.__acc_pass)

# a1 = Account(169,12345)
# print(a1.acc_pass)
# print(a1.reset_pass())

