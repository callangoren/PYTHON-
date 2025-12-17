level_input = input("what is your level?")
coins_collected_input = input("how many coins do you have?")
level = int(level_input)
coins_collected = int(coins_collected_input)

if level >= 5 and coins_collected >= 10:
    print("Advance to the next level!")
else:
    print("keep playing!")