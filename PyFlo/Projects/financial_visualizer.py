#Checks whether the user's input is a numeric value or not, and keeps asking until it's a numeric value
#When the user finally inputs a valid value, then it also assigns it to whichever variable is being checked
def numeric(a):
    while str.isnumeric(a) == False:
        a = input("Enter an actual number:\n")
        if str.isnumeric(a) == True:
            break
    a = float(a)
    return a

#Calculates the percentage that the annual value (expenses) constitutes of your salary (total income)
def percentage(income, annual_value):
    a = round((annual_value / income) * 100, 2)
    return a

#Calculates monthly value to annual value
def monthly(a):
    a = round(a * 12, 2)
    return a

#Calculates weekly value to annual value
def weekly(a):
    a = round(a * 52, 2)
    return a

print("--------------------------------")
print("----- FINANCIAL VISUALIZER -----")
print("--------------------------------")

#Calculates the following:
salary = numeric(input("Annual Salary:"))
housing = monthly(numeric(input("Monthly Housing:")))
bills = monthly(numeric(input("Monthly Bills:")))
food = weekly(numeric(input("Weekly Food:")))
travel = numeric(input("Annual Travel:"))

#Calculates taxes
if salary >= 80001:
    tax = round(float(salary) * 0.20, 2) 
elif salary >= 40001:
    tax = round(float(salary) * 0.15, 2)
elif salary >= 10001:
    tax = round(float(salary) * 0.10, 2)
else:
    tax = round(float(salary) * 0.05, 2)

#Calculates extra (leftover money)
expenses = housing + bills + food + travel + tax

extra = salary - expenses

#Compute percentages for each
perc_housing = percentage(salary, housing)
perc_bills = percentage(salary, bills)
perc_food = percentage(salary, food)
perc_travel = percentage(salary, travel)
perc_tax = percentage(salary, tax)
perc_extra = percentage(salary, extra)

total = perc_bills + perc_extra + perc_food + perc_housing + perc_tax + perc_travel

#Calculates the length of whichever expense is inserted and subtracts it from the length of the number that represents the salary.
#Salary is the number we use, since that'll always be the largest number, if the input doesn't lie
def space(salary, data):
    a = ' '*(int(len(str(salary)))-int(len(str(data)))+1)
    return a

print(f"""
-----------------------------------------------------------------------
housing | $ {housing:.2f}{space(salary, housing)}| {perc_housing}%{space(total, perc_housing)} | {'#'*int(perc_housing)}
  bills | $ {bills:.2f}{space(salary, bills)}| {perc_bills}%{space(total, perc_bills)} | {'#'*int(perc_bills)}
   food | $ {food:.2f}{space(salary, food)}| {perc_food}%{space(total, perc_food)} | {'#'*int(perc_food)}
 travel | $ {travel:.2f}{space(salary, travel)}| {perc_travel}%{space(total, perc_travel)} | {'#'*int(perc_travel)}
    tax | $ {tax:.2f}{space(salary, tax)}| {perc_tax}%{space(total, perc_tax)} | {'#'*int(perc_tax)}
  extra | $ {extra:.2f}{space(salary, extra)}| {perc_extra}%{space(total, perc_extra)} | {'#'*int(perc_extra)}
-----------------------------------------------------------------------
""")