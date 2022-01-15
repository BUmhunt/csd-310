#choice = int(input('Please enter "1" if you would like to get your current weather by using your city name, or enter "2" if you would like to get your current weather by using your zip code: '))

#if choice == 1:
    #cityName = input("Please enter your city name: ")
#elif choice == 2:
    #zipCode = input("Please enter your zip code: ")
#else:
    #print("Please enter either '1' or '2'")

#def cityName():
    #input("Please enter your city name: ")

#def zipCode():
    #input("Please enter your zip code: ")

#choice = '1' or '2'
#while choice == '1':
	#cityName()
    
	#print('Do you want to play again? (yes or no)')
	#playAgain = input()
	#if playAgain == "no" or playAgain == 'n':
		#print("Thanks for playing!")

import requests, json

#print("Welcome to the weather report program.  This program will provide you with current weather infromation of any given city or zip code.")

#apiKey = "ff8f089b9e8f2cb55f436d3caaecc7dc"

#baseUrl = "http://api.openweathermap.org/data/2.5/weather?"

#cityName = input("Please enter your city name: ")

#completeUrl = baseUrl + "appid=" + apiKey + "&q=" + cityName

#r = requests.get(completeUrl)

#rJson = r.json()



print("Welcome to the weather report program.  This program will provide you with current weather infromation of any given city or zip code.")

choice = 1 or 2

while(choice == 1):
    choice = int(input('Please enter "1" if you would like to get your current weather by using your city name, or enter "2" if you would like to get your current weather by using your zip code: '))

    if (choice == 1):
        city = input("Please enter your city name: ")

    elif (choice == 2):
        zipCode = input("Please enter your zip code: ")
