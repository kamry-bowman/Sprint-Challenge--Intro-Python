import csv
import sys
# Create a class to hold a city location. Call the class "City". It should have
# fields for name, latitude, and longitude.


class City:
    def __init__(self, name, lat, lon):
        self.name = name
        self.lat = float(lat)
        self.lon = float(lon)

    def __str__(self):
        return '{}, {}, {}'.format(self.name, self.lat, self.lon)


# We have a collection of US cities with population over 750,000 stored in the
# file "cities.csv". (CSV stands for "comma-separated values".)
#
# In the body of the `cityreader` function, use Python's built-in "csv" module
# to read this file so that each record is imported into a City instance. Then
# return the list with all the City instances from the function.
# Google "python 3 csv" for references and use your Google-fu for other examples.
#
# Store the instances in the "cities" list, below.
#
# Note that the first line of the CSV is header that describes the fields--this
# should not be loaded into a City object.
cities = []


def cityreader(cities=[]):
    """reads from the 'cities.csv' file. For each city record, create a new City instance and add it to the `cities` list"""
       with open('cities.csv', newline='') as citiesFile:
            reader = csv.DictReader(citiesFile)
            # next(reader)
            for city in reader:
                name = city['city']
                lat = city['lat']
                lon = city['lng']
                cities.append(
                    City(name=name, lat=lat, lon=lon))
        return cities


cityreader(cities)


# STRETCH GOAL!
#
# Allow the user to input two points, each specified by latitude and longitude.
# These points form the corners of a lat/lon square. Pass these latitude and
# longitude values as parameters to the `cityreader_stretch` function, along
# with the `cities` list that holds all the City instances from the `cityreader`
# function. This function should output all the cities that fall within the
# coordinate square.
#
# Be aware that the user could specify either a lower-left/upper-right pair of
# coordinates, or an upper-left/lower-right pair of coordinates. Hint: normalize
# the input data so that it's always one or the other, then search for cities.
# In the example below, inputting 32, -120 first and then 45, -100 should not
# change the results of what the `cityreader_stretch` function returns.
#
# Example I/O:
#
# Enter lat1,lon1: 45,-100
# Enter lat2,lon2: 32,-120
# Albuquerque: (35.1055,-106.6476)
# Riverside: (33.9382,-117.3949)
# San Diego: (32.8312,-117.1225)
# Los Angeles: (34.114,-118.4068)
# Las Vegas: (36.2288,-115.2603)
# Denver: (39.7621,-104.8759)
# Phoenix: (33.5722,-112.0891)
# Tucson: (32.1558,-110.8777)
# Salt Lake City: (40.7774,-111.9301)

def normalize(lat1, lon1, lat2, lon2):
    """takes in (lat1, lon1) and (lat2, lon2) representing two coordinates creating a square.
    It normalizes these by making lat1, lon1 represent the NW corner of the square, and lat2 and
    lon2 represent the SE corner."""
    # check if lat1 is south of lat2
    if lat1 < lat2:
            # first point is south of second point, swap position
        lat1, lat2 = lat2, lat1
        lon1, lon2 = lon2, lon1

    if lon1 > lon2:
        # first point is SW of second point, so to normalize, swap longitudes:
        lon1, lon2 = lon2, lon1

    return (lat1, lon1, lat2, lon2)


def between(city, lat1, lon1, lat2, lon2):
    """determines if a given city object is between the square creates by
    (lat1, lon1) and (lat2, lon2)"""
    vertical_check = city.lat <= lat1 and city.lat >= lat2
    horizontal_check = city.lon >= lon1 and city.lon <= lon2
    return vertical_check and horizontal_check


def cityreader_stretch(lat1, lon1, lat2, lon2, cities=[]):
    try:
        lat1, lon1, lat2, lon2 = [float(val)
                                  for val in [lat1, lon1, lat2, lon2]]
    except ValueError:
        print('Arguments passed must be parsable lat/lon float values')

    lat1, lon1, lat2, lon2 = normalize(lat1, lon1, lat2, lon2)

    within = [city for city in cities if between(city, lat1, lon1, lat2, lon2)]
    return within


# program behaves differently if passed four arguments representing coords
arg_len = len(sys.argv)
if arg_len == 5:
    lat1, lon1, lat2, lon2 = sys.argv[1:5]
    answer = cityreader_stretch(lat1, lon1, lat2, lon2, cities)
    for city in answer:
        print(city)

else:
    for c in cities:
        print(c)
