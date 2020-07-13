import math

def inductance (x, y, h, b, N):
    s = x + y + 2*h
    return (.0276*s*s*N*N)/(1.908*s+9*b+10*h)

def turnFinder (x, y, h, b, L):
    s = x + y + 2*h
    return math.sqrt(L*(1.908*s+9*b+10*h)/(.0276*s*s))

print(turnFinder(3.81, 3.81, .25, .25, 300))

print(inductance(3.81, 3.81, .25, .25, 67))

print(turnFinder(19.05, 8.89, .25, .25, 1500))