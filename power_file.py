password = input("whats your password")
if len(password) < 6:
    print("not very good password")
elif len(password) <= 10:
    print("good password")
else:
    print("great password!!!")





'''
Exercise:
Write a program that asks the user for a password string
Print:
- "Too short" if length < 6
- "Good password" if length is 6-10
- "Very strong password" if longer than 10
'''