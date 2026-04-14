def basic_detector(text):
     blacklist = ["shit", "fuck", "spam", "bitch", "dick", "retard", "cunt" ]
     words = text.lower().split()
     found_words = [word for word in words if word in blacklist]
     if found_words:
          return True, found_words
     return False, []
message = input("Type a message to test: ")
#message = "this is a toxic message" if you want manual this is good
is_bad, detected = basic_detector(message)
#print(f"Contains bad word: {is_bad} ") manual
if is_bad:
     print(f"🚫 Alert! Found these blocked words: {detected}")
else:
     print("✅ Message is clean!")
