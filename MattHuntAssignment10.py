import os

Directory = input("Please enter the name of the directory: ")
File = input("Please enter the name of the file: ")
Name = input("What is your name? ")
Address = input("What is your address? ")
phoneNumber = input("What is your phone number? ")

fName = open(File, 'x')

fName = open(File, 'w')

fName.write(Name)
fName.write(Address)
fName.write(phoneNumber)
fName.close()

fName = open(File, 'r')
print(fName.read())