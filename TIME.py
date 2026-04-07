hour = int(input("Enter the current hour: "))
hours_to_add = int(input("Enter the number of hours to add: "))
hour = (hour + hours_to_add)% 12



print(hour)