from solution import DeliveryDates
import unittest

class DeliveryDatesTests(unittest.TestCase):

    
    def test1(self):
        result = DeliveryDates()
        self.assertEqual(result.calculate_delivery_date("Order Date", "Lead Time", "Dispatch Cut Off", "Working Day Delivery Only"), "Invalid Data")

    def test2(self):
        result = DeliveryDates()
        self.assertEqual(result.calculate_delivery_date("07/09/2022 13:00:00", "17", "12:00:00", "False"), "25/09/2022")

    def test3(self):
        result = DeliveryDates()
        self.assertEqual(result.calculate_delivery_date("07/09/2022 13:00:00", "3", "12:00:00", "True"), "12/09/2022")

    def test4(self):
        result = DeliveryDates()
        self.assertEqual(result.calculate_delivery_date("07/10/2022 11:00:00", "2", "12:00:00", "True"), "10/10/2022")

    def test5(self):       
        result = DeliveryDates()
        self.assertEqual(result.calculate_delivery_date("07/10/2022 11:00:00", "0", "12:00:00", "False"), "07/10/2022")

    def test6(self):       
        result = DeliveryDates()
        self.assertEqual(result.calculate_delivery_date("17/12/2022 11:00:00", "9", "12:00:00", "False"), "28/12/2022")

    def test7(self):       
        result = DeliveryDates()
        self.assertEqual(result.calculate_delivery_date("31/12/2021 11:00:00", "1", "12:00:00", "False"), "01/01/2022")

    def test8(self):       
        result = DeliveryDates()
        self.assertEqual(result.calculate_delivery_date("31/12/2021 11:00:00", "1", "12:00:00", "True"), "04/01/2022")

    def test9(self):       
        result = DeliveryDates()
        self.assertEqual(result.calculate_delivery_date("24/12/2021 11:00:00", "1", "12:00:00", "False"), "25/12/2021")

    def test10(self):       
        result = DeliveryDates()
        self.assertEqual(result.calculate_delivery_date("25/12/2021 11:00:00", "0", "12:00:00", "True"), "29/12/2021")

    def test11(self):       
        result = DeliveryDates()
        self.assertEqual(result.calculate_delivery_date("24/12/2015 11:00:00", "1", "12:00:00", "False"), "26/12/2015")

    def test12(self):       
        result = DeliveryDates()
        self.assertEqual(result.calculate_delivery_date("25/12/2015 11:00:00", "0", "12:00:00", "True"), "29/12/2015")    

    def test12(self):       
        result = DeliveryDates()
        self.assertEqual(result.calculate_delivery_date("25/12/2015 11:00:00", "-1", "12:00:00", "True"), "Invalid Data")

    def test12(self):       
        result = DeliveryDates()
        self.assertEqual(result.calculate_delivery_date("25/12/2015    11:00:00", "1", "12:00:00", "True"), "Invalid Data")
if __name__ == '__main__':
    unittest.main()