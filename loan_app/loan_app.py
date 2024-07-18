class LoanApplication:
    def __init__(self, applicant_name, loan_amount, annual_income, credit_score):
        self.applicant_name = applicant_name
        self.loan_amount = loan_amount
        self.annual_income = annual_income
        self.credit_score = credit_score

    def is_eligible(self):
        # Simple eligibility criteria
        if self.credit_score >= 700 and self.loan_amount < (self.annual_income * 0.5):
            return True
        return False

    def display_application_status(self):
        if self.is_eligible():
            print(f"{self.applicant_name}, your loan application is approved.")
        else:
            print(f"{self.applicant_name}, your loan application is denied.")

def main():
    print("Loan Application System")
    applicant_name = input("Enter your name: ")
    loan_amount = float(input("Enter the loan amount: "))
    annual_income = float(input("Enter your annual income: "))
    credit_score = int(input("Enter your credit score: "))

    application = LoanApplication(applicant_name, loan_amount, annual_income, credit_score)
    application.display_application_status()

if __name__ == "__main__":
    main()