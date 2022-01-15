import requests, json

print("Welcome to the Weather Report Program!")
#Next is the city function that will ask for the user to put in either 1 or 2 depending on which way they want to get the weather
def City():
    area = ''
    while area != '1' and area != '2':
	    area = input("Please enter 1 if you would like to get your current weather by using your city name, or enter 2 if you would like to get your current weather by using your zip code: ")

    return area
#Next is the main funciton that will have the user put the specific name or zip code and make the complete URL
def main():
    if __name__ == '__main__':
        location = City()

        if location == '1':
            choice = input("Please enter your city name: ")
        
        elif location == '2':
            choice = input("Please enter your zip code: ")
        
        apiKey = "ff8f089b9e8f2cb55f436d3caaecc7dc"

        baseUrl = "http://api.openweathermap.org/data/2.5/weather?"

        completeUrl = (baseUrl + "appid=" + apiKey + "&q=" + choice)
#Next is the try block for the request from the web source or else it will show an error
    try:
        response = requests.get(completeUrl)
        response.raise_for_status()
    
    except requests.HTTPError as error:
        print(error, "Unsuccessfully connected to the weather service, please enter a valid city name or zip code.")

    else:
        print("Successfully connected to the weather service")
        print(response)

        x = response.json()

        if x["cod"] != "404":
            Information = x["main"]
            temp = Information["temp"]
            temp_min = Information["temp_min"]
            temp_max = Information["temp_max"]
            feels_like = Information["feels_like"]
            humidity = Information["humidity"]
            temp = (temp - 273.5)*1.8 + 32
            temp_min = (temp_min - 273.5)*1.8 + 32
            temp_max = (temp_max - 273.5)*1.8 + 32
            feels_like = (feels_like - 273.5)*1.8 + 32

            print("The temperature for", choice, "is", temp, "degrees fahrenheit, the minimum temperature is", temp_min, "degrees fahrenheit, the maximum temperature is", temp_max, "degrees fahrenheit, it feels like", feels_like,"degrees fahrenheit, and the humidity is", humidity,"%")
#Finally, next is the question asking the user if they would like to enter a new location
main()
print('Do you want to enter a new location? (yes or no)')
newChoice = input()
if newChoice == "no" or newChoice == 'n':
	print("Thank you for using the weather report program!")

elif newChoice == 'yes' or newChoice == 'y':
	main()
	newChoice == "no" or newChoice == 'n'
    