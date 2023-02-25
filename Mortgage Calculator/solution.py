class MortgageCalculator:

    rate = 0.05
    years= 20
    
    def calculate_eligibility(self, number_of_people_on_mortgage, house_cost, deposit, salary1, salary2, annual_overpayment):
        # Your code goes here
        output = [0, 0, 0, 0]
        if not self.valid_input(number_of_people_on_mortgage, house_cost, deposit, salary1, salary2, annual_overpayment):
            return output
        
        maximum_possible_mortgage = 5 * (salary1 + salary2)
        output[0] = round(maximum_possible_mortgage,2)
        
        annual_repay = self.rate * maximum_possible_mortgage / (1 - (1 + self.rate)**-self.years)
        output[1] = round(annual_repay,2)
        
        total_repaid = annual_repay * self.years
        output[2] = round(total_repaid,2)
        
        years_to_pay = self.years_to_pay(total_repaid, annual_repay, annual_overpayment)
        output[3] =  years_to_pay
        
        return output
    
    def valid_input(self, number_of_people_on_mortgage, house_cost, deposit, salary1, salary2, annual_overpayment):
        valid = False
        if deposit < house_cost / 10:
            return valid
        if number_of_people_on_mortgage < int(bool(salary1)) + int(bool(salary2)):
            return valid
        if any( x < 0 for x in (number_of_people_on_mortgage, house_cost, deposit, salary1, salary2, annual_overpayment)):
            return valid
        if any(x == 0 for x in (number_of_people_on_mortgage, house_cost, deposit, salary1)):
            return valid
        
        return True
                
        
    def years_to_pay(self, total_repaid, annual_repay, annual_overpayment):
        owe = total_repaid
        total_annual_repay = annual_repay + annual_overpayment
        years = 0
        while round(owe,2) > 0:
            years += 1
            owe -= total_annual_repay 
        return years 
        
