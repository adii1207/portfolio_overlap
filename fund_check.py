from json_read import fund_collection

# fund_collection is where the funds.json file is loaded
#this function returns true if a fund name exist in funds json file
def fund_existence(fund_name):

    for name in fund_collection["funds"]:
        # "name" is the key in funds.json file
        if name["name"] == fund_name:
            return True
        



