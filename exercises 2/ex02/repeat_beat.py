"""Repeating a beat in a loop."""

__author__ = "730393720"


# Begin your solution here...
minimum: int = 0
beat: str = str(input("what beat do you what to repeat?"))
number: int = int(input("How many times do you want to repeat it?"))
maximum: int = number
while number < minimum:
    print("No beat...")
    number = number - number
while number > minimum:
    print(beat * number)
    number = number - number