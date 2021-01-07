import random
dice = ["-","-","-",
        "-","-","-","-"]

def display_dice():
    number = random.randint(1,6)        
    print(" " + dice[0] + dice[1] + dice[2] + dice[3] + dice[4] + dice[5] + dice[6])
    print("|" + " " + " " + " " + " " + " " + " " + " " + "|")
    print("|" + " " + " "  , number , " " + " " + "|")
    print("|" + " " + " " + " " + " " + " " + " " + " " + "|")
    print(" " + dice[0] + dice[1] + dice[2] + dice[3] + dice[4] + dice[5] + dice[6])
def dice_roll():
    Roll_the_dice = "yes"
    while Roll_the_dice == "yes" or "y":
        display_dice()
        Roll_the_dice = input('Enter "yes" or "y" to Roll the Dice : ') 
dice_roll()    