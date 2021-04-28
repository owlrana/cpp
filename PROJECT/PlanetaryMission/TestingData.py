# Library for opening url and creating requests
import urllib.request

# pretty-print python data structures
from pprint import pprint

# for parsing all the tables present on the website
from html_table_parser import HTMLTableParser

# for converting the parsed data in a
# pandas dataframe
import pandas as pd


# Opens a website and read its
# binary contents (HTTP Response Body)
def url_get_contents(url):

	# Opens a website and read its
	# binary contents (HTTP Response Body)

	#making request to the website
	req = urllib.request.Request(url=url)
	f = urllib.request.urlopen(req)

	#reading contents of the website
	return f.read()

# defining the html contents of a URL.
xhtml = url_get_contents('https://nssdc.gsfc.nasa.gov/planetary/factsheet/').decode('utf-8')

# Defining the HTMLTableParser object
p = HTMLTableParser()

# feeding the html contents in the HTMLTableParser object
p.feed(xhtml)

# Now finally obtaining the data of the table required
#pprint(p.tables[0])
solarSystemData = p.tables[0]

# row = 0 for planet name row
#row = 0
# col = 1,2,3,4,... for name of planets
#col = 1
#for i in range(1,10):
#	print(solarSystemData[row][i])

row_dict = {"mass": 1, "diameter": 2, "density": 3, "gravity": 4, 
			"escape velocity": 5, "rotation period": 6,
			"length of day": 7, "distance from sun": 8,
			"perihelion": 9, "aphelion": 10,
			"orbital period": 11, "orbital velocity": 12,
			"orbital inclination": 13, "orbital eccentricity": 14,
			"obliquity to orbit": 15, "mean temperature": 16,
			"surface pressure": 17, "number of moons": 18,
			"ring system?": 19, "global magnetic field?": 20,
			}

col_dict = {"mercury": 1, "venus": 2, "earth": 3, "moon": 4, "mars": 5, "jupiter": 6,
			"saturn": 7, "uranus": 8, "neptune": 9, "pluto": 10,
			}

print()
for key, value in col_dict.items():
	print(key, end=", ")
print("", end= "\n\n")
for key, value in row_dict.items():
	print(key, end=", ")

col_input = input("Enter the planet name: ")
row_input = input("Enter the data key: ")

print(solarSystemData[row_dict[row_input]][col_dict[col_input]])
# can later do print(solarSystemData[row_dict["mass"]][col_dict["mercury"]])

# converting the parsed data to dataframe
#print("\n\nPANDAS DATAFRAME\n")
#print(pd.DataFrame(p.tables[0]))