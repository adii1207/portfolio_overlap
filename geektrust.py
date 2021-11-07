import sys
import overlap, fund_check, stock_matching
from addstocks import ADD_STOCK
from Findstocks import find_stocks


current_fund_hold = [] #this list contains fund name which user hold currently


# this function stores the fund name that a user holds
def CURRENT_PORTFOLIO(*current_funds):
    for fund1 in current_funds[0]:
        current_fund_hold.append(fund1)
    return 1 


# this function prints the overlap in given format
# format of displaying overlap < FUND_NAME> <EXISTING_FUND> OVERLAP_PERCENTAGE%
def CALCULATE_OVERLAP(fund_name):
    stock_list2 = find_stocks(fund_name)
    if fund_check.fund_existence(fund_name) == True:
        
        for current_funds in current_fund_hold:
            stock_list1 = find_stocks(current_funds)
            matched_stocks = len(stock_matching.match_stocks(stock_list1, stock_list2))
            overlap_percent = overlap.overlap_calculation(matched_stocks, len(stock_list1), len(stock_list2))
            if overlap_percent == "0.00":
                continue
        
            else:
                print(fund_name, end=" ")
                print(current_funds, end=" ")
                print(overlap_percent, end = "")
                print("%")
        
    
    else:
        print("FUND_NOT_FOUND")

       

if __name__ == "__main__":

    input_file = sys.argv[1] # An absolute path will be provided for a file which conatain input for program

    # this function handles input given from test_file.txt and can have any number of arguments which is represented by *args. 
    # this program will recieve a list or array as an argument .
    # function checks zero index value of passed array and
    # looks for the values CURRENT_PORTFOLIO, ADD_STOCK, CALCULATE_OVERLAP
    # if zero ndex value is CURRENT_PORTFOLIO call CURRENT_PORTFOLIO() defined above 
    # if zero ndex value is ADD_STOCK call ADD_STOCK() defined above 
    # if zero ndex value is CALCULATE_OVERLAP call CALCULATE_OVERLAP() defined above
    # anything after zero index will be arguments for the function call
    # stock to be added is a white space separated string and has to eb considered one string 
    def function_call(*args):
        length = len(args[0])
        if args[0][0] == "CURRENT_PORTFOLIO":
            CURRENT_PORTFOLIO(args[0][1:length])

        elif args[0][0] == "ADD_STOCK":

            # It is a check for stock name  
            # if length of input file is three that means stock name is not white space separated, its only one string
            # else it is white space separated and needs to considered one string as a whole 
            if length <= 3:
                ADD_STOCK(args[0][1], args[0][2])
    
            else:
                stocks = ' '.join(args[0][2:length])
                ADD_STOCK(args[0][1], stocks)
        
        elif args[0][0] ==  "CALCULATE_OVERLAP":
            CALCULATE_OVERLAP(args[0][1])
        
    # reading test_file.txt which contain inputs for this prgram
    # Input is of format:  CALCULATE_OVERLAP <fund_name> : CALCULATE_OVERLAP ICICI_PRU_NIFTY_NEXT_50_INDEX
    #                      ADD_STOCK <fund_name> <stock_name> : ADD_STOCK TATA_BIRLA_FUNDS ACC limited
    #                      CURRENT_PORTFOLIO fund(1), fund(2), fund(3) ... fund(n) : CURRENT_PORTFOLIO TATA, TCS, ACC_Limited

    with open(input_file , 'r') as file:
        lines = file.readlines() # reading all the lines line by of input_file 
        
        #Accessing each line of input_file stored in "lines" variable through for loop
        for line in lines:
            function_call(line.split())
        current_fund_hold.clear()
        