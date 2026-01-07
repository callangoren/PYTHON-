is_raining = (input("is it raining?"))
is_cold = (input("is it cold?"))
if is_raining == "no" and is_cold == "no":
    print("Enjoy the weather!")

elif is_raining == "yes" and is_cold =="no":
    print("Bring an umbrella.")

elif is_cold == "yes" and is_raining == "no":
    print("Bring a jacket.")
else:
    print("Bring a jacket AND an umbrella!!!")
