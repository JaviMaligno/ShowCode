from datetime import datetime, timedelta

class DeliveryDates:
    bank_holidays = set()
    weekend = [5,6]

    def calculate_delivery_date(self, OrderDate, LeadTime, DispatchCutOff, WorkingDayDeliveryOnly):
        # Your code goes here
        INVALID = "Invalid Data"
        
        FORMAT_DATE = "%d/%m/%Y %H:%M:%S"
        FORMAT_HOUR = "%H:%M:%S"
        FORMAT_DAY = "%d/%m/%Y"
        booleans = ["True", "False"]
        
        #it is supposed to received the string noot the boolean
        #if  not isinstance(WorkingDayDeliveryOnly,bool):
         #   return INVALID
        try:
            lead_time = int(LeadTime)
            spaces = OrderDate.count(' ') #in case the number of spaces matters for the chaallenge
            if lead_time < 0 or WorkingDayDeliveryOnly not in booleans or spaces != 1:
                return INVALID
        except:
            return INVALID
    
        try: 
            dispatch_cut_off = datetime.strptime(DispatchCutOff, FORMAT_HOUR
            ).time()
            order_date = datetime.strptime(OrderDate, FORMAT_DATE)  
            order_day = order_date.date() 
            order_time = order_date.time() 
            lead_time = timedelta(days = lead_time)  
        except:
            return INVALID
        
        delivery_date = order_day + lead_time if self.on_time(order_time,dispatch_cut_off) else self.next_day(order_day + lead_time)
        
        if WorkingDayDeliveryOnly == "True":
            while self.is_bank_holiday(delivery_date) or self.is_weekend(delivery_date):
                delivery_date = self.next_day(delivery_date)
        else:
            while self.is_bank_holiday(delivery_date):
                delivery_date = self.next_day(delivery_date)
                
        delivery_date = datetime.strftime(delivery_date, FORMAT_DAY)  
        return delivery_date

    @staticmethod          
    def on_time(order, cut_off):
        return True if order < cut_off else False
    
    def add_bank_holidays(self, year):
        new_year = datetime(year, 1, 1).date()
        xmas = datetime(year, 12, 25).date()
        boxing = datetime(year, 12, 26).date()

        if new_year.weekday() == 5:
            monday = self.next_day(self.next_day(new_year))
            self.bank_holidays.add(monday)
        elif new_year.weekday() == 6:
            monday = self.next_day(new_year)
            self.bank_holidays.add(monday)
        else:
            self.bank_holidays.add(new_year)

        # 25 and 26 go together, so I only need to check 25 and add monday and tuesday when necessary
        if xmas.weekday() == 4:
            # if xmas is friday, boxing is saturday, so add monday as well
            monday = self.next_day(self.next_day(boxing))
            self.bank_holidays.update([xmas, monday])
        elif xmas.weekday() == 5:
            # if xmas is saturday, then add monday and tuesday
            monday = self.next_day(boxing)
            tuesday = self.next_day(monday)
            self.bank_holidays.update([monday,tuesday])
        elif xmas.weekday() == 6:
            # if xmas is sunday, also add monday and tuesday, but monday is already boxing
            tuesday = self.next_day(boxing)
            self.bank_holidays.update([boxing, tuesday])
        else:
            # else non of them is a weekend so just add xmas and boxing
            self.bank_holidays.update([xmas, boxing])


    def is_bank_holiday(self, date):
        year = date.year
        # compute the bank holidays for this year
        self.add_bank_holidays(year)
        return True if date in self.bank_holidays else False

    
    def is_weekend(self, date):
        weekday = date.weekday()
        return True if weekday in self.weekend else False
    
    @staticmethod  
    def next_day(date):
        return date + timedelta(days = 1)
