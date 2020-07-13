import math

def f (Is, Vd, Vt):
    #function for Id
    return (Is)*(math.exp(Vd/Vt) - 1)

def fPrime (Is, Vd, Vt):
    #Function for Id'
    return (Is/Vt)*math.exp(Vd/Vt)

def looping (Vop, R, initGuess):
    #setup of problem parameters
    Is = 10**-11
    Vt = .025
    #initial guess
    x = initGuess
    #iterations
    for z in range(10000):
        #(Vop-V)/R = f(x) + f'(x)*(V - x)
        # V = (f(x) - f'(x)*(x) - Vop/100)/(-1/R - f'(x))
        x_new = (f(Is, x, Vt) - fPrime(Is, x, Vt)*x - Vop/R)/(-1*(1/R+fPrime(Is, x, Vt)))
        x = x_new
    #reporting of final solution
    return x

print("initial = 0.6: " + str(looping(5, 100, 0.6)))
print("initial = 0.1: " + str(looping(5, 100, .1)))
print(looping(5, 500000, .5))

