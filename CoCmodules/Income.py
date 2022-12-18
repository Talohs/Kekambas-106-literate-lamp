import re

total = 0.0
income = {
        'rental':'0',
        'laundry':'0',
        'storage':'0',
        'misc':'0',
    } 

def income_calculation():

    global total
    flag = True
    for inc, value in income.items():
        value = input(f"How much income from {inc}?")
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

def income_modifier(key, money):
    global total

    total -= float(income.get(key))
    income[key] = money
    total += float(money)
    return total