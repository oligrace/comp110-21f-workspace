"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730393720"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
from random import randint


# Begin your solution here...
answer = (randint(1, 3))

print("Your fortune cookie says...")

if answer == 1:
    print("You will recieve an A in this class!")
else:
    if answer == 2:
        print("You will recieve good news soon!")
    else:
        if answer == 3:
            print("You will come into some money!")

print("Now go spread positive vibes")
