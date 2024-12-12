from random import randint as r
from colorist import ColorHex as Color

grey = Color("#676767")
red = Color("#FF0000")

def inp(string_input):
    string_input += f" {grey}(Press ENTER to continue){grey.OFF}"
    input(string_input)
    return string_input


def start():
    input("--PYTHON GUESSING THE NUMBER GAME!!! PRESS ENTER TO CONTINUE!!!--")
    inp("\nHello and welcome!")
    inp("The rules are simple!")
    inp("I will pick a number from a certain range...")



start()