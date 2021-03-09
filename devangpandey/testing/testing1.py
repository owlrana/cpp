from __future__ import print_function
import random
import math

def generateOne(strlen):
    alphabts = "abcdefghijklmnopqrstuvwxyz "
    s = ""
    for i in range(strlen):
        ran = random.randint(0,26)
        s=s+alphabts[ran]
    return s    

def score(goal,testString):
    numSame = 0
    for i in range(len(goal)):
        if(goal[i]==testString[i]):
            numSame=numSame+1
    return (numSame/float(len(goal)))

def main():
    goalString = "methinks it is like a weasel"
    newString = generateOne(28)
    best = 0
    newScore = score(goalString,newString)
    for i in range(10):
        print(newScore)
        if newScore>best:
            print(newScore,newString)
            best = newScore
        newString = generateOne(28)
        newScore = score(goalString,newString)

main()


