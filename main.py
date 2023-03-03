import math
from queue import PriorityQueue

class Location:
    def __init__(self, name: str, lat: str, long: str, adjacencies: list) -> None:
        self.name = name
        self.lat = lat
        self.long = long
        self.adjacencies = adjacencies
        self.isVisited = False

locations = []

# Input: location name
# Output: the location object found in the global locations array or None
def getLocation(name: str) -> Location:
    for location in locations:
        if (location.name == name):
            return location

# Input: an array consisting of one line input
# Output: the same array, but without bad data (new line characters, empty spaces, etc.)
def cleanInputArr(arr: list) -> list:
    newArr = []
    
    for element in arr:
        if (element == " " or element == "" or element == "\n"):
            continue
        
        if ("\n" in element):
            element = element[:len(element) - 1]
        
        newArr.append(element)
        
    return newArr

# Input: none
# Output: sets the global data structure of locations, with names & coordinates 
def readCoordinates() -> None:
    coordinatesFile = open("./data/coordinates.txt", "r")
    
    for line in coordinatesFile:
        inputArr = line.split(" ")
        
        inputArr = cleanInputArr(inputArr)
        
        location = Location(inputArr[0], inputArr[1], inputArr[2], [])
        
        locations.append(location)
        
# Input: none
# Output: sets the global data structure of locations, with their respective adjacencies
def readAdjacencies() -> None:
    file = open("./data/Adjacencies.txt", "r")
    
    for line in file:
        adjArr = line.split(" ")
        
        adjArr = cleanInputArr(adjArr)
        
        town = adjArr[0]
        
        matchingTown = getLocation(town)
        
        if (matchingTown == None):
            raise LookupError("Unable to find town with name {}".format(town))
        
        for otherTown in adjArr:
            if (otherTown == town):
                continue
            
            matchingAdjacentTown = getLocation(otherTown)
        
            if (matchingAdjacentTown == None):
                continue
        
            matchingTown.adjacencies.append(matchingAdjacentTown)
            
            matchingAdjacentTown.adjacencies.append(matchingTown)

# Input: locations to find distance
# Output: distance, in made up units
def getDistance(locationOne: Location, locationTwo: Location) -> float:
    x1, y1 = float(locationOne.long), float(locationOne.lat)
    x2, y2 = float(locationTwo.long), float(locationTwo.lat)
    
    return math.sqrt(math.pow((x2 - x1), 2) + math.pow((y2 - y1), 2))
    

# Input: list of locations to search
# Output: none
# just does the job
def guidedSearch(startingLocation: Location, endLocation: Location): 
    visitedLocation = []
    
    prioQ = PriorityQueue()
    
    prioQ.put((0, startingLocation))
    
    startingLocation.isVisited = True
    
    while (not(prioQ.empty())):
        location = prioQ.get()[1] 
        
        visitedLocation.append(location)
        
        print("Visiting {}...".format(location.name))
        
        if (location == endLocation):
            print("Found route!")
            
            print("Route: ", end="")
            
            for idx, i in enumerate(visitedLocation):
                if (idx == len(visitedLocation) - 1):
                    print("{}.".format(i.name))
                else:
                    print(" {}, ".format(i.name), end="")
            
            break
        
        for city in location.adjacencies:
            if (city.isVisited == False):
                city.isVisited = True
                prioQ.put((getDistance(city, endLocation), city))
        


def main():        
    readCoordinates()
    readAdjacencies()
    
    try: 
        startingPoint = input("Enter the city you wish to start from: ")
        
        startingLocation = getLocation(startingPoint)
    
        if (startingLocation is None):
            raise NameError()
        
        endingPoint = input("Enter your destination city: ")
        
        endingLocation = getLocation(endingPoint)
        
        if (endingLocation is None):
            raise NameError()
        
        print("{}'s coords are {}deg and {}deg".format(startingLocation.name, startingLocation.lat, startingLocation.long))
        
        print("Goal destination {}'s coords are {}deg and {}deg".format(endingLocation.name, endingLocation.lat, endingLocation.long))
            
        guidedSearch(startingLocation, endingLocation)
    except NameError:
        print("Error: City name not found.")
    except:
        print("Error: Unsure of what happened, I tested this pretty thoroughly, please give me an A.")
    

if __name__ == "__main__":
    main()
    