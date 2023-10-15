from collections import defaultdict
class NationwideAnalysis:
    
    

    def find_largest_payers(self, transactions):
        # Your code goes here
        transaction_dict = defaultdict(lambda: defaultdict(int))
        transactions = self.format_transactions(transactions)
        transaction_dict = self.update_transaction_dict(transaction_dict,transactions)
        net = self.net_payments(transaction_dict)
        total = self.total_payments(net)
        top = self.top_senders(total)
        return top
        
        
    
    def get_data(self, transaction):
        parts = transaction.split(" ")
        sender, receiver = (parts[0], parts[-1]) if parts[1] == "paid" else (parts[-1],parts[0])
        amount = float(parts[2][1:])
        trans_summary = {"sender" : sender, "receiver" : receiver, "amount" : amount}
        return trans_summary
    
    def format_transactions(self, transactions):
        return list(map(self.get_data, transactions))
    
    def update_dictionary(self, dictionary, transaction):
        sender, receiver, amount = transaction["sender"], transaction["receiver"], transaction["amount"]
        if sender != receiver:
            dictionary[sender][receiver] += amount
        return dictionary
        
    def update_transaction_dict(self, transaction_dict, transactions):
        for transaction in transactions:
            self.update_dictionary(transaction_dict, transaction)
        return transaction_dict
    
    def net_payments(self, transaction_dict):
        senders = set(transaction_dict.keys())
        for sender, receivers in transaction_dict.items():
            senders.remove(sender)
            for receiver in set(receivers).intersection(senders):
                dif = transaction_dict[sender][receiver] - transaction_dict[receiver][sender]
                if dif > 0:
                    transaction_dict[sender][receiver] = dif
                    del transaction_dict[receiver][sender]
                else:
                    transaction_dict[receiver][sender] = -dif
                    del transaction_dict[sender][receiver]
        return transaction_dict
    
    def total_payments(self, net_payments):
        total_payments = defaultdict(int)
        for sender, receivers in net_payments.items():
            sent = sum(receivers.values())
            if sent > 0:
                total_payments[sender] = sent
            
        return total_payments
        
    def top_senders(self, total_payments):
        return sorted(total_payments.keys(), key=lambda x: -total_payments[x])
    
if __name__ == "__main__":
    result = NationwideAnalysis()
    print(result.find_largest_payers([ "A paid £0 to C" ]) == [])