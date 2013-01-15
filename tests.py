import unittest

class TestFunctions(unittest.TestCase):
    def test_dots(self):
        self.date_string = '09.10.2010'
        self.order = 'straight'
        self.assertEqual(datetime.date(2010,10,9), check_date (self.date_string, self.order))

    def test_twonumber(self):
        self.date_string = '09/10/00'
        self.order = 'straight'
        self.assertEqual(datetime.date(2000,10,9), check_date (self.date_string, self.order))

    def test_opposite(self):
        self.date_string = '09.10.1999'
        self.order = 'opposite'
        self.assertEqual(datetime.date(1999,9,10), check_date (self.date_string, self.order))

    def test_leap1(self):
        self.date_string = '29.02.2012'
        self.order = 'straight'
        self.assertEqual(datetime.date(2012,2,29), check_date (self.date_string, self.order))

    def test_leap2(self):
        self.date_string = '29.02.2011'
        self.order = 'straight'
        self.assertRaises(DateException, check_date, self.date_string, self.order)

    def test_regular(self):
        self.date_string = '2.2.211'
        self.order = 'straight'
        self.assertRaises(DateException, check_date, self.date_string, self.order)
