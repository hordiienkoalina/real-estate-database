def calculate_commission(sale_price):
    if sale_price < 100000:
        commission_rate = 0.10
    elif sale_price < 200000:
        commission_rate = 0.075
    elif sale_price < 500000:
        commission_rate = 0.06
    elif sale_price < 1000000:
        commission_rate = 0.05
    else:
        commission_rate = 0.04

    commission = sale_price * commission_rate
    return commission