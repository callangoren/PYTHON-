print("welcome to callans travel assistant")
choice = input("enter the mode of travel bus/train?")
if choice == "train":
    choice2=input("normal train or bullet train")
    if choice2=="normal train":
        print("please pay 10k")
    else:
        print("please pay 50k")
else:
    choice3=input("overnightbus or bus?")
    if choice3=="overnightbus":
       print("please pay 5k")
    else:
        print("please pay 1k")



    