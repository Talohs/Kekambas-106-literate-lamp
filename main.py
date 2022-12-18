from CoCmodules.Income import income_calculation as inca
from CoCmodules.Income import income_modifier as inmo
from CoCmodules.Expense import expense_calculation as exca
from CoCmodules.Expense import expense_modifier as exmo
from CoCmodules.CashonCashFlowROI import roi_calculation as roica
from CoCmodules.CashonCashFlowROI import roi_modifier as roimo
from dataclasses import dataclass
from dataclasses import field

@dataclass
class Return_On_Investment:
    income: str  = field(default_factory=str)
    expenses: str = field(default_factory=str)
    investments: str = field(default_factory=str)


    income = inca()
    expenses = exca()
    investments = roica()
    

def process_info():
    cash_flow = float(roi.income) - float(roi.expenses)
    month_cash_flow = cash_flow * 12
    return_on_investment = month_cash_flow / float(roi.investments)
    cocroi = return_on_investment  * 100
    return cocroi

def modify_info():
    while True:    
        mod_fact = input("Which factor would you like to change? Income, Expenses, Investments").lower()
        if mod_fact == 'income':
            print("Please enter rental, laundry, storage, or miscellaneous")
        if mod_fact == 'expenses':
            print("Please enter tax, insurance, utilities, Electric, Water, Sewer, gas, HOA fees, Lawn/Snow, Vacancy, Repairs, Capital Expenses, Property Management, Mortgage")
        if mod_fact == 'investments':
            print("Please enter down payment, closing cost, rehab budget, miscellaneous")
        if mod_fact in ['income','expenses', 'investments']:    
            while True:    
                mod_key = input("Which category would you like to change?").lower()
                mod_num = input("What should the new value be?").lower()
                if mod_fact == 'income' and mod_key in ['rental', 'laundry', 'storage', 'miscellaneous']:
                    roi.income  = inmo(mod_key, mod_num)
                    return
                else:
                    print("Please enter rental, laundry, storage, or miscellaneous")
                if mod_fact == 'expenses' and mod_key in ['Tax', 'Insurance', 'Utilities', 'Electric', 'Water', 'Sewer','gas', 'HOA fees', 
                                                        'Lawn/Snow', 'Vacancy', 'Repairs', 'Capital Expenses(CapEx)', 'Property Management', 'Mortgage']:
                    roi.expenses = exmo(mod_key, mod_num)
                    return
                else:
                    print("Please enter tax, insurance, utilities, Electric, Water, Sewer, gas, HOA fees, Lawn/Snow, Vacancy, Repairs, Capital Expenses, Property Management, Mortgage")
                if mod_fact == 'investments' and mod_key in ['down payment', 'closing cost', 'rehab budget', 'miscellaneous']:
                    roi.income  = roimo(mod_key, mod_num)
                    return
                else:
                    print("Please enter down payment, closing cost, rehab budget, miscellaneous")
        else:
            print("Please enter income, expenses, investments")   
            
roi = Return_On_Investment() 
user_str = ''          
while user_str != 'calculate':
    user_str = input("Would you like to change anything you input? modify, or calculate").lower().strip()
    if user_str == 'modify':
        modify_info()
        process_info()
    elif user_str == 'calulate':
        ret_inv = process_info()
        break

print(f"Future rental income will be ${roi.income}\nFuture rental expenses will be ${roi.expenses}\nFor the total investment of ${roi.investments}\nWill return a percentage of {ret_inv}%")


        

     



# income = inca()
# expenses = exca()
# cash_flow = float(income) - float(expenses)
# investments = roica()
# month_cash_flow = cash_flow * 12
# return_on_investment = month_cash_flow/float(investments)
# cocroi = float(return_on_investment) * 100 
# print(f"{cocroi:.2f}%")

