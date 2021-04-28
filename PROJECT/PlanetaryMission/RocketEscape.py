import urllib.request
from html_table_parser import HTMLTableParser
import math

# Read website content
def url_get_contents(url):
    req = urllib.request.Request(url=url)
    f = urllib.request.urlopen(req)
    return f.read()

# return data for global use
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

    rocket_mass = { "pigeon 10": 549054, "pigeon 10 heavy": 549054, "big fat rocket": 3401942, 
                    "air captain": 14220, "air captain heavy": 733000,
                    }

    rocket_thrust = {"pigeon 10": 7607000, "pigeon 10 heavy": 934000, "big fat rocket": 9900000, 
                    "air captain": 110000, "air captain heavy": 240000,
                    }
    
    return [solarSystemData, row_dict, col_dict, rocket_mass, rocket_thrust]

# Initialise Global Variables
BURNING_CONSTANT = 43919.97979797
MASS_CONV = 1000000000000000000000000
G = 0.0000000000667430
SOLAR_SYSTEM_DATA = dataInitialisation()[0]
ROW_DICT = dataInitialisation()[1]
COL_DICT = dataInitialisation()[2]
ROCKET_MASS = dataInitialisation()[3]
ROCKET_THRUST = dataInitialisation()[4]

# checking input data for planets
def printCheck():
    col = (input("Enter the name of planet: ")).lower()
    row = (input("Enter information you want: ")).lower()
    print("--> " + str(SOLAR_SYSTEM_DATA[ROW_DICT[row]][COL_DICT[col]]))

# Rocket class with necessary attributes
class Rocket():
    def __init__(self, rocketName, payload, fuelKgs):
        self.name = rocketName.lower()
        self.payload = payload
        self.fuelKgs = fuelKgs
        self.massKgs = ROCKET_MASS[self.name]
        self.totalMass = self.massKgs + self.payload + self.fuelKgs
        self.thrust = ROCKET_THRUST[self.name]

    def getName(self):
        return self.name

    def getFuel(self):
        return self.fuelKgs

    def getMass(self):
        return self.massKgs

    def getPayload(self):
        return self.payload

    def getTotalMass(self):
        return self.totalMass

    def getThrust(self):
        return self.thrust

    def showDetails(self):
        print()
        print("Name of Rocket: " + self.getName().capitalize())
        print("Fuel (in Kgs): " + str(self.getFuel()))
        print("Mass of Rocket (in Kgs): " + str(self.getMass()))
        print("Payload (in Kgs): " + str(self.getPayload()))
        print("Total Mass (in Kgs): " + str(self.getTotalMass()))
        print("Thrust " + self.getName().capitalize() + " can produce: " + str(self.getThrust()))
        print()

class Journey():
    def __init__(self, fromPlanet, toPlanet, rocket):
        self.fromPlanet = fromPlanet.lower()
        self.toPlanet = toPlanet.lower()
        self.rocket = rocket
        self.tripDistance = abs(float(SOLAR_SYSTEM_DATA[ROW_DICT["distance from sun"]][COL_DICT[self.fromPlanet]]) - float(SOLAR_SYSTEM_DATA[ROW_DICT["distance from sun"]][COL_DICT[self.toPlanet]]))

    def getFromPlanet(self):
        return self.fromPlanet

    def getToPlanet(self):
        return self.toPlanet

    def getRocket(self):
        return self.rocket

    def getTripDistance(self):
        return self.tripDistance

    def showDetails(self):
        print()
        print("From Planet: " + str(self.fromPlanet).capitalize())
        print("To Planet: " + str(self.toPlanet).capitalize())
        print("Trip Distance (in Kms): " + str((self.tripDistance)*1000000))
        print("With the Rocket: " + str(self.rocket.getName().capitalize()))
        print("Thrust " + self.rocket.getName().capitalize() + " can produce: " + str(self.rocket.getThrust()))
        print()

# to calculate if mission successful or not
def calculation(rocket, journey):
    
    thrust = rocket.getThrust()
    
    # force experienced while launching = thrust - (mass * g1)
    g1 = float(SOLAR_SYSTEM_DATA[ROW_DICT["gravity"]][COL_DICT[journey.fromPlanet]])
    launchingForce = abs(thrust - (rocket.getTotalMass() * g1))
    print("Launching Force in N:" +  str(launchingForce)) # in Newtons
    
    # acceleration = launchingForce / mass
    acclr = launchingForce/(rocket.getTotalMass())
    print("Acceleration while Launching in m/s^2: " + str(acclr)) # acclrn in m/s^2

    #  t1 = (v1 - 0) / a;  ## v1 = escape velocity
    t1 = (float(SOLAR_SYSTEM_DATA[ROW_DICT["escape velocity"]][COL_DICT[journey.fromPlanet]])) / acclr
    print("Time taken to enter space: " + str(t1 * 60) + " seconds")

    # fuel left = initial fuel - (t1 *  some const value )
    fuel_left = rocket.getFuel() - (t1 * BURNING_CONSTANT)
    print("Fuel Left in the rocket: " + str(fuel_left))
    print()

    rocket.totalMass = rocket.totalMass - t1 * BURNING_CONSTANT
    
    #force experienced while landing = thrust - (new mass * g2)
    g2 = float(SOLAR_SYSTEM_DATA[ROW_DICT["gravity"]][COL_DICT[journey.toPlanet]])
    landingForce = thrust - (rocket.getTotalMass() * g2)
    print("Landing Force in N: " + str(landingForce))

    # a = F/m
    landAcclr = abs(landingForce / rocket.totalMass)
    print("Acceleration while Landing in m/s^2: " + str(landAcclr))
    
    # Orbital Velocity is different for each planet calculated as:  v = SQRT(G*M/R)
    mass = float(SOLAR_SYSTEM_DATA[ROW_DICT["mass"]][COL_DICT[journey.toPlanet]])
    radius = float(SOLAR_SYSTEM_DATA[ROW_DICT["diameter"]][COL_DICT[journey.toPlanet]]) / 2
    orbitVel = math.sqrt((G * (mass*MASS_CONV)/36) / radius) / 10000
    print("Orbit Velocity for landing planet: " + str(orbitVel))

    print()
    #t2 = orbital velocity / a
    t2 = (orbitVel / landAcclr)
    print("Time taken in landing: " + str(t2*60) + " seconds")
    
    # fuel left = initial fuel - (t1 *  some const value )
    fuel_left = fuel_left - (t2 * BURNING_CONSTANT)
    print("Fuel Left after Landing: " + str(fuel_left))
    print()

    return(fuel_left)

if __name__ == "__main__":
    # only for testing, this does not represent the package
    #printCheck()
    name = "big fat rocket"
    payload = 44000000
    fuel = 75000
    fromPlanet = "Earth"
    toPlanet = "Mars"

    rocket1 = Rocket(name, payload, fuel)
    rocket1.showDetails()

    journey1 = Journey(fromPlanet, toPlanet, rocket1)
    journey1.showDetails()

    fuelLeft = calculation(rocket1, journey1)

    if (fuelLeft >= 100):
        print("MISSION WILL BE SUCCESSFULL!")
    else:
        print("MISSION FAILED!!!")