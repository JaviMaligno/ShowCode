from solution import NextSustainability
import unittest

class NextSustainabilityTests(unittest.TestCase):

    
    def test1(self):
        result = NextSustainability()
        self.assertEqual(result.percentage_recycled("Paper", [ "Paper - 60% recycled" ]), 60)

    def test2(self):
        result = NextSustainability()
        self.assertEqual(result.percentage_recycled("Shirt", [ "Shirt: 90% cotton 10% polyester", "Cotton - 10% recycled", "Polyester - 50% recycled" ]), 14)
        
    def test_process_material(self):
        result = NextSustainability()
        self.assertEqual(result.process_material("Paper - 60% recycled"), ("Paper", 60))
    
    def test_process_material_complex(self):
        result = NextSustainability()
        self.assertEqual(result.process_material("Shirt: 90% cotton 10% polyester", simple = False), ("Shirt",({"cotton": 90, "polyester": 10})))
        
    def test_add_material(self):
        result = NextSustainability()
        self.assertEqual(result.add_material("Paper", 60, {}), {"paper":60})
    def test_add_material_complex(self):
        result = NextSustainability()
        self.assertEqual(result.add_material("Shirt", {"cotton": 90, "polyester": 10}, {}), {"shirt": {"cotton": 90, "polyester": 10}})
        
    def test_database(self):
        result = NextSustainability()
        self.assertEqual(result.database([ "Shirt: 90% cotton 10% polyester", "Cotton - 10% recycled", "Polyester - 50% recycled" ]),
        ({"cotton": 10, "polyester":50},{"shirt": {"cotton": 90, "polyester":10}}))
        
    def test_empty_info(self):
        result = NextSustainability()
        self.assertEqual(result.percentage_recycled("Paper", [ ]), 0)
        
    def test_non_recyclable(self):
        result = NextSustainability()
        self.assertEqual(result.percentage_recycled("Shirt", [ "Shirt: 90% cotton 10% polyester"]), 0)
        
        
        
    

if __name__ == '__main__':
    unittest.main()