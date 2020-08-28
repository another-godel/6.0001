total_cost = float(input("enter the cost of your dream house: "))

annual_salary = float(input("enter your annual salary: "))

portion_saved = float(input("enter the portion of salary to be saved, as a decimal: "))

portion_down_payment = 0.25
current_savings = 0
r = 0.04    #annual return 

down_payment = total_cost*portion_down_payment
month_count = 0

while(current_savings < down_payment):
    month_count += 1 
    current_savings += (current_savings*r/12 + (annual_salary/12)*portion_saved)

print("you will need to save for",month_count,"months")
