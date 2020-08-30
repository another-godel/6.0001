annual_salary = float(input("enter your annual salary: "))

total_cost = 1000000
semi_annual_raise = .07
monthly_salary = annual_salary/12
portion_down_payment = 0.25
r = 0.04    #annual return 

down_payment = total_cost*portion_down_payment
month = 36

low = 0
high = 10000
ans = int((low + high)/2)
portion_saved = ans/10000

def total_savings(salary ,portion):
    current_savings = 0
    i = 0   #month count
    while(i < 36):
        current_savings += (current_savings*r/12 + salary*portion)
        i += 1
        if(i%6 == 0):
            salary *= (1 + semi_annual_raise)
    return current_savings

times = 0
while(abs(total_savings(monthly_salary, portion_saved) - down_payment) > 100):
    times +=1
    if(times > 1000):
        break
    if(total_savings(monthly_salary, portion_saved) < down_payment):
        low = ans
    else:
        high = ans
    ans = int((low + high)/2)
    portion_saved = ans/10000

    print("times:", times)
    print("low =", low, "high =", high, "ans =", ans)
    print("difference", abs(total_savings(monthly_salary, portion_saved) - down_payment), "\n")

print("optimal saving rate is", str(portion_saved*100) + "%")
        
