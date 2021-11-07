import json_read

# adds stock name to the given fund name in the loaded funds.json file if it exist
def ADD_STOCK(Fund_name, stock_name):
    for i in json_read.fund_collection["funds"]:
        if i["name"] == Fund_name:
            i["stocks"].append(stock_name)
            return 1
