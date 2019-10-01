def average(a,b):
    return (a+b)/2

def square_root(num,low,high):
    '''Finds the square root of num by 
    playing the Number Guessing Game 
    strategy by guessing over the 
    range from "low" to "high"'''
    for i in range(20):
        guess = average(low,high)
        if guess**2 == num:
            print(guess)
        elif guess**2 > num: # "Guess Lower":
            high = guess
        else: # "Guess Higher"
            low = guess

    print(guess)

square_root(60,7,8)