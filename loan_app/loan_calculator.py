def calculate_monthly_payment(principal, annual_interest_rate, years):
    monthly_interest_rate = annual_interest_rate / 12 / 100
    number_of_payments = years * 12
    monthly_payment = (
        principal *
        monthly_interest_rate /
        (1 - (1 + monthly_interest_rate) ** -number_of_payments)
    )
    return monthly_payment

def main():
    print("Loan Calculator")
    principal = float(input("Enter the loan amount: "))
    annual_interest_rate = float(input("Enter the annual interest rate (in %): "))
    years = int(input("Enter the loan term (in years): "))

    monthly_payment = calculate_monthly_payment(principal, annual_interest_rate, years)
    total_payment = monthly_payment * years * 12

    print(f"\nMonthly Payment: ${monthly_payment:.2f}")
    print(f"Total Payment: ${total_payment:.2f}")

if __name__ == "__main__":
    main()