#coin flipper
import sys
import random
coin = input("press enter to flip a coin")
coin = random.randint(1,2)
if coin == 1:
    print("heads")
elif coin == 2:
    print("tails")
else:
    sys.exit("you should have pressed enter")
