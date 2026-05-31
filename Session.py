
numbers = [1, 0, 14, 9, 5]
total = 0
for number in numbers:
     if number % 2 == 0:
        total = total + 1
print(f"There are {total} even numbers in your list")
 #-------------------------------------------------------------------------       
numbers = [1, 13, 10, 9, 5]
total = 0
for number in numbers:
     if number % 2 != 0:
        total = total + number
print(f"The sum is now {total}")








 


words = ["apple", "Banana", "kiwi"]
for word in words:
    if word[0].isupper():
        print(word)
    

words = ["apple", "Banana", "kiwi"]
count = 0 
for word in words:
    if word.istitle():
        count = count + 1
        print(f"There are {count} capital words in this list")


sentence = "python is fun"
sentence = sentence.split()
print(sentence)

secret_message = "blue red green yellow"
secret_message = secret_message.split
print(secret_message)

bag = ["apple", "banana", "cherry"]
print(len(bag))


word = "python"
print(len(word))


price = float("19.99")
print(price + 1)

pi = 3.178172
print(round(pi, 6))


x = 1
print(type(x))


math = [-1, 6, -9]
for i in range(len(math)):
    if math[i] < 0:
        math[i] = 0
print(math)




words = ["python", "is", "awesome", "coding", "fun"]
for n in numbers:
 new_word  = [word.upper() for word in words if len(word) > 3]
print(new_word)


caps = ["HI, HELLO, SUP "]

new_cap = [word.lower() for word in caps]
print(new_cap)

        
grade = [90, 80, 50, 40]
passing = []
failing = []
for i in range(len(grade)):
    if grade[i] >= 70:
        passing.append(grade[i])
    else:
        failing.append(grade[i])
print("passing grades:", passing)
print("failing grades:", failing)

user = {
"name": "Alex",
"age": "25",
"city": "manila",
}
print(user["name"]) 
print(user["age"])

inventory = {"gold": 50, "potion": 2, "sword": 1}
for item, amount in inventory.items():
    print(f"You have {amount} of {item}")

my_car = {
    "brand": "BMW",
    "year": "2006",
    "model":"WHO CARES",
}
my_car["model"] = "5 Series"
print(my_car["model"])



stuffs = ["coding", "habits", "bland", "fun"]
for stuff in stuffs:

    if (length := len(stuff)) > 3:
            print(f" the word {stuff}' has {length} letters")

words = ["coding", "habits", "bland", "fun", "a"]
judgement = [f"'{w}' is big" if len(w) > 4 else f"'{w}' is tiny" for w in words]
print(judgement)


calculate = lambda p, d, t: round((p * (1 - d / 100)) * (1 + t / 100), 2)
print(f"Total for shoes: ${calculate(100, 20, 8)}")

import random; print("The scream" if random.random() > 0.5 else "The shhhheam")