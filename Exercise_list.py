'''
schedule = ["wake up", "breakfast", "school"]
schedule[1] = "Eat breakfast"
print(schedule)
schedule.append("pack bag")
print(schedule)
schedule.append("Get on bike")
print(schedule)
schedule.insert(1, "brush teeth")
print(schedule)
schedule.insert(3, "do homework")
print(schedule)
schedule.insert(5, "eat lunch")
print(schedule)
'''












'''
Exercise:
Suppose we have a list of animals
Use extend to add 3 more animal strings into list_of_animals
'''
list_of_animals = ["shoebill"]
print(list_of_animals)
list_of_animals.extend(["bison", "peacocks", "spider monkeys"])
print(list_of_animals)
list_of_animals.remove("spider monkeys")
print(list_of_animals)

'''
toys = ["ball", "car", "doll"]

last_toy = toys.pop(2)
print(last_toy)
print(toys)
toys.append( "toy train")
print(toys)
'''

snacks = ["apple", "cookie", "banana", "cookie", "sandwich"]
print(snacks)
snacks_last = snacks.remove("cookie")
print(snacks)