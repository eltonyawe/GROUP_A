#Iterating Using Seqeunce  {lists,tuple,sets,dict}
numbers =(1,2,3,4,5)
for number in numbers :
    print(number)


# Numbers are Iterated 1-20" using Range.
for digits in range(1,11):
    print(digits)
    

#Number are Reversed from big to small "10-1"
for num in reversed(range(10,21)):
    print(num)
    

# Using a for loop in a function  (for interating over items in the function)
def language():
    characters = "SQL"
    for character in characters:
        print(character)
          
def skill():
    characters = "Database"
    for x in characters:
        print(x)

language()        
skill() 




#Ranging Number by sequence "3" when iterating.
for num in range(1,21,3):
    print(num)
    


#Continue in For Loop
for number in range(1,11):
    if number == 5:
        continue
    else:
        print(number)
        
        
#Break in For Loop
for x in range(1,100):
    if x == 50:
        break
    else:
        print(x)   


#Iterating Using Strings.
visa_card = "1234-5678-3456-6645"
for each_number in visa_card :
    print(each_number)

print("Success!!!")    


#Creating a num pad using a for loop and a 2D List
Num_pad =[[1,2,3,],
          [4,5,6],
          [7,8,9],
          ["*",0,"#"]]
print(Num_pad)
for loop in Num_pad :
    for Num_pad_og in loop :
        print(Num_pad_og,end=" ")
    print()






