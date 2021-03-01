# An app created to encode a string given as an input
import sys

import dic
import decoder


# Main encode method
def encode():
    print("Let's encode a string")
    print("Select encoding method")
    # TODO: Print encode methods
    print("Okay, know select the input to code")

    encoder = str(input())
    split = [str(i) for i in str(encoder)]
    # print(split)

    result = map(code, split)
    joined = "".join(map(str, list(result)))

    print("Your encode string is : " + joined)


# It create a secure string based on the input
def code(item):
    return dic.defaultValue.get(item)


def main():
    print("If you want to encode a string type 0. If you want to decode a string type 1")
    try:
        selection = int(input())
        if selection == 0:
            encode()
        elif selection == 1:
            print("Please enter number to decode: ")
            number = str(input())
            decoder.decode(number, "tortilla")
        else:
            # TODO: Add ability to retype instead of exiting program
            print("Please select a valid option")
            sys.exit()
    except ValueError:
        print("You didn't introduce a number")
        sys.exit()


# Starts the app
main()
