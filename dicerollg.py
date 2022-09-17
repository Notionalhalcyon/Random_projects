import random

dice_list = ("d4", "d6", "d8", "d12", "d20")

print("Dice List:")
for dice in dice_list:
    print(dice)
while True:
    chosen_dice = input("Which dice would you like to use? ").lower()
    print(f"{chosen_dice} selected")
    modifiers = int(input("What are your plus or minus modifiers? "))
    print(f"{modifiers} inputed")

    if chosen_dice == "d4":
        roll = random.randint(1, 4)
        totalroll = roll + modifiers
        print(f"{roll} + {modifiers} or {totalroll} is your roll!")

    elif chosen_dice == "d6":
        roll = random.randint(1, 6)
        totalroll = roll + modifiers
        print(f"{roll} + {modifiers} or {totalroll} is your roll!")

    elif chosen_dice == "d8":
        roll = random.randint(1, 8)
        totalroll = roll + modifiers
        print(f"{roll} + {modifiers} or {totalroll} is your roll!")

    elif chosen_dice == "d12":
        roll = random.randint(1, 12)
        totalroll = roll + modifiers
        print(f"{roll} + {modifiers} or {totalroll} is your roll!")

    elif chosen_dice == "d20":
        roll = random.randint(1, 20)
        totalroll = roll + modifiers
        print(f"{roll} + {modifiers} or {totalroll} is your roll!")