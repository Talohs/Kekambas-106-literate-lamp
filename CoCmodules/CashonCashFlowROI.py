total = 0.0
return_on_invest = {
        'Down Payment': '40000',
        'Closing Costs': '3000',
        'Rehab budget': '7000',
        'Miscellaneous': '0',
        'Total Investment': '50000'
    } 

def roi_calculation():

    global total
    total
    for value in return_on_invest.values():
        # value = input(f"How much income from {value}?")
        total += float(value)
    return total

def roi_modifier(key, money):
    global total
    
    if key in return_on_invest:
        total -= return_on_invest.get(key)
        return_on_invest[key] = money
        total += float(money)
    else:
        print("Please input the investment value you wish to change: ")
    return total