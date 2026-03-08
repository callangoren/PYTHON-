import random
random_food = ["ramen", "crepe", "udon", "wagyu", "curry rice"]
print(random.choice(random_food))


#print(random.randint(1, 6))



for i in range (1, 11):
    if i % 2 == 0:
        print(f"{i} is even")
    else:
        print(f"{i} is odd")








''' Exercise 2: 
- Make a list of 6 food names
- Print a random choice from the food list
'''







numbers = [4, 15, 8, 23, 10, 17, 2]
count = 0
for num in numbers:
    if num > 10:
        count += 1
print(f"There are {count} numbers greater than 10.")








