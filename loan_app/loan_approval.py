loan_amount = int(input("From 1-1000000, Type your Loan Amount :"))
credit_amount =int(input("From 1-10, Type your Credit Amount :"))
income = int(input("From 1-1000000, Type your Monthly Income :"))
down_payment = int(input("From 1-1000000, Type your Down Payment :"))


if loan_amount >=500000:
    if income >=500000 and down_payment >=250000:
        print("Congralutions , You are preapproved for your loan request !")
    else :
        print("Sorry your loan was not approved, Bad luck try again next time")
elif loan_amount < 500000:
    if credit_amount <4:
        print("Sorry your loan was not approved, Bad luck try again next time")
    elif income >=490000 or down_payment >=150000:
        print("Congralutions , You are preapproved for your loan request !")
    elif income >=200000 and down_payment >= 100000:
        print("Congralutions , You are preapproved for your loan request !")
    else :
        print("Sorry your loan was not approved, Bad luck try again next time")
else :
    print("Sorry !")               

print("***********************")