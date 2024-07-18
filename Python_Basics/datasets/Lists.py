list_of_names =['Gavi','Pedri','John','Mosh','Najib','Eve']
print(list_of_names)

#Accesing item using index
print(list_of_names[-1])

#Appending a string at the end of the list
list_of_names.append('Adam')
print(list_of_names)


list_of_numbers =[1,2,3,4,5,6,7,8,9]
print(list_of_numbers)

#Reversing the list from desending order
list_of_numbers.reverse()
print(list_of_numbers)

#Inserting a number at index zero
list_of_numbers.insert(0,1000)
print(list_of_numbers)




list_of_dict =[{
    'ID' : 1,
    "Name" : "John Mosh",
    'Age' : 34,
    "Gender" :'Male',
    "Status" : "Married",
    'Occupation' : "Soft Engineer",
    "Credit History" : 1.0
}]
print(list_of_dict)
print(list_of_dict[0]['Name'])
print(list_of_dict[0]['Age'])


#Removing an item from the list 
tona= ['you',200,'boy']
print(tona)
tona.remove(200)
print(tona)


#Sorting items in the list in asending order  
p = [5,4,8,1,2,9,5,5,7,9,1,3,6]
p.sort()
print(p)


#Concatenating / Joining  lists together
list100 = ["mangoes","apples","melon"]
list200 = [1000,2000,3000,"Coding"]
Newlist = list100 + list200
print(Newlist)

#Determining the length/ number of items in the list
print(len(Newlist))

#Poping / removing/droping  an item  using its index
home = ['bigup',100,200,300,400]
print(home)
home.pop(0)
print(home)


#Extending an item to the end of the List as an interal(interating only strings)
eats = ['cake','bread','egg']
eats.extend('12345')
print(eats)

#Copy (returns a shallow list of items)
Go=[1,2,3,4,5,6,7,8,9,]
Go.copy()
print(Go)



#Clearing / Deleting all items in the list
Go1 = ['bigup',100,200,'cake','bread']
print(Go1)
Go1.clear()
print(Go1)

#Creating a 2D list 
items =      [['mangoes','oranges','grapes','melon'],
               ['carrots','nakati','cabbage'],
               ['beef','chicken']]
print(items)

#Accesing other lists in a 2D list
print(items[0])
print(items[1])
print(items[2])


#Accessing items of a 2D list
print(items[0][2])
print(items[1][1])
print(items[2][0])



#How add a list to a 2Dlist
food = [['potatoes','rice','chapati']]
menu = items+food
print(menu)

#How to update items in a 2D list
(items[1][1]) = 'lettus'
(items[0][0]) = 'pine-apple'
(items[2][-1]) = 'Samosa'


#Displaying updated values/items
print(items[1][1])
print(items[0][0])
print(items[2][-1])

#Displaying list after updating for clarity
print(menu)

#A List of Items
list_of_fruits = ['mangoes','apples','oranges','grapes']
print('Original list before Joining the list with a next line...')
print(list_of_fruits)


#Join function() it combines list items a one 
print('\n'.join (list_of_fruits))



#Reversed fun()  for arranging  items in desending order
numbers = [1000,200,300,400,500,600,700,800,900]
numbers.reverse()
print(numbers)


