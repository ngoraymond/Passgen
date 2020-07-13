import random
import math
import numpy as np
import matplotlib.pyplot as plt

def numSelect(x):
    if(x < 6):
        return [random.randint(0,5)]
    dieRoll = random.randint(0,5)
    base = x//6
    val = [dieRoll] + numSelect(base)
    return val

def numSelecter(x):
    guess = numSelect(x)[::-1]
    num = 0
    for z in range(len(guess)):
        num += guess[z]*(6**z)
    if num >= x:
        return numSelecter(x)
    return num

def main():
    
    numRolls = int(input("Input the max size of your random number: "), base=10)
    numTimes = int(input("Number of times to test: "), base = 10)
    values = [0] * numRolls
    for z in range(numTimes):
        num = numSelecter(numRolls)
        if(num >= numRolls):
            print("ERROR")
            break
        values[num] += 1
    print(values)
    plt.plot(values)
    plt.show()

if __name__ == "__main__":
    main()