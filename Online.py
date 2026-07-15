#Create a list of numbers. Make a new list that contains only the even numbers from the original list. Print the new list.
import random
numbers = [1, 6, 9, 105, 8]
new_numbers = []
for i in range(len(numbers)):
    if numbers[i] % 2 == 0:
        new_numbers.append(numbers[i])
print(new_numbers)



#Create a list of numbers. Make a new list containing only the numbers greater than 10. Print the new list.
numberss =  [21, 4, 7, 835, 50]
greater = []
for i in range(len(numberss)):
    if numberss[i] > 10:
        greater.append(numberss[i])
print(greater)

#Create a list of words. Count how many words have more than 5 letters.
words_the_first = ["hurray", "python", "fun", "!"]
count = 0
for i in range(len(words_the_first)):
    if len(words_the_first[i]) > 5:
        count += 1
print(count)

 #Create a list of words. Make a new list containing only the words that are written completely in uppercase.   
words_the_second = ["END", "hi", "HALO" ]
words_the_awakening = []
for i in range(len(words_the_second)):
    if words_the_second[i].isupper():
        words_the_awakening.append(words_the_second[i])
print(words_the_awakening)

#Create a list of words. Replace every word with fewer than 5 letters with the string "short".
words_the_third = ["long", "live", "third", "hurray"]
for i in range(len(words_the_third)):
    if len(words_the_third[i]) < 5:
        words_the_third[i] = "short"
print(words_the_third)

#Create a list of words. Count how many times the word "apple" appears.
words_the_fourth = ["fourth", "shall", "LIVE", "for", "apple"]
count_the_first = 0
for i in range(len(words_the_fourth)):
    if "apple" == words_the_fourth[i]:
        count_the_first += 1
print(count_the_first)


if random.randint(1, 4096) == 1:
    print("✨ SHINY ENCOUNTER! ✨")
else:
    print("Just a normal Pokémon... boring.")


class Pokemon:
    def __init__(self, name, type):
        self.name = name
        self.type = type

        self.is_shiney = random.randint(1, 4096) == 1
    def show(self):
        prefix = "✨ SHINY " if self.is_shiney else ""
        print(f"Wild {prefix}{self.name} appeared! (Type: {self.type})")
my_team = [
    Pokemon("Gengar", "Ghost"),
     Pokemon("Charizard", "Fire"),
       Pokemon("Pikachu", "Electric")
       ]



wild_encounter = random.choice(my_team)
wild_encounter.show()





words = ["banana", "equals", "fun"]
wonk = 0
for word in words:
    wonk += len(word)
    
print(wonk)


numbers = [1, 99, 3, 5]
total = 0 
for i in range(len(numbers)):
    total += numbers[i]
average = total / len(numbers)
print(average)


numbers_two = [1, 99, 3, 5]
new = []
totals = 0 
for i in range(len(numbers)):
    totals += numbers_two[i]
averages = totals / len(numbers)
for i in range(len(numbers_two)):
    if average < numbers_two[i]:
        new.append(numbers_two[i])
print(new)

from dataclasses import dataclass
@dataclass
class User:
    name: str
    age: int

person = User("Alice", 25)
print(person)


code = ["print", "ursina", "loops"]


for index, fruit in enumerate(code):
    print(f"Index{index} is code {code}")



strings = ["Python", "is", "nice"]
result = ""
for word in strings:
    result += word[0]
print(result)




password2 = "hello123!" 
for character in password2:
    if character.isdigit():
        has_number = True
    elif character == "!":
        has_special = True

if len(password2) >= 8 and has_number and has_special:
    print("Strong password")
else:
    print("Weak password")


price = [20, 30, 50]
total_price = sum(price)

if total_price >= 100:
    final_total = total_price * 0.8
else:
    final_total = total_price
print(final_total)


sentence = "python is fun to learn"
total_length = 0
new_stuff = []
words = sentence.split()
for word in words:
    total_length += len(word)
average_length = total_length / len(words)
for word in words:
    if len(word) > average_length:
        new_stuff.append(word)
print(new_stuff)







cards = ["Kabutops", "Charizard", "Gengar"]
values = [50, 200, 1000]
card_market = {card: value for card, value in zip(cards, values)}
print(card_market)











price5 = [20, 30, 50]
total = 0
for price in price5:
    total += price
print(total)



names = [" paul", "ALEX ", " maria ", "jOhN"]
new_names = []
for name in names:
    clean = name.strip().lower().capitalize()
    new_names.append(clean)
print(new_names)

words = ["book", "cat", "tree", "dog", "hello", "goddessship"]
for word in words:
    has_double_letter = False
    for i in range(len(word) - 1):
        if word[i] == word[i + 1]:
            has_double_letter = True
    if has_double_letter == True:
        print(word)

wordss = ["cat", "education", "tree", "banana"]
vowels = "aeiou"
max_count = 0
for word in wordss:
    vowel_count = 0
    for character in word:
        if character in vowels:
            vowel_count += 1
    if (vowel_count > max_count):
        max_count = vowel_count
        max_word = word
print(max_word)

grades = [85, 92, 67, 74, 100, 58, 90]
failing_grades = []
winning_grades = []
average = sum(grades) / len(grades)
print("Average:", average)
print("Highest:", max(grades))
print("Lowest:", min(grades))
for grade in grades:
    if grade >= average:
        winning_grades.append(grade)
    else:
        failing_grades.append(grade)
    
print("Beyond average:", winning_grades)
print("Below average:", failing_grades)
    



def count_words(word_list, word):
    count = 0
    for element in word_list:
        if element == word:
            count += 1
    return count


sentence = "python is fun and python is useful"
seen_words = []
words = sentence.split()
for word in words:
    if word not in seen_words:
        seen_words.append(word)
        count = count_words(words, word)
        print(word, "=", count)


    
        

def add(a, b):
    total = a + b
    return total
c = add(1, 5)
print(c)


def output(word):
    print(word)

output("こにちわ")

words = ["apple", "banana", "grape", "orange", "cat", "pineapple"]
search = "range"
fruiiiiiiits = []
for word in words:
    if search in word:
        fruiiiiiiits.append(word)
print(fruiiiiiiits)


# Write a function convert_to_seconds(hours, minutes, seconds) 
# that takes a nonnegative integer  number of hours, minutes, 
# and seconds as its parameters, and returns the total number of seconds in that time period

def convert_to_seconds(hours, minutes, seconds):  
    return hours * 3600 + minutes * 60 + seconds  
a = convert_to_seconds(1, 1, 1)
b = convert_to_seconds(2, 1, 1)
print(a + b)


# The formulas for converting between Fahrenheit temperatures and Celsius temperatures are:
# C = 5/9 (F - 32)
# F = 32 + 9/5 * C
# Write functions to perform these conversions.


def fahr_to_cels(temperature):
    return (5/9) * (temperature - 32) 


def cels_to_fahr(temperature):
    return 32 + (9/5) * temperature
    
a = cels_to_fahr(fahr_to_cels(37))
print(a)


# write a function letter_square(letter, size) that takes as input a string letter consisting of a single character, and a positive integer size
# The function should return a string that prints a size-by-size square of letter.
# For example, print(letter_square('x', 5)) should print
# xxxxx
# xxxxx
# xxxxx
# xxxxx
# xxxxx

def letter_square(letter, size):
    square = ""
    for i in range(size):   
        square += (letter * size) + "\n"

    return square

print(letter_square('x', 1)) 


def letter_triangle(letter, height):
    cube = ""
    for i in range(height):
        cube += (letter * (i + 1)) + "\n"
    return cube
print(letter_triangle('y', 4))


def check_battle(attack_power, defense):
    if attack_power > defense:
        return "you won!"
    else:
        return "The monster blocked your attack."
result1 = check_battle(10, 5)
result2 = check_battle(3, 8)

print(result1) 
print(result2)




    



def count_long_words(text, min_length):
    words = text.split() # <- why is not glowing up?
    count = 0 # <- the bucket
    for word in words: # <- the loop needed to run more than once
        if len(word) >= min_length: # <- if it's smaller than min_length!
            count += 1 # <- you add so you get an anwser

    return count # <- you spill the bucket like a print!


def student_report(text):
    names = ""
    for name in names:
        word_two = name.split() + "\n"
    






