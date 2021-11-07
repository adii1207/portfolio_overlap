This program has funds.json file which contains all fund names and their stocks
write the input in test_file.txt in the following format:
CURRENT_PORTFOLIO FUND_NAME_1 FUND_NAME_2
CALCULATE_OVERLAP FUND_NAME
ADD_STOCK FUND_NAME STOCK_NAME

for example:
CURRENT_PORTFOLIO AXIS_BLUECHIP ICICI_PRU_BLUECHIP UTI_NIFTY_INDEX
CALCULATE_OVERLAP MIRAE_ASSET_EMERGING_BLUECHIP
CALCULATE_OVERLAP MIRAE_ASSET_LARGE_CAP
ADD_STOCK AXIS_BLUECHIP TCS
CALCULATE_OVERLAP MIRAE_ASSET_EMERGING_BLUECHIP

To run this program add input to test_file.txt and run the command "python -m geektrust <absolute path of file>"

test_program.py is a python file for unit testing

