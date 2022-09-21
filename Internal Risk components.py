import math
import random

class Game:

    def __init__(self, gameType = ""):
        self.__gameType = gameType
        self.__board = []
        self.__players = []
        self.__turn = 1
        self.__sets = 0
        self.boardInitializer()
        random.shuffle(self.__board)
        numOfPlayers = self.numOfStartPlayers()
        troopCount = self.numOfStartTroops(numOfPlayers)
        self.initPlayers(numOfPlayers)
        self.initCountries()
        self.addLeftoverTroops(troopCount)
        

    def getPlayers(self):
        return self.__players

    def getBoard(self):
        return self.__board

    def getTurn(self):
        return self.__turn

    def getSets(self):
        return self.__sets

    def addCountry(self, country):
        self.__board.append(country)

    def removePlayer(self, player):
        self.__players.remove(player)

    def addTurn(self):
        self.__turn += 1

    def addSet(self):
        self.__sets += 1

    ## Initialize Players
    def initPlayers(self, numOfPlayers):
        for i in range(numOfPlayers):
            playerNumber = str(i+1)
            name = input("What is the name of player " + playerNumber + "? ")
            self.__players.append(Player(name, []))

    ## Gives each player a set of countries
    def initCountries(self):
        for i in range(len(Game.Board)):
            country = Game.Board[i]
            index = i % len(Game.Players)
            player = Game.Players[index]
            country.setPlayerName(player.getName())
            player.addCountry(country)
            
    ## Adds remaining troops to each players' countries
    def addLeftoverTroops(self, troopCount):
        for i in range(len(Game.Players)):
            player = Game.Players[i]
            remaining = troopCount - player.getTotalTroops()
            countries = player.getCountriesOccupied()
            numOfCountries = len(countries)
            for j in range(remaining):
                index = random.randint(0,(numOfCountries - 1))
                countries[index].addTroop()

    def boardInitializer(self):
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
        mongolia = Country("Mongolia", "", 1, "Asia", ["China", "Japan", "Ural", "Irkutsk", "Kamchatka"])
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
        self.addCountry(brazil)
        self.addCountry(venezuela)
        self.addCountry(peru)
        self.addCountry(argentina)
        
        self.addCountry(centralAmerica)
        self.addCountry(westernUS)
        self.addCountry(easternUS)
        self.addCountry(quebec)
        self.addCountry(ontario)
        self.addCountry(alberta)
        self.addCountry(greenland)
        self.addCountry(northwestTerritory)
        self.addCountry(alaska)
        
        self.addCountry(kamchatka)
        self.addCountry(yakutsk)
        self.addCountry(irkutsk)
        self.addCountry(siberia)
        self.addCountry(mongolia)
        self.addCountry(china)
        self.addCountry(japan)
        self.addCountry(ural)
        self.addCountry(afghanistan)
        self.addCountry(siam)
        self.addCountry(india)
        self.addCountry(middleEast)
        
        self.addCountry(indonesia)
        self.addCountry(westernAustralia)
        self.addCountry(easternAustralia)
        self.addCountry(newGuinea)
        
        self.addCountry(ukraine)
        self.addCountry(northernEurope)
        self.addCountry(southernEurope)
        self.addCountry(westernEurope)
        self.addCountry(greatBritain)
        self.addCountry(iceland)
        self.addCountry(scandinavia)
        
        self.addCountry(egypt)
        self.addCountry(northAfrica)
        self.addCountry(eastAfrica)
        self.addCountry(congo)
        self.addCountry(southAfrica)
        self.addCountry(madagascar)

    def numOfStartPlayers(self):
        numOfPlayers =  int(input("How many players? (2-6 players allowed): "))
        if numOfPlayers in range(2,6):
            return numOfPlayers
        else:
            print("Please pick a reasonable number of players\n")
            self.numOfStartPlayers()

            
    ## 6 players = 20 troops
    ## 5 players = 25
    ## 4 players = 30
    ## 3 players = 35
    ## 2 players = 40
    def numOfStartTroops(self, numOfPlayers):
        return 50 - 5*numOfPlayers

    

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
        self.__cards = []

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

    #Returns list of occupied country names
    def getOccupiedCountryNames(self):
        occupiedCountryNames = []
        for country in self.getCountriesOccupied():
            occupiedCountryNames.append(country.getName())
        return occupiedCountryNames

    def getCards(self):
        return self.__cards

    def addCard(self):
        card = random.randint(1,3)
        self.__cards.append(card)

    #Returns match information ([Bool, Num] = [True if has match, Max match value])
    def hasMatch(self):
        cards = self.getCards()
        if len(cards) < 3:
            return [False, 0]
        else:
            ones = cards.count(1)
            twos = cards.count(2)
            threes = cards.count(3)
            if ones > 0 and twos > 0 and threes > 0:
                return [True, 10]
            elif threes > 2:
                return [True, 8]
            elif threes > 2:
                return [True, 6]
            elif threes > 2:
                return [True, 4]
            else:
                return [False, 0]

    #Removes country from players list
    def removeCountry(self, country):
        if country in self.__occupied:
            self.__occupied.remove(country)


    #Adds country to players list
    def addCountry(self, country):
        self.__occupied.append(country)

    def isAlive(self):
        if self.getTotalTroops() == 0:
            return False
        else:
            return True

    #Returns number of troops added by country count
    def draftTroopsByCountries(self):
        numOfCountries = len(self.getCountriesOccupied())
        if numOfCountries < 12:
            return 3
        else:
            return numOfCountries // 3


    def getContinentCount(self):
        ## lst: [SA, NA, Asia, Oceania, Europe, Africa]
        continentCount = [0,0,0,0,0,0]
        for country in self.getCountriesOccupied():
            if country.getContinent() == "South America":
                continentCount[0] += 1
            elif country.getContinent() == "North America":
                continentCount[1] += 1
            elif country.getContinent() == "Asia":
                continentCount[2] += 1
            elif country.getContinent() == "Oceania":
                continentCount[3] += 1
            elif country.getContinent() == "Europe":
                continentCount[4] += 1
            elif country.getContinent() == "Africa":
                continentCount[5] += 1

        return continentCount

    
    def draftTroopsByContinent(self):
        additionalTroops = 0
        continentCount = self.getContinentCount()

        #SA
        if continentCount[0] == 4:
            additionalTroops += 2
        #NA
        elif continentCount[1] == 9:
            additionalTroops += 5
        #Asia
        elif continentCount[2] == 12:
            additionalTroops += 7
        #Oceania
        elif continentCount[3] == 4:
            additionalTroops += 2
        #Europe
        elif continentCount[4] == 7:
            additionalTroops += 5
        #Africa
        elif continentCount[5] == 6:
            additionalTroops += 3

        return additionalTroops

        
    ## def draftTroopsByCards(self):
   
    #Returns country drafted to
    def draftRandom(self):
        draftTroops = 0
        draftTroops += self.draftTroopsByCountries()
        draftTroops += self.draftTroopsByContinent()
        draftTroops += self.draftTroopsByCards()
        options = len(self.getCountriesOccupied()) - 1
        index = random.randint(0,options)
        country = self.getCountriesOccupied()[index]
        country.addTroops(draftTroops)
        return country

    
    #Returns list of invadable countries
    def invadableCountries(self, country):
        occupiedCountryNames = self.getOccupiedCountryNames()
        nearbyCountries = country.getNearbyCountryNames()
        for countryName in nearbyCountries:
            if countryName in occupiedCountryNames:
                nearbyCountries.remove(countryName)
        return nearbyCountries
    
    #Needs work
    def attackDecision(self, attackingCountry):
        options = self.invadableCountries(attackingCountry)
        print("Here are your options: ", options)
        defender = input("Who are you attacking? ")
        if len(options) > 0:
            index = random.randint(0, (len(options)-1))
            defender = options[index]
            self.attackCountry(attackingCountry, defender)
            ##Else, don't attack    
        
    def attackRandom(self, attackingCountry):
        options = self.invadableCountries(attackingCountry)
##        print("Here are your options: ", options)
##        defender = input("Who are you attacking? ")
        if len(options) > 0:
            index = random.randint(0, (len(options)-1))
            defender = options[index]
            self.attackCountry(attackingCountry, defender)
            ##Else, don't attack


        
    #def fortifyRandom(self):
    

    ## Simulates an attack and updates accordingly
    def attackCountry(self, startCountry, defender):
        for country in board:
            if country.getName() == defender:
                myTroops = startCountry.getNumOfTroops()
                enemyTroops = country.getNumOfTroops()
                result = whoWins(myTroops, enemyTroops)
                
                if result[2]: ##Attacker wins

                    ## Add country to our list
                    self.addCountry(country)
                    
                    ## Remove country from defender's list
                    defenderName = country.getPlayerName()
                    for player in players:
                        if defenderName == player.getName():
                            player.removeCountry(country)
                            break

                    ## Add new owner to country
                    country.setPlayerName(startCountry.getPlayerName())

                    # Move associated troops
                    if myTroops <= 4:
                        country.setNumOfTroops(result[0] - 1)
                    else:
                        options = range(3,result[0])
                        move = result[0] - 1
                        ## move = int(input("How many troops do you want to move? (", options, ")"))
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
        return"Player: %s \nNumber: %s \nTotal troops: %d \nCountries occupied: \n%s" % \
               (self.__name, self.__number, self.getTotalTroops(), countriesStr)



#Country consists of a name, a player name, number of troops, a continent and a list of nearby countries
               
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

    def addTroops(self, troops):
        self.__numOfTroops += troops
    



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


## Prints board status by printing all players
def printPlayers(game):
    players = game.getPlayers()
    for i in range(len(players)):
        print(players[i])

        
#Play the fixed game to completion
def fixedGame(game):
    while len(game.getPlayers()) > 1:
                
                #Each player plays turn
                players = game.getPlayers()
                for i in range(len(players)):
                    player = players[i]
                    if not player.isAlive():
                        print(player)
                        print("Player ", player.getName(), " Has Been Terminated From The Board!")
                        game.removePlayer(player)
                    else:
                        player.draftFixed()
                        player.attack()
                        player.fortify()
                game.addTurn()

#Play the progressive game to completion
def progressiveGame(game):
    while len(game.getPlayers()) > 1:
                
                #Each player plays turn
                players = game.getPlayers()
                for i in range(len(players)):
                    player = players[i]
                    if not player.isAlive():
                        print(player)
                        print("Player ", player.getName(), " Has Been Terminated From The Board!")
                        game.removePlayer(player)
                    else:
                        player.draftProgressive()
                        player.attack()
                        player.fortify()
                game.addTurn()

#Autogenerate the random game to completion or to 500 turns printing the board status every 100 turns
def randomGame(game):
    while len(game.getPlayers()) > 1 and turn < 501:
        
        #Each player plays turn
        players = game.getPlayers()
        for i in range(len(players)):
            player = players[i]
            if not player.isAlive():
                print(player)
                print("Player ", player.getName(), " Has Been Terminated From The Board!")
                game.removePlayer(player)
            else:
                countryDrafted = player.draftRandom()
                player.attackRandom(countryDrafted)
                player.fortifyRandom()
        game.addTurn()
        if turn in [100,200,300,400,500]:
            for player in players:
                print(turn)
                print(player)

def main():
    # Random autogenerates moves and uses progressive cards
    gameType = input("What kind of game do you want to play? ('fixed', 'progressive' or 'random'): ")
    gameOptions = ['fixed', 'progressive', 'random']
    if gameType not in gameOptions:
        print(gameType, " is not an available option!")
        main()
    else:
        game = Game(gameType)
        printPlayers(game)
        print("The game ", gameType, " will now begin")

        if gameType == gameOptions[0]: 
            progressiveGame(game)
            

        elif gameType == gameOptions[1]: 
            fixedGame(game)

        elif gameType == gameOptions[2]: 
            randomGame(game)


main()




