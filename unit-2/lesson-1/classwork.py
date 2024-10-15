myList = ["lu", "is", "coding"]

print(myList)

myList.append("right now")

print (myList)

# when i run this file (like this:) python3 classwork.py
# these are printed below:
# ['lu', 'is', 'coding']
# ['lu', 'is', 'coding', 'right now']

isLuinlist = "lu" in myList
#"in" is a command that tells python to find 
print (isLuinlist)

# curly brackets define a dictionary
university = {}
university ["subject"] = "theory"
university ["course"] = "coding as a liberal art"
university ["department"] = "SPEliberal arts"

Isthisdept = "department" in university

# print (university)

students = ["zada", "chris", "sigrid"]
university ["roster"] = students
# this is doing the same thing as the one above by just attributing a variable to the list.
# we do have the possibility of simply attributing a string to a list as well. but im sure it must be limiting in some way"?""
# n