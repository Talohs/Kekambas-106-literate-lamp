import re

total = 0.0
return_on_invest = {
        'down payment': '0',
        'closing costs': '0',
        'rehab budget': '0',
        'miscellaneous': '0',
    } 

def roi_calculation():

    global total
    flag = True
    for inv, value in return_on_invest.items():
        value = input(f"How much investment from {inv}?")
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
                    value = input("Please input the income numeric value you wish to change: ")
                    continue
                else:
                    break
            total += float(value)
    return total

def roi_modifier(key, money):
    global total
    
    total -= float(return_on_invest.get(key))
    return_on_invest[key] = money
    total += float(money)
    
    return total