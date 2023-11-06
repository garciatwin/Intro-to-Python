

print("Welcome to the Compound Interest Calculator!")
#adding string for the person to enter info on calculator
P = float(input("Please enter the initial amount of your investment: "))
r = float(input("Please enter the interest rate(e.g., '.02' for 2% interest):  "))
t = float(input("Please enter the number of years for the investment: "))
n = float(input("Please enter the number of compounding per year: "))
#using formula for compound interest
new_balance = P*(pow((1+(r/n)), n*t))
#printing solution, ":,." used for integers
print("original investment:", "${:,.2f}".format(round(float(P), 2)))
print("interest earned:", "${:,.2f}".format(round(float(new_balance-P), 2)))
print("The final amount will be ", "{:,.2f}".format(round(float(new_balance), 2)))


