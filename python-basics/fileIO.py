#writing a file

f = open("demo.txt","w")
f.write("Keep Going !!")
f = open("demo.txt","a") #for append
f.write("\n You can do it")
f.close()

#reading a file by using a function
def learn():
 f = open("demo.txt","r")
data = f.read()
print(data)
print(type(data))
learn()

#by using with for read
with open("demo.txt","r") as f:
    data = f.read()
    print(data)

# for write
with open("demo.txt","w") as f:
    f.write("Hello Everyone")

#deleating a file

import os
os.remove("demo.txt")

#Q1 create a new file "practice.txt" using py. add a following datail it: Hello EverOne. I am learning file I/O using Python.
# f = open("practice.txt","w")
# f.writelines("Hello EveryOne")
# f = open("practice.txt","a")
# f.write("\n We are learning file I/O using Python")
# f.close()
with open("practice.txt","w") as f:
    f.write("Hello EveryOne \n")
    f.write("I am learning file I\o using Python.")

#Q2 WAP that replace all the occurance of "learning" with "practice" in the above file

with open("practice.txt","r") as f:
    data = f.read()
    new_data = data.replace("learning","practice")
    print(new_data)

with open("practice.txt","w") as f:
    f.write(new_data)

#Q3 Search if the word "learning" exits in the file or not

word = "learning"
with open("practice.txt","r") as f:
    data = f.read()
    if(data.find(word) != -1):
        print("found")
    else:
        print("not found")
