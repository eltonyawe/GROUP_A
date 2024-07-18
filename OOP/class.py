class Loan:
    def _init_(self, loan_amount, interest_rate, duration):
        self.loan_amount = loan_account
        self.interest_rate = interset_rate
        self.duration = duration
    

    def calculate_monthly_payment(self):
        # simple interest calculation for illustration purposes
        total_amount = self.loan_amount + (self.loan_amount * self.duration / 100)
        return total_amount / (self.duration * 12)
    

class PersonalLoan(Loan):
    def _init_(self, loan_account, interest_rate, duration, credit_score):
        super()._init_(loan_amount, interest_rate, duration)
        self.credit_score = credit_score
    
    def calculate_interest(self):
        if self.credit_score > 700:
            return self.interest_rate - 0.5
        else:
            return self.interest_rate 
        
    class Homeloan(Loan):
        def _init_(self, loan_amount, interest_rate, duration, property_value):
            super()._init_(loan_amount, interest_rate, duration)
            self.property_value = property_value


        def calculate_loan_to_value_ratio(self):
            return self.loan_amount / self.property_value
        
# Example usage
personal_loan = PersonalLoan(1000, 5, 5, 700)
print("Personal Loan Monthly Payment:", Personal_loan.calculate_monthly_payment())
    