import random
import sys


def main():
    score = 1000

    print("Guess a number between 100 and 1000")
    number = random.randint(100, 1000)
    # Splits the number to guess in part to use it as clues
    split = [int(i) for i in str(number)]
    print(number)

    print("Enter first guess")
    guess1: int = guess()

    if guess1 == number:
        print("You have win")
        print("Your score is " + str(score))
        sys.exit()
    else:
        score = update_score(score, guess1, number)
        print("Let's try again")
        print("The number starts with " + str(split[0]))

        print("Enter second guess")
        guess2: int = guess()

        if guess2 == number:
            print("You have win")
            print("Your score is " + str(score))
            sys.exit()
        else:
            score = update_score(score, guess2, number)
            print("More luck next time")
            print("Here is another hint " + str(split[0]) + str(split[1]))

            print("Enter third guess")
            guess3: int = guess()

            if guess3 == number:
                print("You have win")
                print("Your score is " + str(score))
                sys.exit()
            else:
                score = update_score(score, guess3, number)
                print("Today isn't your day")
                print("The number was " + str(number))
                print("Your score is " + str(score))


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


# Updates the user score based on the difference from the input value to the solution
def update_score(score: int, value: int, number: int):
    # We add the score because if not we'd be doing + - (-), so we'd end up with a number bigger than 1000
    if number < value:
        new_score = score + number - value
        if new_score <= 0:
            print("You have loose because your current score is 0")
            sys.exit()
        return new_score

    if number >= value:
        new_score = score - (number - value)
        if new_score <= 0:
            print("You have loose because your current score is 0")
            sys.exit()
        return new_score


#   Starts the app
main()
