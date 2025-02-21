


Salary = int(input("Please enter Nabiha's salary: "))
Month = input("Please enter the month of Nabih's salary: ")
Psavings = int(input("Please enter the saving percentage:"))
Prent = int(input("Please enter the saving percentage:"))
Pelectricity = int(input("Please enter the saving percentage:"))

Savings = (Salary*Psavings)/100
Rent = (Salary*Prent)/100
Electricity = (Salary*Pelectricity)/100

print("The amount of savings is: "+str(Savings))
print("The amount of rent is: "+str(Rent))
print("The amount of savings is: "+str(Electricity))

Expenses = Savings + Rent + Electricity
print("The total amount of the expenses: "+str(Expenses))

Remainder = Salary-Expenses
print("The Remainder from salary is: "+str(Remainder))
