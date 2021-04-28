import urllib.request
from html_table_parser import HTMLTableParser

# Opens a website and read its binary contents (HTTP Response Body)
def url_get_contents(url):

    # Opens a website and read its
    # binary contents (HTTP Response Body)

    #making request to the website
    req = urllib.request.Request(url=url)
    f = urllib.request.urlopen(req)

    #reading contents of the website
    return f.read()

# to initialise and return table, column and row information
def dataInitialisation():
    xhtml = url_get_contents('https://nssdc.gsfc.nasa.gov/planetary/factsheet/').decode('utf-8')
    p = HTMLTableParser()
    p.feed(xhtml)
    solarSystemData = p.tables[0]

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

    rocket_dict = { "Falcon 9": 549054, "Falcon 9 Heavy": 549054, "SN 8": 3401942, 
                    "Delta IV": 14220, "Delta IV Heavy": 733000,
                    }

    return [solarSystemData, row_dict, col_dict, rocket_dict]

# Store as Global Variables to use everywhere
SOLAR_SYSTEM_DATA = dataInitialisation()[0]
ROW_DICT = dataInitialisation()[1]
COL_DICT = dataInitialisation()[2]
ROCKET_DICT = dataInitialisation()[3]

def printCheck():
    col = input("Enter the name ofk planet: ")
    row = input("Enter information you want: ")
    print(SOLAR_SYSTEM_DATA[ROW_DICT[row]][COL_DICT[col]])

class Rocket():
    def __init__(self, rocketName, payload, fuelKgs):
        self.name = rocketName
        self.payload = payload
        self.fuelKgs = fuelKgs
        self.massKgs = ROCKET_DICT[rocketName]
        self.totalMass = self.massKgs + self.payload

    def change_name(self, new_name):
        self.name = new_name

if __name__ == "__main__":
    printCheck()