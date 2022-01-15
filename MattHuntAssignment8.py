class Vehicle:
    def __init__(self, make, model, color, fuelType, options):
        self.make = make
        self.model = model
        self.color = color
        self.fuelType = fuelType
        options = options.lower()
        if (options == "backup camera" , options == "remote start" , options == "bluetooth" , options == "leather seats" , options == "heated seats" , options == "heated steering wheel" , options == "navigation" , options == "tinted windows"):
            self.options = options
        else:
            self.options = "Invalid Option"
        
 
    def getMake(self):
        return self.make
    
    def getModel(self):
        return self.model

    def getColor(self):
        return self.color

    def getFuelType(self):
        return self.fuelType

    def getOptions(self):
        return self.options

class Car(Vehicle):
    def __init__(self, make, model, color, fuelType, options, enigneSize, numDoors):
        super().__init__(make, model, color, fuelType, options) 
        self.enigneSize = enigneSize
        self.numDoors = numDoors

    def getEngineSize(self):
        return self.enigneSize

    def getNumDoors(self):
        return self.numDoors

class Pickup(Vehicle):
    def __init__(self, make, model, color, fuelType, options, cabStyle, bedLength):
        super().__init__(make, model, color, fuelType, options)
        self.cabStyle = cabStyle
        self.bedLength = bedLength

    def getCabStyle(self):
        return self.cabStyle

    def getBedLength(self):
        return self.bedLength

print("Please enter the following information as attributes for a car:")
Lambo = Car(input("Enter the make of the car: "), input("Enter the model of the car: "), input("Enter the color of the car: "), input("Enter the fuel type of the car: "), input("Choose any of the following options to be added to the car: Backup Camera, Remote Start, BlueTooth, Leather Seats, Heated Seats, Heated Steering Wheel, Navigation, Tinted Windows: "), input("Enter the size of the car's engine: "), input("Enter how many doors the car has: "))
print("Now Enter the Pickup:")

F150 = Pickup(input("Enter the make of the pickup: "), input("Enter the model of the pickup: "), input("Enter the color of the pickup: "), input("Enter the fuel type of the pickup: "), input("Choose any of the following options to be added to the pickup: Backup Camera, Remote Start, BlueTooth, Leather Seats, Heated Seats, Heated Steering Wheel, Navigation, Tinted Windows: "), input("Enter the cab style that the pickup has: "), input("Enter the length of the bed that the pickup has: "))
print("Shown below is the car and the pickup that were created:")

print(Lambo.make, Lambo.model, "that is", Lambo.color, "and takes" , Lambo.fuelType, "fuel, and has", Lambo.options, ", a", Lambo.enigneSize, "engine, and", Lambo.numDoors, "doors.")
print(F150.make, F150.model, "that is", F150.color, "and takes", F150.fuelType, "fuel, and has", F150.options, ", a/an", F150.cabStyle, "cab, and a", F150.bedLength, "bed.")
flag = 1
auto = ""

while(flag == 1):
    flag = int(input("To enter another vehicle, enter 1, to exit enter 0: "))

    if (flag == 1):
        auto = input("Car or Pickup? ")
            
        if (auto.lower() == "car"): 
            print("Please enter the following information as attributes for a car:")
            Lambo = Car(input("Enter the make of the car: "), input("Enter the model of the car: "), input("Enter the color of the car: "), input("Enter the fuel type of the car: "), input("Choose any of the following options to be added to the car: Backup Camera, Remote Start, BlueTooth, Leather Seats, Heated Seats, Heated Steering Wheel, Navigation, Tinted Windows: "), input("Enter the size of the car's engine: "), input("Enter how many doors the car has: "))
            print(Lambo.make, Lambo.model, "that is", Lambo.color, "and takes" , Lambo.fuelType, "fuel, and has", Lambo.options, ", a", Lambo.enigneSize, "engine, and", Lambo.numDoors, "doors.")

        elif(auto.lower() == "pickup"): 
            print("Please enter the following information as attributes for a pickup:")
            F150 = Pickup(input("Enter the make of the pickup: "), input("Enter the model of the pickup: "), input("Enter the color of the pickup: "), input("Enter the fuel type of the pickup: "), input("Choose any of the following options to be added to the pickup: Backup Camera, Remote Start, BlueTooth, Leather Seats, Heated Seats, Heated Steering Wheel, Navigation, Tinted Windows: "), input("Enter the cab style that the pickup has: "), input("Enter the length of the bed that the pickup has: "))
            print(F150.make, F150.model, "that is", F150.color, "and takes", F150.fuelType, "fuel, and has", F150.options, ", a/an", F150.cabStyle, "cab, and a", F150.bedLength, "bed.")

    elif (flag == 0):
        print("Thank you, have a nice day.")