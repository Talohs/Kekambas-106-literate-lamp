expense = {
        'Tax': '150',
        'Insurance': '100',
        'Electric': '0',
        'Water':  '0',
        'Sewer':  '0',
        'Gas': '0',
        'HOA fees': '0',
        'Lawn/Snow': '0',
        'Vacancy': '100',
        'Repairs': '100',
        'Capital Expenses(CapEx)': '100',
        'Property Management': '200',
        'Mortgage': '860'
    }
total = 0.0
def expense_calculation():
    

    global total
    for value in expense.values():
        # value = input(f"How much income from {value}?")
        total += float(value)
    return total

def expense_modifier(key, money):
    global total
    
    if key in expense:
        total -= expense.get(key)
        expense[key] = money
        total += float(money)
    else:
        print("Please input the expense value you wish to change: ")
    return total