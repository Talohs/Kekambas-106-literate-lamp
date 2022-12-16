def income_calculation():
    income = {
        'rental':'2000',
        'laundry':'0',
        'storage':'0',
        'misc':'0',
    } 

    
    total = 0.0
    for value in income.values():
        # value = input(f"How much income from {value}?")
        total += float(value)
    return total
    
