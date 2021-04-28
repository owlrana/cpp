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

    rocket_dict = { "falcon 9": 549054, "falcon 9 heavy": 549054, "sn 8": 3401942, 
                    "delta iv": 14220, "delta iv heavy": 733000,
                    }

    return [solarSystemData, row_dict, col_dict, rocket_dict]

# Store as Global Variables to use everywhere
SOLAR_SYSTEM_DATA = dataInitialisation()[0]
ROW_DICT = dataInitialisation()[1]
COL_DICT = dataInitialisation()[2]
ROCKET_DICT = dataInitialisation()[3]

def printCheck():
    col = (input("Enter the name of planet: ")).lower()
    row = (input("Enter information you want: ")).lower()
    print("--> " + str(SOLAR_SYSTEM_DATA[ROW_DICT[row]][COL_DICT[col]]))

class Rocket():
    def __init__(self, rocketName, payload, fuelKgs):
        self.name = rocketName.lower()
        self.payload = payload
        self.fuelKgs = fuelKgs
        self.massKgs = ROCKET_DICT[self.name]
        self.totalMass = self.massKgs + self.payload + self.fuelKgs

    def showDetails(self):
        print()
        print("Name of Rocket: " + str(self.name).capitalize())
        print("Fuel (in Kgs): " + str(self.fuelKgs))
        print("Mass of Rocket (in Kgs): " + str(self.massKgs))
        print("Payload (in Kgs): " + str(self.payload))
        print("Total MASS (in Kgs): " + str(self.totalMass))
        print()

if __name__ == "__main__":
    # only for testing, this does not represent the package
    printCheck()
    name = "FaLcOn 9 HEavY"
    payload = 5000
    fuel = 10000
    rocket1 = Rocket(name, payload, fuel)
    rocket1.showDetails()