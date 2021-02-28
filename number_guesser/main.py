import random
import sys


def main():
    print("Guess a number between 0 and 1000")
    number = random.randint(0, 1000)
    split = [int(i) for i in str(number)]

    print("Enter first guess")
    guess1: int = guess()

    if guess1 == number:
        print("You have win")
        sys.exit()
    else:
        print("Let's try again")
        print("The number starts with " + str(split[0]))

        print("Enter second guess")
        guess2: int = guess()

        if guess2 == number:
            print("You have win")
            sys.exit()
        else:
            print("More luck next time")
            print("Here is another hint " + str(split[0]) + str(split[1]))

            print("Enter third guess")
            guess3: int = guess()

            if guess3 == number:
                print("You have win")
                sys.exit()
            else:
                print("Today isn't your day")
                print("The number was " + str(number))


# Collects the user type
def guess():
    # Checks that a number is introduced
    try:
        value = int(input())
        return value
    except ValueError:
        print("You didn't introduce a number")
        print("Let's try again. Introduce a number")
        try:
            value = int(input())
            return value
        except ValueError:
            print("You have again introduce a non valid answer. Start again the game in case you want to play")
            sys.exit()


# Starts the app
main()
