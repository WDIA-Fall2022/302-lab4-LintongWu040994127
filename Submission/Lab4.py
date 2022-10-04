# Stundent name: Lintong Wu
# Student number: 040994127
# Section: 302

from cgitb import grey
from secrets import choice
from sense_emu import SenseHat
import time

s = SenseHat()
s.low_light = True

green = (0,255, 0)
yellow = (255,255, 0)
blue = (0, 0,255)
red = (255, 0, 0)
white = (255,255,255)
nothing = (0,0,0)
pink = (255,105, 180)

def trinket_logo():
    G = green
    Y = yellow
    B = blue
    O = nothing
    logo = [
    O, O, O, O, O, O, O, O,
    O, Y, Y, Y, B, G, O, O,
    Y, Y, Y, Y, Y, B, G, O,
    Y, Y, Y, Y, Y, B, G, O,
    Y, Y, Y, Y, Y, B, G, O,
    Y, Y, Y, Y, Y, B, G, O,
    O, Y, Y, Y, B, G, O, O,
    O, O, O, O, O, O, O, O,
    ]
    return logo

def raspi_logo():
    G = green
    R = red
    O = nothing
    logo = [
    O, G, G, O, O, G, G, O, 
    O, O, G, G, G, G, O, O,
    O, O, R, R, R, R, O, O, 
    O, R, R, R, R, R, R, O,
    R, R, R, R, R, R, R, R,
    R, R, R, R, R, R, R, R,
    O, R, R, R, R, R, R, O,
    O, O, R, R, R, R, O, O,
    ]
    return logo

def plus():
    W = white
    O = nothing
    logo = [
    O, O, O, O, O, O, O, O, 
    O, O, O, W, W, O, O, O,
    O, O, O, W, W, O, O, O, 
    O, W, W, W, W, W, W, O,
    O, W, W, W, W, W, W, O,
    O, O, O, W, W, O, O, O,
    O, O, O, W, W, O, O, O,
    O, O, O, O, O, O, O, O,
    ]
    return logo

def equals():
    W = white
    O = nothing
    logo = [
    O, O, O, O, O, O, O, O, 
    O, W, W, W, W, W, W, O,
    O, W, W, W, W, W, W, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, W, W, W, W, W, W, O,
    O, W, W, W, W, W, W, O,
    O, O, O, O, O, O, O, O,
    ]
    return logo

def heart():
    P = pink
    O = nothing
    logo = [
    O, O, O, O, O, O, O, O,
    O, P, P, O, P, P, O, O,
    P, P, P, P, P, P, P, O,
    P, P, P, P, P, P, P, O,
    O, P, P, P, P, P, O, O,
    O, O, P, P, P, O, O, O,
    O, O, O, P, O, O, O, O,
    O, O, O, O, O, O, O, O,
    ]
    return logo

def elephant():
    G = blue
    O = nothing
    W = white
    logo = [
        O, O, G, G, O, O, O, O,
    O, G, G, G, G, G, G, O,
    G, O, G, G, G, G, G, G,
    G, G, G, G, G, G, G, G,
    G, W, W, G, G, G, G, G,
    G, O, G, G, G, G, G, G,
    G, O, G, G, O, G, G, O,
    G, O, W, G, O, W, G, O,
    ]
    return logo

images = [trinket_logo, trinket_logo, plus, raspi_logo, raspi_logo, equals, heart, heart]

while True:
        print("\nWhat do you want to display (0. to exit): ")
        print("1. Logo")
        print("2. Plus sign")
        print("3. Equals sign")
        print("4. Raspberry")
        print("5. Heart")
        print("6. Elephant")
        print("0. Exit")
        
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print('Please enter the choice number')

        if choice == 1:
            s.set_pixels(trinket_logo())
        
        elif choice == 2:
            s.set_pixels(plus())

        elif choice == 3:
            s.set_pixels(equals())

        elif choice == 4:
            s.set_pixels(raspi_logo())

        elif choice == 5:
            s.set_pixels(heart())
        
        elif choice == 6:
            s.set_pixels(elephant())

        elif choice == 0:
            break

        

        

