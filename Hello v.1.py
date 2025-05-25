import sys
import time

print("Hello!\nSay Hello back? (y/n)")
hello = input()

while hello != "y" and hello != "n":
    print("It is y or n.\nThere is no other choice...")
    hello = input()

if hello == "y":
    print("*You said Hello back. Good job!*")
elif hello == "n":
    print("*You refused to say Hello back. How rude...*")
    
time.sleep (3)
sys.exit()
