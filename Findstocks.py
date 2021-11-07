import json_read
# this function looks for the stocks of a particular fund name in loaded json file "fund_collection"
def find_stocks(fund_name):
    for i in json_read.fund_collection["funds"]:
        if i["name"] == fund_name:
            return i["stocks"]
    


