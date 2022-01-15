def mile_to_kilometer (m):
    return float(mile / .62137)
print("Welcome to the mile to kilometer conversion program.")
try:
    mile = float(input("Please enter the amount of miles driven: ")) 
except ValueError:
    print("That is not a proper mileage, please restart with a valid amount of miles driven: ")
else:
    print(mile, "miles equals", mile_to_kilometer (mile), "kilometers")     