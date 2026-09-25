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


#Variations of rules expressed in different ways

#Extreme Roller Coaster variations
def extremeRollerCoaster1(age, medicalProblems, pregnant):
    isPregnant = False
    if pregnant.lower() == "yes":
        isPregnant = True

    if age - 14 > 0 and medicalProblems.lower() == "no" and not isPregnant:
        return print("\nYou can get on the extreme roller coaster")
    else:
        return print("\nNo, get out")
    
def extremeRollerCoaster2(age, medicalProblems, pregnant):
    if age > 14 and medicalProblems.lower() == "no" or pregnant.lower() == "no":
        return print("You can't get on until we confirm if you are pregnant or not")
    else:
        return print("You can't get on")


#Water Slide variations
def waterSlide1(height, fearHeights, swimsuit):
    if height < 150 and fearHeights.lower() == "no" and swimsuit.lower() == "yes":
        return print("You must be atleast this height to get on")

def waterSlide2(height, fearHeights, swimsuit):
    heights = False
    if fearHeights == "yes":
        heights = True

    if height > 150 and not heights and swimsuit.lower() == "yes":
        return print("Get on the water slide")
    else:
        return print("Don't even think about it")


#Slinghshot coaster variations
def slingshotCoaster1(intercom, medicalProblems, age):
    if intercom == False and medicalProblems.lower() == "yes" and age > 16:
        return print("Bruh the intercom again. But if you can hear me then you can't get on either way")
    else:
        return print("Wait just a sec")

def slingshotCoaster2(intercom, medicalProblems, age):
    if intercom == True and medicalProblems.lower() == "no" or age > 16:
        return print("How old were you again?")
    else:
        return print("Nah bro you can't get on")