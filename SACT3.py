days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
monday = 0
tuesday = 0
wednesday = 0
thursday = 0
friday = 0
saturday = 0
sunday = 0

sumDay = 0

valid = True

print("Hello, we are going to get the avarage of your total screen time and hours for each category!\n (Please answer in minutes)")


for day in days:
    print(day)
    if day == "monday":
        monday = float(input("What is your total time for this day?"))
        if (monday > 1440):
            print("This is not a valid time for this day")
            valid = False
            break
    elif day == "tuesday":
        tuesday = float(input("What is your total time for this day?"))
        if (tuesday > 1440):
            print("This is not a valid time for this day")
            valid = False
            break
    elif day == "wednesday":
        wednesday = float(input("What is your total time for this day?"))
        if (wednesday > 1440):
            print("This is not a valid time for this day")
            valid = False
            break
    elif day == "thursday":
        thursday = float(input("What is your total time for this day?"))
        if (thursday > 1440):
            print("This is not a valid time for this day")
            valid = False
            break
    elif day == "friday":
        friday = float(input("What is your total time for this day?"))
        if (friday > 1440):
            print("This is not a valid time for this day")
            valid = False
            break
    elif day == "saturday":
        saturday = float(input("What is your total time for this day?"))
        if (saturday > 1440):
            print("This is not a valid time for this day")
            valid = False
            break
    elif day == "sunday":
        sunday = float(input("What is your total time for this day?"))
        if (sunday > 1440):
            print("This is not a valid time for this day")
            valid = False
            break

sumDay = int(monday) + int(tuesday) + int(wednesday) + int(thursday) + int(friday) + int(saturday) + int(sunday)

if(valid == True):
    totalSum = sumDay / 7
    print("Your average for each day in minutes is: ",  totalSum)
elif(valid == False):
    print("Try using a valid time next")
    