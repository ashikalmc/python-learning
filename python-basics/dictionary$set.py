#Dictionary

infoStudent={
   "fullName ": "Ashika Lamichhane",
   "fav_language" : ["py","java","js"], #list
   "fav_color" : ("black","yellow"),  #Tuple
   "age " : 20,
   "study" : "BCA",
   "is_adult" : True
}
print(infoStudent)
print(infoStudent["study"]) #print key valuse
print(type(infoStudent))
infoStudent["age"] = 21
print(infoStudent["age"])

#empty dictionary
null_dic={}
print(null_dic)

#nested dictionary
student = {
    "name" : "Ashika",
    "subject" : {
        "nm" : 98,
        "py" : 99,
        "dsa" : 90
    }
}
print(student)
print(student["subject"])
print(student["subject"]["py"])

#dictionary Method
print(student.keys())
print(list(student.keys()))
print(student.values())
print(list(student.values()))
print(student.items())  #give in tuple
print(student["name"])
print(student.get("name"))
# print(student["name2"]) # give an error
print(student.get("name2"))  #give no erroe >> none
student.update({"rollNo" : 105 , "name" : "Sita Khadka"})
print(student)

#Set
set_collection = {1,3,4,7,"Ashika","py","Ashika",7}

print(type(set_collection))
print(len(set_collection))
print(set_collection) #set ignored the duplicated value

#empty set
emp = set()
print(type(emp))
print(emp)

#set method
students = {"ram","hari","krishna"}
print(student)
print(student.add("astha"))
print(student)
print(student.remove("ram"))
print(student.pop())
print(student.clear())

set1 = {1,4,5,6}
set2 = {2,4,3,5}
print(set1.union(set2))
print(set1.intersection(set2))

#Q1 Store the following word meaning in py dictonary > cat : "a small animal" , table : "a piece of furniture","a list of fact and figure"
storehouse = {
    "cat" : "a small animal",
    "table" : ["a piece of furniture","a list of fact and figure"]
}
print(storehouse)

#Q2 you are given a list of subject for student. assume that one classroom is required by one subject. how many classroom is needed by all student
subject = {"python","java","c++","python","java","javascript","python","java","c++","c"}
print(len.subject())

#Q3 WAP to enter 3 marks of the users and store them in a dictionary. start with an empty dictionary and add one by one, use subject name as key and marks as a value

# marks1 = float(input("enter first marks :"))
# marks2 = float(input("enter second marks :"))
# marks3 = float(input("enter third marks :"))
# null_dic = ()
# print(null_dic.items("python",marks1 ,"math",marks2,"dsa",marks3 ))

marks = {}
x = int(input("enter python marks:"))
marks.update(x)
x = int(input("enter math marks:"))
marks.update(x)
x = int(input("enter dsa marks:"))
marks.update(x)

#figure out a way to store 9 ans 9.0 as a seperate value in the set using build in datatype.

value = {
    "int" : 9,
    "float" :9.0
}
print(value)