age = int(input("Please enter your age: "))
has_ticket_input = input("Do you have a ticket to the amusement park? (yes/no):")
if age < 12 or age > 65:
    print("You get a discount!")
elif has_ticket_input == 'no':
    print("buy a ticket")


else:
    print("you can enter the park")

'''Homework Question:
Write a program that asks the user for their age and whether they have a ticket to the amusement park ("yes" or "no").

If the user is under 12 or over 65, print "You get a discount!" regardless of whether they have a ticket or not.
If they are 12 or older but under 65 and do not have a ticket, print "You need to buy a ticket!".
Otherwise, print "You can enter the park without buying a ticket!".
Use if, elif, else, and, and or to handle all the different cases.'''