import random

#Simulation of a wheel with 100 segments
#Each segment has a dollar on it, redeemable once if it lands on that number
#How much money will you have if you spin 100 times?
def guess():
    sum = 0
    wheel = [0] * 100
    for z in range(100):
        idx = random.randint(0,99)
        if(wheel[idx] == 0):
            sum += 1
            wheel[idx] = 1
    return sum

def main():
    runningSum = 0
    for z in range(1,1000):
        runningSum += guess()
        print(runningSum/z)

if __name__ == "__main__":
    main()