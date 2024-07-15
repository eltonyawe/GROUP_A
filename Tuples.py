tup1 = ("Audio","Maybach","Mustang","Raum","Bugaati")
print(tup1)
#Accesing items in a tuple
tup1 = ("Audio","Maybach","Mustang","V8","Bugaati")
print(tup1[0])
print(tup1[-1])
print(tup1[3])

#Slicing items in the tuple
print(tup1[0:-1])
print(tup1[2:4])



#Concancating two tuples altogether
tuple001=('a','b','c','d','e')
tuple002=('f','g','h','i','j')
tuple1=tuple001 + tuple002
print(tuple1)


#Interating over items in atuple
for t in tuple1:
    print(t)




#Creating a tuple containing a list
sammer = (12,44,('food','sauce'),True,False,[2.55,3.006,100000000000])
print (sammer)


#Concancating two tuples as one 
sam2 = ('boy','girl','  ',400,100,['Feb ','Jan',22.6],[('hommie','tomboy'),(100,200,300,400,500)])
sam3 = sam2 + sammer
print(sam3)

#Interating over items in atuple
for s in sam3:
        print(s)

#Determining the length of the items in the tuple
print(len(sam3))

