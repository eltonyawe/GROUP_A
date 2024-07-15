#Creating a diictionary using (string key)
dictionary = {
    'ID' : 1,
    'Name' : 'Yawe Elton',
    'Age' : '23',
    'Status' : 'Single & Searching'
}
print (dictionary)

#Accessing items in a dictionary using the key
print(dictionary['Name'])
print(dictionary['Age'])
print(dictionary['Status'])


#Changing items  to new values  basing on the key
dictionary['Name'] = 'John Mosh'
dictionary['Age'] = 40
dictionary['Status'] = 'Married'

print(dictionary)


#Deleting an item from the dictionary basing on the key
del dictionary['ID']
print(dictionary)

#Updating/adding an item at the end of the dictionary
dictionary.update({"Occupation":"Programmer","Salary":150000})
print(dictionary)


#Copy for showing a shallow copy of the dictionary
dictionary.copy()
print(dictionary)


#Accessing items using key (interger key)
students ={1 : "Samson",
           2 : "Yaseen",
           3 : "Elton",
           4 :'Afford',
           5 : 'Tonney' 
}
print(students)
print(students[1])
print(students[2])
print(students[3])
print(students[4])
print(students)


#Get for returning the value if existing in the dictionary or not & if not returns none as default
print(students.get(1))
print(students.get(4))
print(students.get(5))
print(students.get(10))


#Pop for removing the a value using on the key
students.pop(2)
print(students)

#Converting two lists into a dictionary
list1 =["beef","chicken","fish fillet"]
list2= [1,2,3]
dict10 = dict (zip (list2,list1))
print(dict10)