actual_cost = float(input("enter the actual cost: "))
sales_cost = float(input("enter the sales cost: "))

if (sales_cost > actual_cost):
    amount = sales_cost - actual_cost
    print("profit: ", amount) 

else: 
    print("No Profit!!!")