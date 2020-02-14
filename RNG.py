import random
import math
import numpy as np
import matplotlib.pyplot as plt

def numSelecter(x):
    if(x <= 1):
        return 0
    dieRoll = random.randint(1,6)
    if(dieRoll % 2 == 0):
        return x//2 + numSelecter(x//2)
    else:
        return numSelecter(x//2)

def main():
    numRolls = 30
    values = [0] * numRolls
    for z in range(1000):
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