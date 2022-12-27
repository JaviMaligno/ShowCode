from collections import defaultdict
from operator import itemgetter
from itertools import groupby
from datetime import datetime

class NiceMigration:

    @staticmethod
    def insert_in_order(transaction_list, element):
        if not transaction_list:
            transaction_list.append(element)
        else:
            date = element[0]
            for i in range(len(transaction_list)):
                if date < transaction_list[i][0]:
                    break
            else:
                transaction_list.insert(i+1, element)
                return transaction_list
            transaction_list.insert(i, element)
        return transaction_list

    @staticmethod
    def compute_value(current_value, t):
        operation = t[0]
        if operation == "++":
            return current_value + 1
        if operation == "--":
            return current_value - 1
        amount = t[1]
        if operation == "=":
            return amount
        if operation == "+":
            return current_value + amount
        if operation == "-":
            return current_value - amount
        if operation == "*":
            return current_value * amount
        if operation == '/':
            return current_value / amount

    @staticmethod
    def unpack(transaction_dict):
        tuples = []
        for k, t in transaction_dict.items():
            k = "@"+k[1:]
            for d, v  in t.items():
                d = datetime.strftime(d, "%Y%m%d")
                v = str(v)
                tuples.append((d, k, v))
        return tuples


    def convert(self, old_format):
        # Your code goes here
        account_transactions = defaultdict(list)
        #transactions = [old_format[m.start(): m.end()] for m in re.finditer("\d{8} #\d+",old_format)]
        transactions = old_format.splitlines()
        for transaction in transactions:
            parts = transaction.split()
            date = datetime.strptime(parts[0], "%Y%m%d")
            account = parts[1]
            operation = parts[2]
            amount = float(parts[3]) if len(parts) == 4 else ''
            info = (date, operation, amount)
            #account_transactions[account].append(info) # I could sort it here, but may be too much code (a different function)
            #info =  {date: (operation, amount)}
            account_transactions[account] = self.insert_in_order(account_transactions[account], info)
        
        account_values = defaultdict(list)
        for account, transactions in account_transactions.items():
            date_transactions = defaultdict(list)
            for date, info in groupby(transactions, itemgetter(0)):
                date_transactions[date] = list(map(lambda x: x[1:], list(info)))
            current_value = 0
            nicensess_by_date = defaultdict(float)
            for date, info in date_transactions.items():
                flag = False
                for op in info:
                    current_value = self.compute_value(current_value, op)
                    if current_value < 0:
                        flag = True
                nicensess_by_date[date] = '?' if flag else round(current_value,2) 
            account_values[account] = nicensess_by_date
            
        tuples = sorted(self.unpack(account_values), key= itemgetter(0,1))
        new_format = ''
        for t in tuples:
            new_format += ' '.join(t)+'\n'

        new_format = new_format[:-1]    

        
        return new_format


#print(NiceMigration().convert(example3))


