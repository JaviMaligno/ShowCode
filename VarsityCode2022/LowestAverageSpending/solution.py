class Solution:

    def check_average_spending(self, monthly_spending):
        # Your code goes here
        if len(monthly_spending) < 3:
            return -1
        else:
            consecutive_months = zip(monthly_spending, monthly_spending[1:], monthly_spending[2:])
            average_spent = list(map(lambda x: sum(x)/3, consecutive_months))
            lowest_spent = min(average_spent)
            index = list(average_spent).index(lowest_spent)
            return index