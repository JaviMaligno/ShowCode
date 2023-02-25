# TASK

Your task is to create a mortgage calculator using the potential buyers' financial information that tells them how much they could borrow for their dream home.

First, you will have to calculate how much the buyers can borrow. The next step of this task is to create a calculator to determine how long it would take to repay the mortgage if the borrower(s) were to pay a value larger than the minimum repayment.

The information that potential buyers will give is:

- The number of people on the mortgage - this is a maximum of 2 people for a joint mortgage
- The deposit amount that they have saved
- The individual salaries of the people applying for the mortgage
- Amount of annual overpayment

In order to take out a mortgage, the buyer(s) needs a minimum deposit of 10% of the mortgage.

If they meet this criteria, the calculator should tell them how much they could borrow which uses the following equation:

**Maximum possible mortgage = 5 * sum of salaries**

**Input must be a non-zero positive integer, unless it is the second salary (i.e. can be zero when only one person is on the mortgage) or the overpayment, which can be zero.**

Once you have calculated how much they could borrow, we want to know how long it will take to repay the mortgage if the borrower were to overpay.

For this exercise, the minimum annual repayments (without overpaying) will be made annually with a fixed interest rate (5%) over a set period (20 years).

To find the minimum annual payment (without overpayment) the equation can be used:

**p=(r*x)/(1-(1+r)-y)**

where **p** is the repayment amount, **x** the amount borrowed/owed, **r** the interest rate (5%), and y the number of years until the mortgage is repaid (without overpayment).

The output is an array of floats (2 decimal places with all rounding done at the end) which should include:
- How much could be borrowed (if eligible)
- Amount of annual repayment (if only the minimum is paid)
- Total that is repaid (if only minimum is paid)
- Time taken (in years) to repay mortgage with overpayments

**Hint: remember to subtract the amount paid AND the overpayment to calculate what is still owed. To find what you currently owe = x * (1 + r) - s (remember to include overpayment).**
where **s** is the total annual repayment.
If the customer is unable to get a mortgage or there is invalid input, an array of zeros should be the output.

## EXAMPLES

### Example 1:

If the input is:
- Number of people on mortgage = 2
- House Cost = 400000
- Deposit = 20000
- Salary 1 = 38000
- Salary 2 = 45000
- Overpayment amount = £0
The deposit is not big enough (less than 10%) to get a mortgage for that house so the output is [0, 0, 0, 0].

OR

### Example 2:

If the input is:
- Number of people on mortgage = 1
- House Cost = 120000
- Deposit = 18000
- Salary 1 = 29000
- Salary 2 = 0
- Overpayment amount = £0
The customer could borrow up to £145000 with annual repayment amount of £11635.18 without overpayments, meaning over 20 years they would pay a total of £232703.50. The output is [145000, 11635.18, 232703.5, 20].

OR

### Example 3:

If the input is:
- Number of people on mortgage = 1
- House Cost = 120000
- Deposit = 18000
- Salary 1 = 29000
- Salary 2 = 0
- Overpayment amount = £2000
The customer could borrow up to £145000 with an annual repayment amount of £11635.18 without overpayments. If they overpaid by £2000 each year, they could repay their mortgage in 16 years. The output is [145000, 11635.18, 232703.50, 18].
