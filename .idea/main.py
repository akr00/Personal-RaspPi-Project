# Created by: Aiden Ridgeway
#

import random
from time import sleep
import os

play = 1

output = []
count = 0
score = 0

def cls(): print("\n" * 50)  # moves current text off of the screen


while play == 1:
    a = (random.randint(1, 4))
    output.append(a)
    print("Ready...")
    sleep(.5)
    cls()
    for val in output: # shows each value in the list once, on its own screen
        print(val)
        sleep(1)
        cls()
        sleep(.5)

    print("Enter all of the previous values")
    for val in output:  # reads each value individually and compares it to expected value to see if the user is correct
        i = 0
        i = input()
        i = int(i)
        if i != val:
            play = 0

    score = str(len(output))
print("Your Score was: " + score)
