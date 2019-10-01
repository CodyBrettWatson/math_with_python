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