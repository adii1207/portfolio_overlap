import json 

# Reading funds.json file and loading its content 
with open('funds.json') as funds:
    fund_collection = json.load(funds)