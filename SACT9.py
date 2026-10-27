days = ["monday", "wednesday", "friday"]

noiseLevel = 0
studentEnergyLevel = 0
actDifficulty = 0
timeWOBreak = 0

def vibeCheck (noiseLevel, sel, actDif, tWOB):
    if noiseLevel >= 8 and sel >= 8 and actDif >= 8 and tWOB >= 120:
        recommendation(1)
    elif noiseLevel >= 8:
        recommendation(2)
    elif sel >= 8:
        recommendation(3)
    elif actDif >= 8:
        recommendation(4)
    elif tWOB >= 8:
        recommendation(5)
    else:
        print("You are all fine. Just tough it out")

def recommendation (vibe):
    if vibe == 1:
        print("Good Luck")
    elif vibe == 2:
        print("Rip your ears off or put on earphones")
    elif vibe == 3:
        print("Drink water and fermented wheat juices")
    elif vibe == 4:
        print("Get gud")
    elif vibe == 5:
        print("Take a break, have a kitkat")
        


print("Answer these questions on a scale from 1-10 except for the last one")

for day in days:
    noiseLevel = float(input(f"\nWhat was the noise level for: {day} "))
    studentEnergyLevel = float(input(f"Did you feel tired for: {day} "))
    actDifficulty = float(input(f"What was the difficulty of your activity for: {day} "))
    timeWOBreak = float(input(f"How much did you spend working without a break for: {day} (INPUT IT IN MINUTES): "))

    print(f"\nHere is some recommendations for this day!: {day}\n")

    vibeCheck(noiseLevel, studentEnergyLevel, actDifficulty, timeWOBreak)

print("Enjoy Your Weekend!")