total_cost = float(input("enter the cost of your dream house: "))

annual_salary = float(input("enter your annual salary: "))

portion_saved = float(input("enter the portion of salary to be saved, as a decimal: "))

semi_annual_raise = float(input("enter your semi-annual salary raise, as a decimal: "))

monthly_salary = annual_salary/12
portion_down_payment = 0.25
current_savings = 0
r = 0.04    #annual return 

down_payment = total_cost*portion_down_payment
month_count = 0

while(current_savings < down_payment):
    current_savings += (current_savings*r/12 + monthly_salary*portion_saved)
    month_count += 1 
    if(month_count%6 == 0):
        monthly_salary *= (1+semi_annual_raise)
        
print("you will need to save for",month_count,"months")