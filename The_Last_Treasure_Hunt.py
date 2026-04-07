#import random
'''
Locations = ["forest", "river", "cave", "mountain", "beach", "rainforest", "savannah", "grassland"]
Treasure = random.randint(0, len(Locations) -1)
for i in range(0, len(Locations)):
    print("Let us start exploring the", Locations[i])
    if i == Treasure:
        print("You did it! We wil be rich!!!")
        break
    else:
        print("Well lets try again boys.... ")
print("---------------------------------------------------------------------------------------------------------")

Treasure = random.choice(Locations)
print(Locations)
interaction = ""
while interaction != Treasure:
    interaction = input("Where do you think the treasure is ma boy? ")
    if interaction == Treasure:
        print("YES WERE RICH RICH!")
    else:
        print("Well NOW WE HAVE NO TREASURE")

'''



grade = int(input("Enter your grade level (1-12): "))

if 1 <= grade < 5:
        print("Elementary school")
elif 5 <= grade <= 8:
        print("Middle school")
elif 9 <= grade <= 12:
        print("High school")
else:
        print("Invalid grade")
 




             


























"A map is just a list of places we can explore."
"""
For example,
locations = ["forest", "river", "cave", "mountain", "beach"]

Be creative and make your own locations list
"""