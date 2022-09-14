import math
import random

trials = 50

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

## Takes in initial troop count (myTroops) and list of enemyTroops along your path
def whatPath(myTroops, enemyPath):
    result = [myTroops, 0, True]
    countriesConquered = 0
    for enemyTroops in enemyPath:
        result = whoWins(result[0], enemyTroops)
        if result[2]:
            countriesConquered += 1
        else:
            break
    result.append(countriesConquered)
    return result ##[myTroops, enemyTroops, Boolean, countriesConquered]
        


## Prints the result of many trials
def manyTimes(myTroops, enemyPath):
    myTroopsLost = 0
    numberOfVictories = 0
    totalCountriesConquered = 0
    for i in range(trials):
        result = whatPath(myTroops, enemyPath)
        if result[2]:
            myTroopsLost += myTroops - result[0]
        totalCountriesConquered += result[3]

        if result[2]:
            numberOfVictories += 1

           
    aveTroopsLost = round((myTroopsLost/numberOfVictories)-len(enemyPath))
    winProbability = numberOfVictories/trials
    troopsAtEnd = myTroops - round(myTroopsLost/numberOfVictories)
    aveCountriesConquered = round(totalCountriesConquered/trials)

    #Prints associated results
    print()
    print("\nProbability of success:", winProbability, "\n")
    print("Average troop loss given a win:", aveTroopsLost, "\n")
    print("Average big troop count given a win:", troopsAtEnd, "\n")
    print("Average countries conquered:", aveCountriesConquered, "\n")
    print("Number of Trials:", trials)

        
## Takes enemy path and my troops to determine probability of success        
def main():
    enemyPath = []
    enemyPathStr = input("What is the enemy path? (ex. 1,1,1,1,5): ")
    enemyPathStr = enemyPathStr.split(',')
    for i in enemyPathStr:
        enemyPath.append(int(i))
    myTroops = int(input("\nHow many of our troops are going into this battle? "))
    manyTimes(myTroops, enemyPath)

main()    



            
