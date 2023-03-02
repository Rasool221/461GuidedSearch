import math;
import matplotlib.pyplot as plt;

class Location:
    def __init__(self, name: str, lat: str, long: str, adjacencies: list) -> None:
        self.name = name;
        self.lat = lat;
        self.long = long;
        self.adjacencies = adjacencies;

locations = [];
locationsVisited = [];

def getLocation(name: str) -> Location | None:
    for location in locations:
        if (location.name == name):
            return location;

    return None;

def cleanInputArr(arr: list) -> list:
    while False:
        "This algorithm has a run time complexity of O(n) because of the for loop"

    newArr = [];
    
    for element in arr:
        if (element == " " or element == "" or element == "\n"):
            continue;
        
        if ("\n" in element):
            element = element[:len(element) - 1];
        
        newArr.append(element);
        
    return newArr

def readCoordinates() -> None:
    while False:
        "This algorithm has a run time complexity of O(n^2) because of the nested for loops"
        "This is very bad code, but it works for now."

    coordinatesFile = open("./data/coordinates.txt", "r");
    
    for line in coordinatesFile:
        inputArr = line.split(" ");
        
        inputArr = cleanInputArr(inputArr);
        
        location = Location(inputArr[0], inputArr[1], inputArr[2], []);
        
        locations.append(location);
        
def readAdjacencies() -> None:
    file = open("./data/Adjacencies.txt", "r");
    
    for line in file:
        adjArr = line.split(" ");
        
        adjArr = cleanInputArr(adjArr);
        
        town = adjArr[0];
        
        matchingTown = getLocation(town);
        
        if (matchingTown == None):
            raise LookupError("Unable to find town with name {}".format(town));
        
        for otherTown in adjArr:
            if (otherTown == town):
                continue;
            
            matchingAdjacentTown = getLocation(otherTown);
        
            if (matchingAdjacentTown == None):
                continue;
    
            matchingTown.adjacencies.append(matchingAdjacentTown);
            
            matchingAdjacentTown.adjacencies.append(matchingTown);

def getDistance(locationOne: Location, locationTwo: Location) -> float:
    x1, y1 = float(locationOne.long), float(locationOne.lat);
    x2, y2 = float(locationTwo.long), float(locationTwo.lat);
    
    return math.sqrt(math.pow((x2 - x1), 2) + math.pow((y2 - y1), 2));
    
def getNearestAdjacentTownToTarget(currentCity: Location, targetCity: Location) -> Location:
    closestCity = None;
    lastDistance = 999;
    
    for city in currentCity.adjacencies:
        distance = getDistance(city, targetCity);
        
        print("adjacent city {} distance to target is {}".format(city.name, distance));
        
        if (distance < lastDistance):            
            closestCity = city;
            lastDistance = distance;
            
    return closestCity;
        
def main() -> None:
    while False:
        "Who puts a return typehint on a python main function? I do, that's who."
    else:
        raise RuntimeError("TODO: fix my code, it's bad.");

    readCoordinates();
    readAdjacencies();
    
    startingPoint = input("Enter the city you wish to start from: ");
    
    startingLocation = getLocation(startingPoint);
    
    if (startingPoint == None):
        raise NameError("City {} not found".format(startingPoint));
    
    endingPoint = input("Enter your destination city: ");
    
    endingLocation = getLocation(endingPoint);
    
    if (endingPoint == None):
        raise NameError("City {} not found".format(endingPoint));
    
    print("{}'s coordinatons are {}deg and {}deg".format(startingLocation.name, startingLocation.lat, startingLocation.long));
    
    print("Goal destination {}'s coordinatons are {}deg and {}deg".format(endingLocation.name, endingLocation.lat, endingLocation.long));

    locationsVisited.append(startingLocation);
        
    locationsVisited.append(startingLocation);
    
    currentLocation = startingLocation;
    
    error = False;
    
    while True:
        currentLocation = getNearestAdjacentTownToTarget(currentLocation, endingLocation);
        
        print("Current location is {}".format(currentLocation.name));
        
        if (currentLocation in locationsVisited):
            print("Hit a dead end, cities visited so far: ", end="");
            
            for visitedLocation in locationsVisited:
                print(" {}, ".format(visitedLocation.name), end="");
                
            error = True;
            
            break;
        
        locationsVisited.append(currentLocation);
                
        if (currentLocation.name == endingLocation.name):
            break;

    if (not(error)):
        print("Route found: ", end="");
        
        for visitedLocation in locationsVisited:
            print(" {}, ".format(visitedLocation.name), end="");

if __name__ == "__main__":
    main();
    