# This function is a brute force method of plugging 
# in all possible whol integers between -100 and 100.
# This is not what would be considered elegant, but 
# it does work.

def plug():
    x = -100
    while x < 100:
        if 2*x +5 == 13:
            print("x=",x)
        x += 1

plug()

def g(x):
    return 6*x**3 + 31*x**2 +3*x -10

def plug_cubic():
    x = -100
    while x < 100:
        if g(x) == 0:
            print("x =", x)
        x += 1

plug_cubic()