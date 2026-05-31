'''
word = input("enter a word: ")
count = 0
for character in word:
    if character in "eE":
        count = count + 1
print(count)
'''

'''
user_input = input("Enter some text: ")
    
    
digit_count = 0
    
    
for char in user_input:
        
        if char.isdigit():
            digit_count += 1
            
    
print(f"The text contains {digit_count} digit(s).")

sentence = input("Enter a sentence: ")
'''  
    
count = 0
'''   
for char in sentence:
        if char != " ":
            count += 1
'''         
   
print(f"Number of characters (excluding spaces): {count}")


'''
word = input("enter a word: ")
count = 0
for character in word:
    if character in "eE":
        count = count / 5
print(count)
'''


text = input("Enter a word: ")
result = (" ")
for character in text:
      if character in text:
            result = character + result
print("\n the reversed string=", result )
      





sentence = input("Enter a sentence: ")

to_lower_changes = sum(1 for i in range(len(sentence)) if sentence[i] != sentence[i].lower())
to_upper_changes = sum(1 for i in range(len(sentence)) if sentence[i] != sentence[i].upper())

print(f"Characters that would change if converted to lowercase: {to_lower_changes}")
print(f"Characters that would change if converted to uppercase: {to_upper_changes}")

#-----------------------------------------------------------------------------#
text = input("Enter some text: ")

upper_count = 0
lower_count = 0

for char in text:
    if char.isupper():
        upper_count += 1
    elif char.islower():
        lower_count += 1

print(f"Uppercase letters count: {upper_count}")
print(f"Lowercase letters count: {lower_count}")

if upper_count > lower_count:
    print("There are more uppercase letters.")
elif lower_count > upper_count:
    print("There are more lowercase letters.")
else:
    print("Uppercase and lowercase counts are equal.")

print("-" * 30) # yay!


