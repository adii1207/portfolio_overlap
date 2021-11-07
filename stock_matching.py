
# this function will return matching stocks for given two fund name
# & operator performs inetrsection operation between two set(a data structure of python) and return common elements in sets
# This function returns a list(array) of common stocks between two funds

def match_stocks(fund_stock1, fund_stock2):
    try:
        stock1 = set(fund_stock1) # conversion of a list to set
        stock2 = set(fund_stock2)
        return list(stock1 & stock2)
    except Exception:
        return "Invalid Input"
