#string
str1 = "hello"
str2 = 'Ashika'
str3 = '''What you are doing ?'''

#string concatenation
msg = "hello \t" + "Ashika"
print(msg)

#stringlength
str = "Welcome to the new journey of py !"
totalLen = len(str)
print ("total length of the string is:",totalLen)
# print(len(str))

#indexing
strname = "Ashika"
ch = strname[3]
print(ch)
print(ch[0])

#slicing
fullName = "Ashika Lamichhane"
slicStr = fullName[1:8]
print(slicStr)
print(fullName[:6])
print(fullName[6:])
#negative indexing 
print(fullName[-6:])

#string function
str = "I am learning Python"
#endword
print(str.endswith("on"))
#capitalized
print(str.capitalize())
#replace
print(str.replace("Python","JS"))
#find
print(str.find("learning"))
#count
print(str.count("a"))

#Q1 WAP to input user first name and find its length
userName = input("Enter your name :")
print("User Name is :",userName)
print("The total length of User Name is :",len(userName))

#Q2 WAP to find the occurance of $ in the string
note = "I have $500 to buy a new friction book"
print(note.count("$"))

