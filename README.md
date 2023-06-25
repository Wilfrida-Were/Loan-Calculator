# Loan-Calculator
I wrote this simple script to help me in my current job.

The code calculates the total balance in a case with multiple loan repayments on specific default days. In my example case, I use one repayment made on day 53 but you can add more repayments if you want to. The number of days must also not exceed 60.

The parameters are:

loan_balance = loan balance RIGHT BEFORE the default days start

num_days = number of default days

daily default rate = 0.72%

repayments = amounts paid on specific default days. They are subtracted from the loan balance
