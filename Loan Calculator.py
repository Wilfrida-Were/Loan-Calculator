"""The code calculates the total balance in a case with multiple loan repayments on specific days
The parameters are:
loan_balance = loan balance RIGHT BEFORE the default days start
num_days = number of default days
daily default rate = 0.72%
repayments = amounts paid on specific default days. They are subtracted from the loan balance"""


def calculate_loan_balance(loan_balance, num_days, repayments):
    if not isinstance(loan_balance, int) or loan_balance <= 0:
        raise ValueError("Loan balance must be a positive integer.")
    if not isinstance(num_days, int) or num_days <= 0 or num_days > 60:
        raise ValueError("Number of days must be a positive integer not exceeding 60.")

    daily_default_rate = 0.0072  # 0.72% expressed as a decimal
    total_balance = loan_balance

    for day in range(1, num_days + 1):
        # Compound default charges
        default_charge = total_balance * daily_default_rate
        total_balance += default_charge

        # Subtract repayments on the specified day
        if day in repayments:
            total_balance -= repayments[day]

    return total_balance


# Example usage
loan_balance = 231334
num_days = 60
repayments = {53: 218240}

try:
    total_balance = calculate_loan_balance(loan_balance, num_days, repayments)
    print("Total loan balance after {} days: {}".format(num_days, total_balance))
except ValueError as e:
    print("Error:", str(e))
