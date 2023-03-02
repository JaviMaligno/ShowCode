class MarketInterest:
    days = 365
    def maximum_value(self, interest_rates):
        # Your code goes here
        maximum_index = 0
        maximum = 0
        for (i,interest_rate) in enumerate(interest_rates):
            rate, gap, interest_type = interest_rate.split(",")
            rate, gap = float(rate)/100, int(gap)
            current_value = self.interest(rate, gap, interest_type)
            maximum_index, maximum = (i, current_value) if current_value > maximum else (maximum_index, maximum)
        return maximum_index
    
    def interest(self, rate, gap, interest_type,):
        time = self.days // gap
        interest = 0
        if interest_type == "S":
            interest = self.simple_interest(rate, time)
        elif interest_type == "C":
            interest = self.compound_interest(rate, time)
        return interest
            
    def simple_interest(self, rate, time):
        return 1+rate*time if time >= 0 else 0 
    
    def compound_interest(self, rate, time):
        return (1+rate)**time if time >= 0 else 0
    
