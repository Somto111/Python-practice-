#Tip calculator
print("Welcome to the tip calculator!")
Bill =float(input("What was the total bill?$"))
Percentage =int(input("What percentage tip would you like to give? 10,12,or 15?$"))
No_of_people =int(input("How many people are to split the bill?"))
New_percentage =Percentage/100
Tip = (Bill*New_percentage)
New_bill = Bill+Tip
Amount_to_be_paid = round(New_bill/No_of_people, 2)
print(f"Each person should pay ${Amount_to_be_paid}")