#Age, height, medical problems, pregnant, swimsuit, fear of heights, intercom

print("Welcome to the park! We are just going to fill in a small survey to get you a guide for the rides you can get on")
print("Please answer: ")

#user conditions
age = int(input("What is your age: \n"))
height = float(input("How tall are you?: (Answer in centimeters) \n"))
medicalProblems = input("Do you have medical problems?: Yes / No \n")
pregnant = input("Are you pregnant?: Yes / No \n")
swimsuit = input("Do you have a swimsuit?: Yes / No\n")
fearHeights = input("Do you have a fear of heights?: Yes / No\n")
intercom = True


#Rides
def extremeRollerCoaster(age, medicalProblems, pregnant):
    if age > 14 and medicalProblems.lower() == "no" and pregnant.lower() == "no":
        return print("\nYou can get on the extreme roller coaster")
    else:
        return print("\nNo, get out")

def waterSLide(height, fearHeights, swimsuit):
    if height > 150 and fearHeights.lower() == "no" and swimsuit.lower() == "yes":
        return print("\nYou can get on the giant water slide")
    else:
        return print("\nYou aren't getting wet today ;)")

def slingshotCoaster(intercom, medicalProblems, age):
    if intercom and medicalProblems.lower() == "no" and age > 16:
        return print("\nWelcome to the sling shot coaster")
    elif intercom == False and medicalProblems.lower() == "no" and age > 16:
        return print("\n(Backstage) Bruh somebody turn on the intercom")
    else:
        return print("\nYou can't go into the slingshot coaster")


extremeRollerCoaster(age,medicalProblems,pregnant)
waterSLide(height,fearHeights,swimsuit)
slingshotCoaster(intercom,medicalProblems,age)
