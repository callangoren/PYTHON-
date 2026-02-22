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

import time
print("I am watching.....")
time.sleep(1)
print("....like a hawk!")





'''
Warm-up exercise:
5. use remove to get rid of the first 4 in list_of_integers
6. use pop to get rid of the last 4 in list_of_integers

Print out list_of_integers after each step to check your work
'''

                        # 2 #3    #5 #6
list_of_integers = [2, 3, 4, 4, 5, 4, 4]

list_of_integers[5] = 6
#list_of_integers.insert(0, 1)

print(list_of_integers)

list_of_integers.remove(4)
print(list_of_integers)

list_of_integers.pop(5)
print(list_of_integers)


'''
Practice: create a guest list manager

Make a list variable and start it with 4 guests (any names you like)
Use input to ask the user to enter a new guest name
If the name is already in the list, print a message like "They're already invited!"
If not, add this name to the list and then print a message like "Added to the guest list."
Print the updated guest list
'''
'''
guest_list = ["Jon", "Bob", "jim", "Tim"]
New_guest = input("Enter a new guest")
if New_guest in guest_list:
    print("they are already invited")
    
else:
    guest_list.append(New_guest)
    print("Invited", guest_list)
'''

fruits_boom = ["apple", "banana","guava","lemon","orange" ]
new_fruit = input("enter a new fruit")
if new_fruit in fruits_boom:
    print("This fruit exists in the list no need for 1 more!")
else:
    fruits_boom.append(new_fruit)
    print("In the list now!", fruits_boom)

banned_list = ["blox","hwjssw","#####","55555","123988"]
new_ban = input("enter a banned username")
if new_ban in banned_list:
    print("this username is already banned")
else:
    banned_list.append(new_ban)
    print("the username is now banned", banned_list)













    '''
Warm-up practice:

Create a shopping cart list and print it out
Ask the user which item they want to remove
Allow the user to remove an item only if it exists in the cart
If the item is not found, print an appropriate message
'''
      
        