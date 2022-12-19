import re

expense = {
        'tax': '0',
        'insurance': '0',
        'electric': '0',
        'water':  '0',
        'sewer':  '0',
        'gas': '0',
        'hOA fees': '0',
        'lawn/Snow': '0',
        'vacancy': '0',
        'repairs': '0',
        'capital expenses': '0',
        'property management': '0',
        'mortgage': '0'
    }
total = 0.0
def expense_calculation():
    

    global total
    flag = True
    for exp, value in expense.items():
        value = input(f"How much expense from {exp}?")
        try:
            float(value)
        except:
            flag = False
        if flag:
            total += float(value)
        else:
            while True:
                value = re.sub(r'[0-9,46]','', value)
                try:
                    float(value)
                except:
                    value = input("Please input the expense numeric value you wish to change: ")
                    continue
                else:
                    break
            total += float(value)
    return total

def expense_modifier(key, money):
    global total
    
    total -= float(expense.get(key))
    expense[key] = money
    total += float(money)

    return total