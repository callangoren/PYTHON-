correct_pin=2015
balance=5000
PIN = int(input("enter your 4-digit PIN"))
if PIN == correct_pin:
    print("PIN accepted!")
    amount=int(input("enter withdrawel amount"))
    if amount <=balance:
        print("withdrawal successful!!!")
    else:
        print("insufficient balance")
else:
    print("wrong PIN try again")
