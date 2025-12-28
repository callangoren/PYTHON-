rule_input = input("did you follow all the rules?")
how_many_input = input("how many rules did you follow exactly?")
how_many = int(how_many_input)

if rule_input == "yes" and how_many_input == "10":
    print("Ok! you may pass.")
else:
    print("go back and follow the rules!!!")

