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




p = lambda d: d*d
def  sqaured_function(p):
    return p

print(sqaured_function(p)(3))
