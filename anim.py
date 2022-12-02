import os
import time

def animation():
    x = 0
    while x < 20:
        x += 1
        print("Calculating.   \\")
        time.sleep(0.05)
        os.system('cls||clear')
        print("Calculating..  |")
        time.sleep(0.05)
        os.system('cls||clear')
        print("Calculating... /")
        time.sleep(0.05)
        os.system('cls||clear')
        print("Calculating.   -")
        time.sleep(0.05)
        os.system('cls||clear')

    input("Results are in: you're a bitch")  
