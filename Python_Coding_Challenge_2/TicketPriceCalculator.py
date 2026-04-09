day = input("Enter the day: ").strip().capitalize()
if day == "Saturday" or day == "Sunday":
    price = 200
else:
    price = 150
print("Ticket price for ",day,"is ",price) 