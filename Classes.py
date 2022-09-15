#A player consists of a name, colour and a list of countries with associated troop counts (ex. [[Country0, troopCount], [Country1, 1],...])
class Player:
  
    def __init__(self, name="N/A", colour="N/A", \
                 occupied=[]):
        
        self.__name = name
        self.__colour = colour
        self.__occupied = occupied

    def getName(self):
        return self.__name

    def getColour(self):
        return self.__colour

    def getCountriesOccupied(self):
        return self.__occupied

    def getTotalTroops(self):
        totalTroops = 0
        for country in self.__occupied:
            totalTroops += country[1]
        return totalTroops

##    GOAL    
## Player: Josh
## Colour: Orange
## Countries occupied:
    ## North Africa: 5
    ## Brazil: 6
    ## ...

    
    def __str__(self):
        countriesStr = ""
        for country in self.__occupied:
            name = country[0].getName()
            troops = str(country[1])
            countriesStr = countriesStr + "\t" + name + ": " + troops + "\n"
        return"Player: %s \nColour: %s \nCountries occupied: \n%s" % \
               (self.__name, self.__colour, countriesStr)


               
class Country:
    
    def __init__(self, name="N/A", playerName="N/A", troops=0, continent="N/A", \
                 nearbyCountryNames=[]):
        
        self.__name = name
        self.__nearbyCountryNames = nearbyCountryNames
        self.__continent = continent
        self.__playerName = playerName
        self.__numOfTroops = troops
        

    def getName(self):
        return self.__name

    def getNearbyCountryNames(self):
        return  self.__nearbyCountryNames

    def getContinent(self):
        return self.__continent

    def getPlayerName(self):
        return self.__playerName

    def getNumOfTroops(self):
        return self.__numOfTroops


##    GOAL    
## Country: Brazil
## Ruler's Name: Josh
## Troops Occupying: 5
## Continent: South America
## Nearby Countries:
    ## Argentina
    ## North Africa
    ## Peru
    ## Venezuela

    
    def __str__(self):
        nearbyStr = ""
        for nearby in self.__nearbyCountryNames:
            nearbyStr = nearbyStr + "\t" + nearby + "\n"
        return"Country: %s \nRuler's Name: %s \nTroops Occupying: %d \nContinent: %s \nNearby Countries: \n%s" \
               % (self.__name, self.__playerName, self.__numOfTroops, self.__continent, nearbyStr)
    
##Countries
brazil = Country("Brazil", "", 1, "South America", ["Argentina", "North Africa", "Peru", "Venezuela"])
venezuela = Country("Venezuela", "", 1, "South America", ["Central America", "Brazil", "Peru"])
peru = Country("Peru", "", 1, "South America", ["Argentina", "Brazil", "Venezuela"])
argentina = Country("Argentina", "", 1, "South America", ["Brazil", "Peru"])

centralAmerica = Country("Central America", "", 1, "North America", ["Western US", "Eastern US", "Venezuela"])
westernUS = Country("Western US", "", 1, "North America", ["Central America", "Eastern US", "Ontario", "Alberta"])
easternUS = Country("Eastern US", "", 1, "North America", ["Western US", "Central America", "Quebec", "Ontario"])
quebec = Country("Quebec", "", 1, "North America", ["Ontario", "Eastern US", "Greenland"])
ontario = Country("Ontario", "", 1, "North America", ["Western US", "Eastern US", "Quebec", "Alberta", "Northwest Territory", "Greenland"])
alberta = Country("Alberta", "", 1, "North America", ["Western US", "Ontario", "Northwest Territory", "Alaska"])
greenland = Country("Greenland", "", 1, "North America", ["Iceland", "Quebec", "Ontario", "Northwest Territory"])
northwestTerritory = Country("Northwest Territory", "", 1, "North America", ["Alberta", "Ontario", "Greenland", "Alaska"])
alaska = Country("Alaska", "", 1, "North America", ["Alberta", "Northwest Territory", "Kamchatka"])

kamchatka = Country("Kamchatka", "", 1, "Asia", ["Alaska", "Japan", "Mongolia", "Irkutsk", "Yakutsk"])
yakutsk = Country("Yakutsk", "", 1, "Asia", ["Kamchatka", "Siberia", "Irkutsk"])
irkutsk = Country("Irkutsk", "", 1, "Asia", ["Siberia", "Kamchatka", "Mongolia", "Irkutsk"])
siberia = Country("Siberia", "", 1, "Asia", ["Ural", "China", "Mongolia", "Irkutsk", "Yakutsk"])
mongolia = Country("MNongolia", "", 1, "Asia", ["China", "Japan", "Ural", "Irkutsk", "Kamchatka"])
china = Country("China", "", 1, "Asia", ["Siam", "India", "Mongolia", "Afghanistan", "Ural", "Siberia"])
japan = Country("Japan", "", 1, "Asia", ["Kamchatka", "Mongolia"])
ural = Country("Ural", "", 1, "Asia", ["Ukraine", "Afghanistan", "Siberia", "China"])
afghanistan = Country("Afghanistan", "", 1, "Asia", ["Ukraine", "Middle East", "Ural", "China", "India"])
siam = Country("Siam", "", 1, "Asia", ["Indonesia", "China", "India"])
india = Country("India", "", 1, "Asia", ["Siam", "China", "Afghanistan", "Middle East"])
middleEast = Country("Middle East", "", 1, "Asia", ["India", "Afghanistan", "Ukraine", "Southern Europe", "Egypt", "East Africa"])

indonesia = Country("Indonesia", "", 1, "Oceania", ["Siam", "Western Australia", "New Guinea"])
westernAustralia = Country("Western Australia", "", 1, "Oceania", ["Eastern Australia", "Indonesia", "New Guinea"])
easternAustralia = Country("Eastern Australia", "", 1, "Oceania", ["Western Australia", "New Guinea"])
newGuinea = Country("New Guinea", "", 1, "Oceania", ["Indonesia", "Eastern Australia"])

ukraine = Country("Ukraine", "", 1, "Europe", ["Ural", "Afghanistan", "Middle East", "Southern Europe", "Northern Europe", "Scandinavia"])
northernEurope = Country("Northern Europe", "", 1, "Europe", ["Scandinavia", "Western Europe", "Southern Europe", "Ukraine", "Great Britain"])
southernEurope = Country("Southern Europe", "", 1, "Europe", ["Middle East", "Western Europe", "Northern Europe", "Ukraine", "Egypt", "North Africa"])
westernEurope = Country("Western Europe", "", 1, "Europe", ["North Africa", "Northern Europe", "Southern Europe", "Great Britain"])
greatBritain = Country("Great Britain", "", 1, "Europe", ["Iceland", "Western Europe", "Northern Europe", "Scandinavia"])
iceland = Country("Iceland", "", 1, "Europe", ["Greenland", "Scandinavia", "Great Britain"])
scandinavia = Country("Scandinavia", "", 1, "Europe", ["Iceland", "Northern Europe",  "Ukraine", "Great Britain"])

egypt = Country("Egypt", "", 1, "Africa", ["East Africa", "Southern Europe",  "Middle East", "North Africa"])
northAfrica = Country("North Africa", "", 1, "Africa", ["East Africa", "Southern Europe",  "Western Europe", "Egypt", "Congo"])
eastAfrica = Country("East Africa", "", 1, "Africa", ["Congo", "Madagascar",  "Middle East", "North Africa", "South Africa", "Egypt"])
congo = Country("Congo", "", 1, "Africa", ["East Africa", "South Africa", "North Africa"])
southAfrica = Country("South Africa", "", 1, "Africa", ["East Africa", "Congo",  "Madagascar"])
madagascar = Country("Madagascar", "", 1, "Africa", ["South Africa", "East Africa"])


##def main():
##    country1 = Country("Brazil", "Josh" , 5, "South America", ["Argentina", "North Africa", "Peru", "Venezuela"])
##    print(country1.getNumOfTroops())
##    print(country1)
##    player1 = Player("Josh", "Orange", [[country1, 5]])
##    print(player1.getName())
##    print(player1)
##
##main()
