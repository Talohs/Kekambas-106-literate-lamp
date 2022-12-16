total = 0.0
income = {
        'rental':'2000',
        'laundry':'0',
        'storage':'0',
        'misc':'0',
    } 

def income_calculation():

    global total
    total
    for value in income.values():
        # value = input(f"How much income from {value}?")
        total += float(value)
    return total

def income_modifier(key, money):
    global total
    
    if key in income:
        total -= income.get(key)
        income[key] = money
        total += money
    else:
        print("Please input the income value you wish to change: ")
    return total