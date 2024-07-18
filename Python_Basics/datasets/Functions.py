def sum (a,b):
    print("Sum of Two Numbers")
    sum = a+b
    return sum

total=sum(5,7)
print(total)


def substraction(x=100,y =1):
    print("Substraction of Two Numbers")
    substraction = x-y
    return substraction


print(substraction())


def mulitpication(one,two):
    mulitpication =one*two
    return mulitpication

one = int(input("First number :"))
two =int(input("Second number :"))
mult =mulitpication(one,two)
print(mult)



def division (v=10,j=2):
    print("Division of two numbers")
    division = v/j
    return division


print(division())


add = lambda x,y : x+y 
def adiition(x,y):
    return x,y

print(add(3,7))


p = lambda d: d*d
def  sqaured_function(p):
    return p

print(sqaured_function(p)(3))



def status(name,age,occupation):
    print(f'YourName :{name} - Your Age :{age} - Your Occupation : {occupation}')
    return name + occupation  
 
print(status('Yawe Elton',30,'Computer Programmer'))


def greet():
    return "Hi, how ae you doing there"


def reply():
    return "\n Hi, \nAm doing well, how are you?  \nhope you are fine."

print(greet()+reply())



def full_name(first_name,last_name):
    print("Your Name In Full")
    first_name = first_name.capitalize()
    last_name = last_name.capitalize()
    return first_name + last_name

name = full_name("yawe","elton")
print(name)


def add(x,y):
    adds = x+y
    return adds

list = [0,2,4,6,8,10,12]
mapped_list = map(add,list)
print(mapped_list)



def loan(people_eligible):
    return ("Verification Notice  :"+ people_eligible)

print("List of People Eligible for Loans")
print(loan(" Afford is eligible"))
print(loan(" Samson is eligible"))
print(loan(" Yaseen is not eligible"))
print(loan(" Tonny is eligible"))
print(loan(" Yawe is not eligible"))



#Function Definition of my Invoice
def invoice (name,amount,date,):
    print("Loan Still Owning")
    print (f"{name},you have a loan of ${amount:.2f},which is due by :{date},") 
    print("For more information cotact us on 0774935567")    
invoice("Yawe Elton", 6000, "1/August/2024")  

