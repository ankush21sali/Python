import random
def dice_rolling():
    dice = random.randint(1,6)
    return dice

print("Dice Rolling Simulator . . .")

while True:
    roll = input("Enter {yes/no} for Dice Rolling : ").lower()

    if roll == "yes":
        print("Dice Rolled : ",dice_rolling())

    elif roll == "no":
        print("\nThanks for Playing . . .")
        break

    else:
        print("Wrong input, please Enter {yes/no}")
