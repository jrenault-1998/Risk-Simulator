import math
import random

## List of Countries
board = []

#List of Players
players = []


#A player consists of a name, number and a list of countries 
class Player:
    # Class variables
    NextNumber = 1


    #Initializes a Player


    def __init__(self, name="N/A", occupied=[]):
        
        self.__name = name
        self.__number = Player.NextNumber
        self.__occupied = occupied
        Player.NextNumber += 1

    def getName(self):
        return self.__name

    def getNumber(self):
        return self.__number

    def getCountriesOccupied(self):
        return self.__occupied

    def getTotalTroops(self):
        totalTroops = 0
        for country in self.__occupied:
            totalTroops += country.getNumOfTroops()
        return totalTroops


    #Removes country from players list
    def removeCountry(self, country):
        if country in self.__occupied:
            self.__occupied.remove(country)


    #Adds country to players list

    def addCountry(self, country):
        self.__occupied.append(country)

    ## Simulates an attack and updates accordingly
    def attackCountry(self, startCountry):
        options = startCountry.getNearbyCountryNames
        print("Here are your options: ", options)
        defender = input("Who are you attacking? ")
        
        for country in board:
            if country.getName() == defender:
                myTroops = startCountry.getNumOfTroops()
                enemyTroops = country.getNumOfTroops()
                result = whoWins(myTroops, enemyTroops)
                if result[2]: ##Attacker wins

                    ## Add country to our list
                    self.addCountry(country)
                    
                    ## Remove country from defender's list
                    for player in players:
                        if defender == player.getName():
                            player.removeCountry(country)
                            break

                    ## Add new owner to country
                    country.setPlayerName(startCountry.getPlayerName())

                    # Move associated troops
                    if myTroops <= 4:
                        country.setNumOfTroops(result[0] - 1)
                    else:
                        options = range(3,(result[0] - 1))
                        move = int(input("How many troops do you want to move? (", options, ")"))
                        if move in options:
                            country.setNumOfTroops(move)
                            startCountry.setNumOfTroops(result[0] - move)
                        else:
                            return("Error!!!! You need to pick an appropriate number of troops")  #Want this to ask the question again


                else: ##Defender wins
                    country.setNumOfTroops(result[1])
                    startCountry.setNumOfTroops(result[0])
                    
                break
        
            


##    Displays    
## Player: Josh
## Number: 1
## Countries occupied:
    ## North Africa: 5
    ## Brazil: 6
    ## ...

    
    def __str__(self):
        countriesStr = ""
        for country in self.__occupied:
            name = country.getName()
            troops = str(country.getNumOfTroops())
            countriesStr = countriesStr + "\t" + name + ": " + troops + "\n"
        return"Player: %s \nNumber: %s \nCountries occupied: \n%s" % \
               (self.__name, self.__number, countriesStr)



#Country consists of a name, a player name, nuber of troops, a continent and a list of nearby countries              
               
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

    def setPlayerName(self, playerName):
        self.__playerName = playerName

    def setNumOfTroops(self, numOfTroops):
        self.__numOfTroops = numOfTroops

    def addTroop(self):
        self.__numOfTroops += 1    



##    Displays    

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

## Takes in the enemy and our troop counts and returns list of final troop counts [myTroops, enemyTroops, Boolean]
def whoWins(myTroops, enemyTroops):


    while enemyTroops > 0 and myTroops > 1:
        d1 = random.randint(1,6)
        d2 = random.randint(1,6)
        d3 = random.randint(1,6)
        d4 = random.randint(1,6)
        d5 = random.randint(1,6)
        myDice = [d1, d2, d3]
        myDice.sort(reverse=True)
        myTwoDice = [d1, d2]
        myTwoDice.sort(reverse=True)
        enemyDice = [d4, d5]
        enemyDice.sort(reverse=True)

        if myTroops > 3:
            if enemyTroops > 1:
                if myDice[0] > enemyDice[0]:
                    enemyTroops -= 1
                else:
                    myTroops -= 1
                    
                if myDice[1] > enemyDice[1]:
                    enemyTroops -= 1
                else:
                    myTroops -= 1
            else:
                if myDice[0] > d4:
                    enemyTroops -= 1
                else:
                    myTroops -= 1
        elif myTroops == 3:
            if enemyTroops > 1:
                if myTwoDice[0] > enemyDice[0]:
                    enemyTroops -= 1
                else:
                    myTroops -= 1
                if myTwoDice[1] > enemyDice[1]:
                    enemyTroops -= 1
                else:
                    myTroops -= 1
            else:
                if myTwoDice[0] > d4:
                    enemyTroops -= 1
                else:
                    myTroops -= 1
        elif myTroops == 2:
            if enemyTroops > 1:
                if d1 > enemyDice[0]:
                    enemyTroops -= 1
                else:
                    myTroops -= 1
            else:
                if d1 > d4:
                    enemyTroops -= 1
                else:
                    myTroops -= 1
        else:
            return ("IDK what happened, I thought we checked all the cases!!!")
        
    finalResult = [myTroops, enemyTroops]
    ## True if myTroops won
    if enemyTroops == 0:
        finalResult[0] -= 1
        finalResult.append(True)
    else:
        finalResult.append(False)
    
    return finalResult ##Final troop counts [myTroops, enemyTroops, Boolean]




def boardInitializer():    
    ##Country variables are created
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
    
    ##Country objects are inserted into a list which is the "board"
    board.append(brazil)
    board.append(venezuela)
    board.append(peru)
    board.append(argentina)
    
    board.append(centralAmerica)
    board.append(westernUS)
    board.append(easternUS)
    board.append(quebec)
    board.append(ontario)
    board.append(alberta)
    board.append(greenland)
    board.append(northwestTerritory)
    board.append(alaska)
    
    board.append(kamchatka)
    board.append(yakutsk)
    board.append(irkutsk)
    board.append(siberia)
    board.append(mongolia)
    board.append(china)
    board.append(japan)
    board.append(ural)
    board.append(afghanistan)
    board.append(siam)
    board.append(india)
    board.append(middleEast)
    
    board.append(indonesia)
    board.append(westernAustralia)
    board.append(easternAustralia)
    board.append(newGuinea)
    
    board.append(ukraine)
    board.append(northernEurope)
    board.append(southernEurope)
    board.append(westernEurope)
    board.append(greatBritain)
    board.append(iceland)
    board.append(scandinavia)
    
    board.append(egypt)
    board.append(northAfrica)
    board.append(eastAfrica)
    board.append(congo)
    board.append(southAfrica)
    board.append(madagascar)

def numOfPlayers():
    numOfPlayers = int(input("How many players? (3-6 players allowed): "))
    
    ## 6 players = 20 troops
    ## 5 players = 25
    ## 4 players = 30
    ## 3 players = 35
    if numOfPlayers in range(3,6):
        return 50 - 5*numOfPlayers
    else:
        print("Please pick a reasonable number of players\n")
        numOfPlayers()

def main():
    boardInitializer()
    random.shuffle(board)
    numOfPlayers = numOfPlayers()

    ## Initialize Players
    for i in range(numOfPlayers):
        playerNumber = str(i+1)
        name = input("What is the name of player " + playerNumber + "? ")
        players.append(Player(name, []))

    ## Gives each player a set of countries
    for i in range(len(board)):
        country = board[i]
        index = i % numOfPlayers
        player = players[index]
        country.setPlayerName(player.getName())
        player.addCountry(country)

    ## Adds remaining troops to each players' countries
    for i in range(len(players)):
        player = players[i]
        remaining = troopCount - player.getTotalTroops()
        countries = player.getCountriesOccupied()
        numOfCountries = len(countries)
        for j in range(remaining):
            index = random.randint(0,(numOfCountries - 1))
            countries[index].addTroop()

    for i in range(len(players)):   
        print(players[i])

    for i in range(4):
        print(board[i])      

main()    



