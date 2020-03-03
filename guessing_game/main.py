#!/bin/usr/python3 *

class Game:
    def __init__(self, secret):
        self.secret = secret    # The generated secret.
        self.tries = 0            # Track the tries.
        self.guess = []       # Track the guesses.
        self.run = True         # If the game runs or not.

    def trackUserScore(self, user_input):
        """ Check if the guess was already placed or not. """
        if not int(user_input) in self.guess:
            self.guess.append(int(user_input))
            self.tries = self.tries + 1

    def compareUserInput(self, user_input):
        """ Take the user input and compare it with the secret. """
        if int(user_input) == self.secret:
            # Guessed the secret correctly.
            print("You did it! Well done!")
            self.run = False
        elif int(user_input) < self.secret:
            # The input was to low.
            print("Your input was to low, try again.")
            Game.trackUserScore(self, user_input)
        elif int(user_input) > self.secret:
            # The input was to high.
            print("Your input was to high, try again.")
            Game.trackUserScore(self, user_input)

    def verifyUserInput(self, user_input):
        """ Check if the user input is a correct integer. """
        error = False
        try:
            int_uip = int(user_input)
        except ValueError:  # Happens if not convertable to int.
            error = True
            err_msg = "Please provide numbers only.\n"
        except Exception:   # Something went badly wrong.
            error = True
            err_msg = "Something went wrong, could not convert your input.\nPlease try again.\n"
        # Check for errors, print/return the error if happened.
        if error:
            print(err_msg)
        return error


def createSecret(min, max):
    """ Create the secret that's going to be guessed. """
    import random
    secret = random.randint(min, max)
    return secret

def main():
    # Initialize the game.
    game = Game(createSecret(1, 100))
    #print(game.secret)
    print("Welcome to the guessing game :)")
    while game.run == True:
        user_input = input("\nYour guess: ")
        if game.verifyUserInput(user_input) == False:   # If returns false, no error occured (error = false).
            game.compareUserInput(user_input)        
    print(f"\nIt took you {game.tries} tries.")


if __name__ == '__main__':
    main()
