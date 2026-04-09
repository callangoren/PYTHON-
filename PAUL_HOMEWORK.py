''''
word = input("enter a word: ")
count = 0
for character in word:
    if character in "eE":
        count = count + 1
print(count)
'''


user_input = input("Enter some text: ")
    
    # Initialize a counter
digit_count = 0
    
    # Iterate through each character in the string
for char in user_input:
        # Check if the character is a digit
        if char.isdigit():
            digit_count += 1
            
    # Display the result
print(f"The text contains {digit_count} digit(s).")

sentence = input("Enter a sentence: ")
    
    # Initialize a counter
count = 0
    
    # Loop through each character
for char in sentence:
        # Check if the character is not a space
        if char != " ":
            count += 1
            
    # Display the result
print(f"Number of characters (excluding spaces): {count}")



word = input("enter a word: ")
count = 0
for character in word:
    if character in "eE":
        count = count / 5
print(count)



def basic_detector(text):
     blacklist = ["shit", "fuck", "spam"]
     words = text.lower().split()
     found_words = [word for word in word if word in blacklist]
     if found_words:
          return True, found_words
     return False, []
message = "this is a toxic message"
is_bad, detected = basic_detector(message)
print(f"Contains bad word: {is_bad} ")

