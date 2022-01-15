class Vehicle:
    def __init__(self, make, model, color, fuelType, options):
        self.make = make
        self.model = model
        self.color = color
        self.fuelType = fuelType
        self.options = options

    def user_pickup(self):
        """
        docstring
        """
        pass

    def user_car(self):
        """
        docstring
        """
        pass
        
class Car(Vehicle):
    def __init__(self, make, model, color, fuelType, options, enigneSize, numDoors):
        self.enigneSize = enigneSize
        self.numDoors = numDoors

class Pickup(Vehicle):
    def __init__(self, make, model, color, fuelType, options, cabStyle, bedLength):
        self.cabStyle = cabStyle
        self.bedLength = bedLength

print("Please enter the following information as attributes for a car:")

car_make = input("Enter the make of the car: ")
car_model = input("Enter the model of the car: ")
car_color = input("Enter the color of the car: ")
car_fuelType = input("Enter the fuel type of the car: ")
car_options = input("Choose any of the following options to be added to the car: Backup Camera, Remote Start, BlueTooth, Leather Seats, Heated Seats, Heated Steering Wheel, Navigation, Tinted Windows: ")
car_engineSize = input("Enter the size of the car's engine: ")
car_numDoors = input("Enter how many doors the car has: ")

print("Please enter the following information as attributes for a pickup: ")

pickup_make = input("Enter the make of the pickup: ")
pickup_model = input("Enter the model of the pickup: ")
pickup_color = input("Enter the color of the pickup: ")
pickup_fuelType = input("Enter the fuel type of the pickup: ")
pickup_options = input("Choose any of the following options to be added to the pickup: Backup Camera, Remote Start, BlueTooth, Leather Seats, Heated Seats, Heated Steering Wheel, Navigation, Tinted Windows: ")
pickup_cabStyle = input("Enter the cab style that the pickup has: ")
pickup_bedLength = input("Enter the length of the bed that the pickup has: ")

Car = Vehicle(car_make, car_model, car_color, car_fuelType, car_options, car_engineSize, car_numDoors)
Pickup = Vehicle(user_pickup(pickup_make, pickup_model, pickup_color, pickup_fuelType, pickup_options, pickup_cabStyle, pickup_bedLength))

print("Shown below is the car and the pickup that were created:")

print("The car is a", car_color, car_make, car_model, "with", car_fuelType, "fuel and (a)", car_options, "with a", car_engineSize, "engine, and", car_numDoors, "doors")

Pickup.user_pickup()
