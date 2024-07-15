#Using If statements {if , else} 
loan_balance=30000
if loan_balance >= 10000:
    print("Not eligible for loan")
else:
    print("Eligible for Loan")
    

Account_bal = 600000  
if Account_bal >=500000:
    print("Salary Recevied")
else:
    print("Salary Not Recevied")


#Using if eilf to prevent repetition of if else statements 
#(it executes the next statement when the current turns false)
def discount(bal,buy_bal,acc_bal,total_bal):
    if bal >= 100000 :
        print(" Loan Allowed")
    elif buy_bal >= 150000:
        print('Loan Not allowed')
    elif acc_bal == 100000:
        print( 'Perfect Loan ') 
    elif total_bal > 500000:
        print('Loan Allowed')
    else:
        print('Not Allowed at all')       
    


discount(50000,70000,100000,1500000)


#Using if case to determine grade it eliminates over use of if else and if elif
def balance (balance):
    match balance :
        case balance if (balance >= 1000000):
            print("Perfectly Eligible for a loan")
        
        case balance if (balance >= 700000):
            print("Qualified For a Loan")  
        case balance if(balance >= 600000):
            print("Eligible to Less Money")
        case balance if(balance >=500000):
            print("Continue Transcating")     
        case balance if (balance <=400000):
            print("Loan Not allowed aparently")
m= int(input("limit :"))

balance(m)              

        
        

    
 


