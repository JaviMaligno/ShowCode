from solution import NationwideAnalysis
import unittest
from collections import defaultdict

class NationwideAnalysisTests(unittest.TestCase):

    
    def test1(self):
        result = NationwideAnalysis()
        self.assertEqual(result.find_largest_payers([ "A paid £6 to B", "B received £1 from C", "A paid £2 to C" ]), [ "A", "C" ])

    def test2(self):
        result = NationwideAnalysis()
        self.assertEqual(result.find_largest_payers([ "A paid £0 to C" ]), [  ])
        
    def test_data_1(self):
        result = NationwideAnalysis()
        self.assertEqual(result.get_data("A paid £6 to B"), {"sender" : "A", "receiver" : "B", "amount" : 6})
    
    def test_data_1(self):
        result = NationwideAnalysis()
        self.assertEqual(result.get_data("B received £1 from C"), {"sender" : "C", "receiver" : "B", "amount" : 1})
        
    def test_update_dictionary1(self):
        result = NationwideAnalysis()
        transaction_dict = defaultdict(lambda: defaultdict(int))
        self.assertEqual(result.update_dictionary(transaction_dict, {"sender" : "A", "receiver" : "B", "amount" : 6}),{"A" : {"B": 6}})
        
    def test_update_dictionary2(self):
        result = NationwideAnalysis()
        transaction_dict = defaultdict(lambda: defaultdict(int), {"A" : {"B": 6}})
        self.assertEqual(result.update_dictionary(transaction_dict, {"sender" : "A", "receiver" : "B", "amount" : 6}),{"A" : {"B": 12}})
    
    def test_update_dictionary3(self):
        result = NationwideAnalysis()
        transaction_dict = defaultdict(lambda: defaultdict(int), {"A" : {"B": 6}})
        self.assertEqual(result.update_dictionary(transaction_dict, {"sender" : "A", "receiver" : "A", "amount" : 6}),{"A" : {"B": 6}})
    
    def test_format_transactions(self):
        result = NationwideAnalysis()
        self.assertEqual(result.format_transactions([ "A paid £6 to B", "B received £1 from C", "A paid £2 to C" ]),[{"sender" : "A", "receiver" : "B", "amount" : 6}, {"sender" : "C", "receiver" : "B", "amount" : 1}, {"sender" : "A", "receiver" : "C", "amount" : 2}]  )
        
    def test_update_transaction_dict(self):
        result = NationwideAnalysis()
        transaction_dict = defaultdict(lambda: defaultdict(int))
        transactions = [{"sender" : "A", "receiver" : "B", "amount" : 6}, {"sender" : "C", "receiver" : "B", "amount" : 1}, {"sender" : "A", "receiver" : "C", "amount" : 2}]
        self.assertEqual(result.update_transaction_dict(transaction_dict,transactions) , 
            {"A": {"B":6, "C":2}, "C":{"B":1}})
        
    def test_net_payments(self):
        result = NationwideAnalysis()
        transaction_dict = defaultdict(lambda: defaultdict(int), {"A": defaultdict(int,{"B":6, "C":2}), "B":defaultdict(int,{"A":3}), "C":defaultdict(int,{"B":1})})
        self.assertEqual(result.net_payments(transaction_dict), {"A":{"B":3, "C":2}, "B":{}, "C":{"B":1}})
        
    def test_total_payments(self):
        result = NationwideAnalysis()
        net_payments =  {"A":{"B":3, "C":2}, "B":{}, "C":{"B":1}}    
        self.assertEqual(result.total_payments(net_payments), {"A":5, "C":1})
        
    def test_top_senders1(self):
        result = NationwideAnalysis()
        self.assertEqual(result.top_senders({"A":5, "C":1}),["A", "C"])
    
    def test_top_senders2(self):
        result = NationwideAnalysis()
        self.assertEqual(result.top_senders({}),[])
        
 
        

if __name__ == '__main__':
    unittest.main()