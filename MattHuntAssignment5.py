investment = float(input("Please enter your current investment amount "))
annualInterest = float(input("Please enter your annual interest rate "))
count = 0
balance = investment
currentBalance = 0
while (balance <= investment * 2):
    currentBalance = investment * (annualInterest / 100)
    balance += currentBalance
    count += 1
print("The number of years is ", count)
