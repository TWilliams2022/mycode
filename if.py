#!/usr/bin/env python3

import random

trys = 0

while True:

    trys += 1

    music = input("What is your favorite song? ")
    if music == " ":
         print("You may want to pick an actual song")
         break
    elif len(music) > 2: 
         print("Cool! Your favorite song is: " + music + "." )
         break
    else:
         print("You did not provide input.")


animal_list= ["Frog", "Lion", "Crocodile", "Antelope", "Mouse", "Cat", "Shrimp", "Moose", "Grizzly", "Shark", "Beta Fish", "Elk", "Hippo", "PEE WEE"]

print("Now that we have your favorite song... ")
print("Your song indicates that you are a.... ")
input("PRESS ENTER FOR RESULT")
print(random.choice(animal_list))
