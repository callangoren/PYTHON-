level_input = input("whats your level")
coins_collected_input = input("how many coins do you have")
level = int(level_input)
coins_collected = int(coins_collected_input)

if level >= 50 and coins_collected >= 100:
    print("Advance to the even harder levels!")
else:
    print("Thats a shame you have to try again!")