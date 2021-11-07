#this function returns overlap calculation in decimal point representation up to two decimal points
def overlap_calculation(common_stocks, stock_A, stock_B):
    try:
        common_stocks += common_stocks
        stock_A = stock_A + stock_B
        overlap = (common_stocks / stock_A) * 100 # percentage of overlap calculated
        return format(overlap, '.2f')
    except Exception:
        return "Invalid input"






