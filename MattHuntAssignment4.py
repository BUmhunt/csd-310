print("Welcome to the fiber optic calculation program")
companyName = input("What is your company name? ")
numberFeet = int(input("How many feet of fiber optic will be installed? "))
fiberCost = .87
bulkDiscount1 = .80
bulkDiscount2 = .70
bulkDiscount3 = .50
bulkFeet1 = 100
bulkFeet2 = 250
bulkFeet3 = 500

if (numberFeet > bulkFeet1 and numberFeet < bulkFeet2):
    print("For the company", companyName, "the total price will be", (.80 * numberFeet))
elif (numberFeet > bulkFeet2 and numberFeet < bulkFeet3):
    print("For the company", companyName, "the total price will be", (.70 * numberFeet))
elif (numberFeet > bulkFeet3):
    print("For the company", companyName, "the total price will be", (.50 * numberFeet))
else: 
    print("For the company", companyName, "the total price will be", (.87 * numberFeet))