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