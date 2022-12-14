#Imports all required packages
import math
import random


# A class to hold all relevant Game information
class Game:

    #Constructor to generate Game object which consists of
    #a game type, board, list of Players, turn and sets
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

    #Returns list of players    
    def getPlayers(self):
        return self.__players

    #Returns list of countries which make up the board
    def getBoard(self):
        return self.__board
    
    #Returns turn number (starts at 1)
    def getTurn(self):
        return self.__turn

    #Returns number of sets traded in thus far (starts at 0)
    def getSets(self):
        return self.__sets

    #Appends Country to the Board
    def addCountry(self, country):
        self.__board.append(country)

    #Removes Player from the game (called if all territories are conquered)
    def removePlayer(self, player):
        self.__players.remove(player)

    #Adds 1 to turn count
    def addTurn(self):
        self.__turn += 1

    #Adds 1 to set count
    def addSet(self):
        self.__sets += 1

    #Prints board status by printing all players
    def printPlayers(self):
        players = self.getPlayers()
        for i in range(len(players)):
            print(players[i])

    #Generates all countries for the classic risk board and appends them to the board list
    def boardInitializer(self):
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

    #Asks user to select number of Players for this game
    def numOfStartPlayers(self):
        numOfPlayers =  input("How many players? (2-6 players allowed): ")
        if numOfPlayers.isdigit():
            numOfPlayers = int(numOfPlayers)
            if numOfPlayers in range(2,6):
                return numOfPlayers
            else:
                print("Please pick a reasonable number of players\n")
                return self.numOfStartPlayers()
        else:
            print("Please pick a number for the player count\n")
            return self.numOfStartPlayers()

    #Returns number of starting troops for each Player according to the board game's rules
    def numOfStartTroops(self, numOfPlayers):
        return 50 - 5 * numOfPlayers

    #Initialize Players by getting their names
    def initPlayers(self, numOfPlayers):
        for i in range(numOfPlayers):
            playerNumber = str(i+1)
            name = input("What is the name of player " + playerNumber + "? ")
            self.__players.append(Player(name, []))

    #Generates a set of countries for each player randomly
    def initCountries(self):
        board = self.getBoard()
        for i in range(len(board)):
            country = board[i]
            players = self.getPlayers()
            index = i % len(players)
            player = players[index]
            country.setPlayerName(player.getName())
            player.addCountry(country)
            
    #Adds remaining troops to each Players' countries randomly
    def addLeftoverTroops(self, troopCount):
        players = self.getPlayers()
        for i in range(len(players)):
            player = players[i]
            remaining = troopCount - player.getTotalTroops()
            countries = player.getCountriesOccupied()
            numOfCountries = len(countries)
            for j in range(remaining):
                index = random.randint(0,(numOfCountries - 1))
                countries[index].addTroop()

    #Returns troop value of next set in a progressive game (4,6,8,10,12,15,20,...)      
    def setValue(self, game):
        setNumber = self.getSets()
        if setNumber == 0:
            return 4
        elif setNumber == 1:
            return 6
        elif setNumber == 2:
            return 8
        elif setNumber == 3:
            return 10
        elif setNumber == 4:
            return 12
        elif setNumber > 4:
            return 5*(setNumber-2)
        else:
            print("Set values negative, set value is now worth zero \n\t*This is a coding error*")
            return 0
    

#A class to hold all relevant Player information
#This class consists of all functions for a Player to play their turn
class Player:
    
    # Class variables
    NextNumber = 1


    #Constructor to generate Player object which consists of
    #a name, number, list of occupied countries and a list of cards
    def __init__(self, name="N/A", occupied=[]):
        self.__name = name
        self.__number = Player.NextNumber
        self.__occupied = occupied
        Player.NextNumber += 1
        self.__cards = []

    #Returns Player's name
    def getName(self):
        return self.__name

    #Returns Player's number
    def getNumber(self):
        return self.__number

    #Returns list of Countries Player occupies
    def getCountriesOccupied(self):
        return self.__occupied

    #Returns total number of troops Player has across all occupied countries
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

    #Returns list of cards owned by Player
    def getCards(self):
        return self.__cards

    #Gives Player a card
    def addCard(self):
        card = random.randint(1,3)
        self.__cards.append(card)

    #Removes Country from Player's list of occupied Countries
    def removeCountry(self, country):
        if country in self.__occupied:
            self.__occupied.remove(country)

    #Prints a list of Countries
    def printCountryNames(self, countries):
        for country in countries:
            print(country.getName())

    #Adds Country to Player's list
    def addCountry(self, country):
        self.__occupied.append(country)

    #Returns true if the Player has a non-zero troop count
    def isAlive(self):
        return not self.getTotalTroops() == 0

    #Returns list where first element is bool (True if found) second element is the country found
    def findCountry(self, countryName):
        for country in self.getCountriesOccupied():
            if country.getName() == countryName:
                return [True, country]
        print("The country you are looking for was not found")
        return [False]

###  Draft Functions  ###
        
    #Returns number of troops added by number of Countries occupied
    def draftTroopsByCountries(self):
        numOfCountries = len(self.getCountriesOccupied())
        if numOfCountries < 12:
            return 3
        else:
            return numOfCountries // 3

    #Returns list containing number of Countries owned in each continent
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

    #Returns number of troops added due to Player holding continents
    def draftTroopsByContinent(self):
        additionalTroops = 0
        continentCount = self.getContinentCount()
        #SA
        if continentCount[0] == 4:
            additionalTroops += 2
        #NA
        if continentCount[1] == 9:
            additionalTroops += 5
        #Asia
        if continentCount[2] == 12:
            additionalTroops += 7
        #Oceania
        if continentCount[3] == 4:
            additionalTroops += 2
        #Europe
        if continentCount[4] == 7:
            additionalTroops += 5
        #Africa
        if continentCount[5] == 6:
            additionalTroops += 3
        return additionalTroops

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
            elif twos > 2:
                return [True, 6]
            elif ones > 2:
                return [True, 4]
            else:
                return [False, 0]

    #Removes match from players hand given a trade in        
    def removeMatch(hasMatch):
        if hasMatch[0]:
            if hasMatch[1] == 10:
                self.__cards.remove(1)
                self.__cards.remove(2)
                self.__cards.remove(3)
            elif hasMatch[1] == 8:
                self.__cards.remove(3)
                self.__cards.remove(3)
                self.__cards.remove(3)
            elif hasMatch[1] == 6:
                self.__cards.remove(2)
                self.__cards.remove(2)
                self.__cards.remove(2)
            elif hasMatch[1] == 4:
                self.__cards.remove(1)
                self.__cards.remove(1)
                self.__cards.remove(1)
        else:
            print("Player didn't have a removable match")

    #Returns boolean answer to trade in cards or not
    def tradeIn(self, hasMatch):
        string = "Do you want to trade in three cards for " + str(hasMatch[1]) + " troops? (0 for no, 1 for yes): "
        if string.isdigit():
            answer = int(string)    
            if answer == 0 or answer == 1:
                return bool(answer)
            else:
                print("This is not an acceptable number")
                return self.tradeIn(hasMatch)
        else:
                print("This is not an acceptable answer")
                return self.tradeIn(hasMatch)
            
    #Returns number of troops leftover after deployment
    def deployHowMany(self, remainingTroops, country):
        print(country)
        string = "You can deploy up to " + str(remainingTroops) + " here, how many do you want to? "
        troops = input(string)
        if troops.isdigit():
            troops = int(troops)
            if troops in range(1, remainingTroops+1):
                country.addTroops(troops)
                leftover = remainingTroops - troops
                return leftover
            else:
                print("Please choose an acceptable number of troops to deploy here")
                return self.deployHowMany(remainingTroops, country)
        else:
            print("Please choose a number")
            return self.deployHowMany(remainingTroops, country)
        
    #Returns number of troops leftover after deployment by calling deployHowMany
    def deployWhere(self, remainingTroops):
        self.printCountryNames(self.getCountriesOccupied())
        countryName = input("What country do you want to deploy some troops to? ")
        country = self.findCountry(countryName)
        if country[0]:
            return self.deployHowMany(remainingTroops, country[1])
        else:
            print("This is not an acceptable answer, please select from your occupied countries")
            return self.deployWhere(remainingTroops)
            
    #Allows Player to draft troops in fixed game
    def draftFixed(self):
        draftTroops = 0
        draftTroops += self.draftTroopsByCountries()
        draftTroops += self.draftTroopsByContinent()
        hasMatch = self.hasMatch()
        if hasMatch[0]:
            if len(self.getCards()) == 5:
                print("You have 5 cards, so you must trade in 3 for " + str(hasMatch[1]) + " troops")
                draftTroops += hasMatch[1]
                self.removeMatch(hasMatch)
            else:
                print("Without cards you have ", draftTroops, " troops to deploy")
                if self.tradeIn(hasMatch):
                    draftTroops += hasMatch[1]
                    self.removeMatch(hasMatch)
        print("You are starting your turn with ", draftTroops, " troops to deploy")
        print("Here is your board position!")
        print(self)
        while draftTroops > 0:
            draftTroops = self.deployWhere(draftTroops)
            
        
    #Allows Player to draft troops in fixed game
    def draftProgressive(self, game):
        draftTroops = 0
        draftTroops += self.draftTroopsByCountries()
        draftTroops += self.draftTroopsByContinent()
        print(int(draftTroops))
        hasMatch = self.hasMatch()
        if hasMatch[0]:
            setValue = game.setValue()
            if len(self.getCards()) == 5:
                print("You have 5 cards, so you must trade in 3 for " + setValue + " troops")
                draftTroops += setValue
                self.removeMatch(hasMatch)
            else:
                print("Without cards you have ", draftTroops, " troops to deploy")
                matchValue = [hasMatch[0], setValue]
                if self.tradeIn(matchValue):
                    draftTroops += setValue
                    self.removeMatch(hasMatch)
        print("You are starting your turn with ", draftTroops, " troops to deploy")
        print("Here is your board position!")
        print(self)
        while draftTroops > 0:
            draftTroops = self.deployWhere(draftTroops)

    #Returns country drafted to
    def draftRandom(self):
        draftTroops = 0
        draftTroops += self.draftTroopsByCountries()
        draftTroops += self.draftTroopsByContinent()
        hasMatch = self.hasMatch()
        if hasMatch[0]:
            draftTroops += hasMatch[1]
            self.removeMatch(hasMatch)
        options = len(self.getCountriesOccupied()) - 1
        index = random.randint(0,options)
        country = self.getCountriesOccupied()[index]
        country.addTroops(draftTroops)
        return country

###  Attack Functions  ###
    
    #Takes in an occupied Country and returns list of invadable Countries
    def invadableCountries(self, country):
        occupiedCountryNames = self.getOccupiedCountryNames()
        nearbyCountries = country.getNearbyCountryNames().copy()
        for countryName in nearbyCountries:
            if countryName in occupiedCountryNames:
                nearbyCountries.remove(countryName)
        return nearbyCountries


##    def attackRandom(self, attackingCountry):
##        options = self.invadableCountries(attackingCountry)
##        if len(options) > 0:
##            index = random.randint(0, (len(options)-1))
##            defender = options[index]
##            self.blitz(attackingCountry, defender)
##            ##Else, don't attack

            
    #Asks for a country name from a list and returns the country
    def attacker(self, options):
        print("Here are your options for countries that you can attack with: \n")
        self.printCountryNames(options)
        countryName = input("What country do you want to attack with? ")
        optionNames = []
        for country in options:
            optionNames.append(country.getName())
        result = self.findCountry(countryName)
        if result[0]:
            return result[1] 
        else:
            print("That is not an option, please try again")
            return self.attacker(options)

            
    def defender(self, attacker, game):
        options = attacker.getNearbyCountryNames().copy()
        owned = self.getOccupiedCountryNames()
        print(options)
        print(owned)
        for name in options:
            if name in owned:
                options.remove(name)
        print(options)
        print("Here are your options for who to attack: ", options)
        defenderName = input("Who do you want to attack? ")
        if defenderName in options:
            #Search the board for this person and their country
            board = game.getBoard()
            for country in board:
                if country.getName() == defenderName:
                    print(attacker)
                    print("Is Attacking")
                    print(country)
                    return country
        else:
            print("That is not an appropriate response")
            return self.defender(attacker, game)

            
    def moveTroops(self, attacker, defender, troops):
        if troops <= 4:
            defender.setNumOfTroops(troops - 1)
            attacker.setNumOfTroops(1)
        else:
            string = "How many troops do you want to move? ("
            for i in range(3,troops):
                string += str(i)
                string += ", "
            string = string[:-2]
            string += ")"
            move = int(input(string))
            if move in range(3,troops):
                defender.setNumOfTroops(move)
                attacker.setNumOfTroops(troops - move)
            else:
                print("Error!!!! You need to pick an appropriate number of troops")
                return self.moveTroops(attacker, defender, troops)
            
    #Simulates a blitzed attack and updates accordingly
    def blitz(self, attacker, defender, game):
            attackerTroops = attacker.getNumOfTroops()
            defenderTroops = defender.getNumOfTroops()
            result = self.blitzWinner(attackerTroops, defenderTroops)
            if result[2]: ##Attacker wins
                print("Attacker Wins!")
                
                ## Remove country from defender's list
                defenderName = defender.getPlayerName()
                for player in game.getPlayers():
                    if defenderName == player.getName():
                        player.removeCountry(defender)
                        #Checks if defender dies
                        if player.getTotalTroops() == 0:
                            print(player)
                            print("Player ", player.getName(), " Has Been Terminated From The Board!")
                            game.removePlayer(player)
                        break
                    
                ## Add country to our list
                self.addCountry(defender)
                
                ## Add new owner to country
                defender.setPlayerName(attacker.getPlayerName())

                # Move associated troops
                self.moveTroops(attacker, defender, result[0])

            else: ##Defender wins
                print("Defender Wins!")
                defender.setNumOfTroops(result[1])
                attacker.setNumOfTroops(result[0])

    ## Takes in the enemy and our troop counts and returns list of final troop counts [attackerTroops, defenderTroops, Boolean]
    def blitzWinner(self, attackerTroops, defenderTroops):
        while defenderTroops > 0 and attackerTroops > 1:
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

            if attackerTroops > 3:
                if defenderTroops > 1:
                    if myDice[0] > enemyDice[0]:
                        defenderTroops -= 1
                    else:
                        attackerTroops -= 1
                        
                    if myDice[1] > enemyDice[1]:
                        defenderTroops -= 1
                    else:
                        attackerTroops -= 1
                else:
                    if myDice[0] > d4:
                        defenderTroops -= 1
                    else:
                        attackerTroops -= 1
            elif attackerTroops == 3:
                if defenderTroops > 1:
                    if myTwoDice[0] > enemyDice[0]:
                        defenderTroops -= 1
                    else:
                        attackerTroops -= 1
                    if myTwoDice[1] > enemyDice[1]:
                        defenderTroops -= 1
                    else:
                        attackerTroops -= 1
                else:
                    if myTwoDice[0] > d4:
                        defenderTroops -= 1
                    else:
                        attackerTroops -= 1
            elif attackerTroops == 2:
                if defenderTroops > 1:
                    if d1 > enemyDice[0]:
                        defenderTroops -= 1
                    else:
                        attackerTroops -= 1
                else:
                    if d1 > d4:
                        defenderTroops -= 1
                    else:
                        attackerTroops -= 1
            else:
                return ("IDK what happened, I thought we checked all the cases!!!")
            
        finalResult = [attackerTroops, defenderTroops]
        ## True if attackerTroops won
        if defenderTroops == 0:
            finalResult[0] -= 1
            finalResult.append(True)
        else:
            finalResult.append(False)
        return finalResult ##Final troop counts [attackerTroops, defenderTroops, Boolean]
    
    #Runs the attack sequence by generating a list of Countries a Player can attack from
    #Calls functions to select the attacking Country and the defending Country
    def attack(self, game):
        options = self.getCountriesOccupied().copy()
        for country in options:
            if country.getNumOfTroops() == 1:
                options.remove(country)  
            else:
                nearby = country.getNearbyCountryNames().copy()
                owned = self.getOccupiedCountryNames()
                for name in nearby:
                    if name in owned:
                        nearby.remove(name)
                if len(nearby) == 0:
                    options.remove(country)
        self.printCountryNames(options)
        if len(options) == 0:
            print("You can't attack since you have no accessible troops")
        else:    
            attacker = self.attacker(options)
            defender = self.defender(attacker, game)
            #Call rollDecision() to either slow roll or blitz (once written)
            self.blitz(attacker, defender, game)

###  Fortify Functions  ###

    def startOptionsFortify(self):
        countries = self.getCountriesOccupied()
        options = []
        for country in countries:
            if country.getNumOfTroops() > 1:
                options.append(country)
        countryNames = self.getOccupiedCountryNames()
        for country in options:
            hasNearby = False
            surrounding = country.getNearbyCountryNames()
            for surroundingCountry in surrounding:
                if surroundingCountry in countryNames:
                    hasNearby = True
                    break
            if not hasNearby:
                options.remove(country)
        return options


                
    def fortifyStart(self, startOptions):
        print("Here are you options for countries to fortify from: ")
        countryNames = []
        for country in startOptions:
            countryNames.append(country.getName())
            print(country)
        startCountryName = input("What country would you like to fortify from? ")
        if startCountryName in countryNames:
            for country in startOptions:
                if country.getName() == startCountryName:
                    return country
        else:
            print("Please pick from the list printed.")
            return self.fortifyStart(startOptions)


    #Returns all possible countries connected via single path to fortifyStart
    def endOptionsFortify(self, fortifyStart):
        checked = []
        toBeChecked = []
        endOptions = []
        for name in fortifyStart.getNearbyCountryNames():
            toBeChecked.append(name)
            checked.append(fortifyStart.getName())
        while len(toBeChecked) > 0:
            countryName = toBeChecked.pop(0)
            if countryName not in checked:
                checked.append(countryName)
                if countryName in self.getOccupiedCountryNames():
                    for country in self.getCountriesOccupied():
                        if countryName == country.getName():
                            endOptions.append(country)
                            for name in country.getNearbyCountryNames():
                                toBeChecked.append(name)
                        
        return endOptions


    def fortifyEnd(self, endOptions):
        print("Here are you options for countries to fortify to: ")
        countryNames = []
        for country in endOptions:
            countryNames.append(country.getName())
            print(country)
        endCountryName = input("What country would you like to fortify to? ")
        if endCountryName in countryNames:
            for country in endOptions:
                if country.getName() == endCountryName:
                    return country
        else:
            print("Please pick from the list printed.")
            return self.fortifyEnd(endOptions)

    def fortifyTroopCount(self, movableTroops):
        print("you can move up to ", movableTroops, ". How many would you like to move? ")
        troopCount = input("Please enter a number of troops to be moves: ")
        if troopCount.isdigit():
            troopCount = int(troopCount)
            if troopCount in range(1, movableTroops+1):
                return troopCount
            else:
                print("Please choose a number within the appropriate range")
                return self.fortifyTroopCount(movableTroops)
        else:
            print("Please choose a number")
            return self.fortifyTroopCount(movableTroops)
        

    def fortify(self):
        startOptions = self.startOptionsFortify()
        fortifyStart = self.fortifyStart(startOptions)
        endOptions = self.endOptionsFortify(fortifyStart)
        fortifyEnd = self.fortifyEnd(endOptions)
        movableTroops = fortifyStart.getNumOfTroops() - 1
        troopCount = self.fortifyTroopCount(movableTroops)
        fortifyStart.removeTroops(troopCount)
        fortifyEnd.addTroops(troopCount)
            


        
##    Displays (ex.)
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
        cards = ""
        for card in self.getCards():
            cards.append(str(cards))
            cards.append(" ")
        return"Player: %s \nNumber: %s \nTotal troops: %d \nCountries occupied: \n%s\nCards Holding: %s" % \
               (self.__name, self.__number, self.getTotalTroops(), countriesStr, cards)



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

    def removeTroops(self, troops):
        self.__numOfTroops -= troops
    



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


#Asks if player wants to fortify
def fortifyDecision():
    answer = input("Do you want to fortify any troops? (0 for no, 1 for yes): ")
    return decision(answer)

    
#Asks if player wants to attack
def attackDecision():
    answer = input("Do you want to attack a country? (0 for no, 1 for yes): ")
    return decision(answer)

#Checks to see that the decision was a boolean
def decision(answer):
    if answer.isdigit():
        answer = int(answer)
        if answer == 0 or answer == 1:
            return bool(answer)
        else:
            print("This is not an acceptable number")
            return attackDecision()
    else:
        print("Please choose a number")
        return attackDecision()

    
#Play the fixed game to completion
def fixedGame(game):
    while len(game.getPlayers()) > 1:
                #Each player plays turn
                players = game.getPlayers()
                for i in range(len(players)):
                    #Insures that a player who dies does not still play this turn
                    if len(game.getPlayers()) > i:
                        player = players[i]
                        player.draftFixed()
                        numCountriesOccupiedStart = len(player.getCountriesOccupied())
                        attackBool = attackDecision()
                        while attackBool:  
                            player.attack(game)
                            attackBool = attackDecision()
                        numCountriesOccupiedEnd = len(player.getCountriesOccupied())
                        if numCountriesOccupiedEnd > numCountriesOccupiedStart:
                            player.addCard()
                        if fortifyDecision():
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
                        player.draftProgressive(game)
                        print("draft done")
                        numCountriesOccupiedStart = len(player.getCountriesOccupied())
                        attackBool = attackDecision()
                        while attackBool:  
                            player.attack(game)
                            attackBool = attackDecision()
                        numCountriesOccupiedEnd = len(player.getCountriesOccupied())
                        if numCountriesOccupiedEnd > numCountriesOccupiedStart:
                            player.addCard()
                        if fortifyDecision():
                            player.fortify()
                game.addTurn()

                
def gameType():
    gameOption = input("What kind of game do you want to play? ('fixed', 'progressive'): ")
    gameOptions = ['fixed', 'progressive']
    if gameOption in gameOptions:
        return gameOption
    else:
        print(gameOption, " is not an available option!")
        return gameType()
    
def main():
    print("Welcome to Risk by Joshua Renault")
    gameChoice = gameType()
    game = Game(gameChoice)
    game.printPlayers()
    print("The ", gameChoice, " game will now begin")
    gameOptions = ['fixed', 'progressive', 'random']
    if gameChoice == gameOptions[0]:
        progressiveGame(game)

    elif gameChoice == gameOptions[1]: 
        fixedGame(game)

main()
