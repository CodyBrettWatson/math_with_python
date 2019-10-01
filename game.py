from random import randint

def number_game():
    #choose a random number
    #between 1 and 100
    number = randint(1,100)
    
    print("I'm thinking of a number between 1 and 100.")
    guess = int(input("What's your guess?"))

    while guess:
        if number == guess:
            print("Correct, the number was, ", number)
            break
        elif number > guess:
            print("Higher")
        else:
            print("Lower")
        guess = int(input("What's your guess?"))
    

def greet():
    name = input("What's your name?")
    print('Hello, ',name)

def whole_game():
    greet()
    number_game()

whole_game()