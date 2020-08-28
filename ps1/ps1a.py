print("enter the cost of your dream house: ")
total_cost = float(input())

print("enter your annual salary: ")
annual_salary = float(input())

print("enter the portion of salary to be saved, as decimal: ")
portion_saved = float(input())

portion_down_payment = 0.25
current_savings = 0
r = 0.04    #annual return 

down_payment = total_cost*portion_down_payment
month_count = 0

while(current_savings < down_payment):
    month_count += 1 
    current_savings += (current_savings*r/12 + (annual_salary/12)*portion_saved)

print("you will need to save for",month_count,"months")
