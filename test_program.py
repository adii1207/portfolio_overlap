import unittest
from addstocks import *
from fund_check import *
from Findstocks import *
from overlap import *
from stock_matching import *


class Test_Modules(unittest.TestCase):
    def test_adding_stock(self):
        self.assertEqual(ADD_STOCK("AXIS_MIDCAP", "breavrages"), 1) #adding stocks "breavragess" to "AXIS_MIDCAP"

    def test_checking_funds(self):
        self.assertEqual(fund_existence("AXIS_MIDCAP"), True) # "AXIS_MIDCAP" exist in funds.json file

    def test_finding_stocks(self):
        result_stocks = ["MPHASIS LIMITED",
        "COMPUTER AGE MANAGEMENT SERVICES LIMITED",
        "AMAZON.COM INC",
        "SUZUKI MOTOR CORPORATION*",
        "FACEBOOK INC",
        "INDIAN ENERGY EXCHANGE LIMITED",
        "BAJAJ HOLDINGS & INVESTMENT LIMITED",
        "MICROSOFT CORPORATION",
        "MULTI COMMODITY EXCHANGE OF INDIA LIMITED",
        "CENTRAL DEPOSITORY SERVICES (I) LIMITED",
        "PERSISTENT SYSTEMS LIMITED",
        "HCL TECHNOLOGIES LIMITED",
        "DR. REDDY'S LABORATORIES LIMITED",
        "ALPHABET INC.",
        "SUN PHARMACEUTICAL INDUSTRIES LIMITED",
        "HERO MOTOCORP LIMITED",
        "AXIS BANK LIMITED",
        "ICICI BANK LIMITED",
        "TATA MOTORS LIMITED",
        "HDFC BANK LIMITED",
        "CIPLA LIMITED",
        "LUPIN LIMITED",
        "IPCA LABORATORIES LIMITED",
        "MARUTI SUZUKI INDIA LIMITED",
        "ORACLE FINANCIAL SERVICES SOFTWARE LIMITED",
        "CADILA HEALTHCARE LIMITED",
        "ICRA LIMITED",
        "ITC LIMITED",
        "TATA STEEL LIMITED",
        "BALKRISHNA INDUSTRIES LIMITED"] 
        self.assertEqual(find_stocks("PARAG_PARIKH_FLEXI_CAP"), result_stocks) #"PARAG_PARIKH_FLEXI_CAP" exist in funds.jso file 

    def test_overlap(self):
        self.assertEqual(overlap_calculation(20,40,30), "57.14") # recieving integer inputs 
        self.assertEqual(overlap_calculation('a', 'b', 'c'), "Invalid input")# recieving string input
        self.assertEqual(overlap_calculation([20], [40], [30]), "Invalid input")# receiving list as input

    def test_match_stocks(self):
        self.assertEqual(match_stocks(['a', 'b', 'c', 'd', 'a', 'd'], ['a', 'p', 'q']), ['a'])# receiving iterable as input
        self.assertEqual(match_stocks(12, 23), "Invalid Input")# receiving non iterables as input

   


   
        