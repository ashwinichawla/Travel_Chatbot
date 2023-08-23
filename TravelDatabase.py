import requests

# first dictionary will be states to travel to, key = state, value = another dictionary consists of the key's
# city, latitude, and longitude
# second dictionary will be the weather associated with a tourist area within the state

api_key = '********************************'

placestotravel = {'Alabama': {'city': 'Huntsville', 'lat': 34.7304, 'lon': 86.5861},
                  'Alaska': {'city': 'Anchorage', 'lat': 61.2176, 'lon': 149.8997},
                  'Arizona': {'city': 'Phoenix', 'lat': 33.4484, 'lon': 112.0740},
                  'Arkansas': {'city': 'Little Rock', 'lat': 34.7445, 'lon': 92.2880},
                  'California': {'city': 'Los Angeles', 'lat': 34.0522, 'lon': 118.2437},
                  'Colorado': {'city': 'Denver', 'lat': 39.7392, 'lon': 104.9903},
                  'Connecticut': {'city': 'Greenwich', 'lat': 41.0262, 'lon': 73.6282},
                  'Delaware': {'city': 'Wilmington', 'lat': 39.7447, 'lon': 75.5484},
                  'Florida': {'city': 'Miama', 'lat': 25.7617, 'lon': 80.1918},
                  'Georgia': {'city': 'Atlanta', 'lat': 33.7488, 'lon': 84.3877},
                  'Hawaii': {'city': 'Honolulu', 'lat': 21.3099, 'lon': 157.8581},
                  'Idaho': {'city': 'Boise', 'lat': 43.6150, 'lon': 43.6150},
                  'Illinois': {'city': 'Chicago', 'lat': 41.8781, 'lon': 87.6298},
                  'Indiana': {'city': 'Indianapolis', 'lat': 39.7684, 'lon': 86.1581},
                  'Iowa': {'city': 'Des Moines', 'lat': 41.5868, 'lon': 93.6250},
                  'Kansas': {'city': 'Wichita', 'lat': 37.6872, 'lon': 97.3301},
                  'Kentucky': {'city': 'Louisville', 'lat': 38.2527, 'lon': 85.7585},
                  'Louisiana': {'city': 'New Orleans', 'lat': 29.9511, 'lon': 90.0715},
                  'Maine': {'city': 'Bar Harbor', 'lat': 44.3876, 'lon': 68.2039},
                  'Maryland': {'city': 'Baltimore', 'lat': 39.2904, 'lon': 76.6122},
                  'Massachusetts': {'city': 'Boston', 'lat': 42.3601, 'lon': 71.0589},
                  'Michigan': {'city': 'Ann Arbor', 'lat': 42.2808, 'lon': 83.7430},
                  'Minnesota': {'city': 'Minneapolis', 'lat': 44.9778, 'lon': 93.2650},
                  'Mississippi': {'city': 'Jackson', 'lat': 32.2988, 'lon': 90.1848},
                  'Missouri': {'city': 'St. Louis', 'lat': 38.6270, 'lon': 90.1994},
                  'Montana': {'city': 'Great Falls', 'lat': 47.5053, 'lon': 111.3008},
                  'Nebraska': {'city': 'Omaha', 'lat': 41.2565, 'lon': 95.9345},
                  'Nevada': {'city': 'Las Vegas', 'lat': 36.1716, 'lon': 115.1391},
                  'New Hampshire': {'city': 'Machester', 'lat': 42.9956, 'lon': 71.4548},
                  'New Jersey': {'city': 'Atlantic City', 'lat': 39.3643, 'lon': 74.4229},
                  'New Mexico': {'city': 'Albuquerque', 'lat': 35.0844, 'lon': 106.6504},
                  'New York': {'city': 'Manhattan', 'lat': 40.7831, 'lon': 73.9712},
                  'North Carolina': {'city': 'Charlotte', 'lat': 35.2271, 'lon': 80.8431},
                  'North Dakota': {'city': 'Fargo', 'lat': 46.8772, 'lon': 96.7898},
                  'Ohio': {'city': 'Cleveland', 'lat': 41.4993, 'lon': 81.6944},
                  'Oklahoma': {'city': 'Oklahoma City', 'lat': 35.4676, 'lon': 35.4676},
                  'Oregon': {'city': 'Portland', 'lat': 45.5152, 'lon': 122.6784},
                  'Pennsylvania': {'city': 'Philadelphia', 'lat': 39.9526, 'lon': 75.1652},
                  'Rhode Island': {'city': 'Providence', 'lat': 41.8240, 'lon': 71.4128},
                  'South Carolina': {'city': 'Charleston', 'lat': 32.7765, 'lon': 79.9311},
                  'South Dakota': {'city': 'Sioux Falls', 'lat': 43.5460, 'lon': 96.7313},
                  'Tennessee': {'city': 'Nashville', 'lat': 36.1627, 'lon': 86.7816},
                  'Texas': {'city': 'Houston', 'lat': 29.7604, 'lon': 95.3698},
                  'Utah': {'city': 'Salt Lake City', 'lat': 40.7608, 'lon': 111.8910},
                  'Vermont': {'city': 'Burlington', 'lat': 44.4759, 'lon': 73.2121},
                  'Virginia': {'city': 'Richmond', 'lat': 37.5407, 'lon': 77.4360},
                  'Wisconsin': {'city': 'Milwaukee', 'lat': 43.0389, 'lon': 87.9065},
                  'Wyoming': {'city': 'Cheyenne', 'lat': 41.1400, 'lon': 104.8202}}


def geo_call(city, state):
    """Calls on geo spatial api to provide current data."""
    geo_response = requests.get(
        f'http://api.openweathermap.org/geo/1.0/direct?q={city},{state},US&limit=5&appid={api_key}')
    # check if the response was unsuccessful
    if not geo_response.ok:
        print("Error: could not retrieve your local weather.")
        exit(1)
    # grab the json data for the location
    location_data = geo_response.json()
    # check if the user didn't provide a valid location
    if len(location_data) == 0:
        print("Error: city or state is not a valid entry.")
        exit(1)
    # grab the latitude and longitude from the location data request
    location = location_data[0]
    # store the latitudes and longitudes in separate variables that use the larger location object
    return location['lat'], location['lon']


def weather_call(lat, lon):
    """Calls on weather api to provide current data."""
    weather_response = requests.get(
        f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&units=imperial&appid={api_key}')
    # check if status was unsuccessful
    if not weather_response.ok:
        print("Error: could not retrieve your local weather.")
        exit(1)
    # grab the json data for the location
    weather_data = weather_response.json()
    # return the current temperature
    return weather_data['main']['temp']


# first hard code coordinates
# next call the weather of the city

# https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API key}

print("=================================")
print("| Welcome to the Travel Chatbot |")
print("=================================")

city_value = input("Hello, where are you located? Please enter your city: ")
state_value = input("Please enter your state: ")

latitude, longitude = geo_call(city_value, state_value)

weather_retrieved = weather_call(latitude, longitude)
print("The current weather at your location is:", weather_retrieved)
