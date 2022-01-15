def displayIntro():
    print('''Welcome to the weather report program.  This program will provide you with current weather infromation of any given city or zip code''')
    print()

class Weather:
    def __init__(self, temperature, feelsLike, wind, humidity, uv, dewPoint, visibility):
       self.temperature = temperature
       self.feelsLike = feelsLike
       self.wind = wind
       self.humidity = humidity
       self.uv = uv
       self.dewPoint = dewPoint
       self.visibility = visibility

def chooseLocation():
    location = ''
    while location != '1' and location != '2':
	    choice = input('Please enter "1" if you would like to get your current weather by your city name, or enter "2" if you would like to get your current weather by your zip code: ')
	    location = input()

    return location

    if choice == 1:
        cityName = input("Please enter your city name")
    elif choice == 2:
        zipCode = input("Please enter your zip code")
    else:
        print("Please enter either '1' or '2'")