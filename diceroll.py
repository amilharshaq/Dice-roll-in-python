import random
dice = ["-","-","-",
        "-","-","-","-"]

def display_dice():
    number = random.randint(0,6)        
    print(" " + dice[0] + dice[1] + dice[2] + dice[3] + dice[4] + dice[5] + dice[6])
    print("|" + " " + " " + " " + " " + " " + " " + " " + "|")
    print("|" + " " + " "  , number , " " + " " + "|")
    print("|" + " " + " " + " " + " " + " " + " " + " " + "|")
    print(" " + dice[0] + dice[1] + dice[2] + dice[3] + dice[4] + dice[5] + dice[6])

Roll_the_dice = input('Enter "roll" or "Roll" to Roll the Dice : ')
if Roll_the_dice == "roll" or "Roll":
    display_dice()
