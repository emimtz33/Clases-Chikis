numOfCheckPoints = 0
altitudes = []
total = 0
hAC = 0

#Add altitude checkpoints to the Array
for checkPointt in range(3):
    altitudes.append(float(input("Enter the altitude for the checkpoint in meters:  ")))
    numOfCheckPoints += 1

#Calculate the total
for altitude in altitudes:
    total += altitude

Average = total / numOfCheckPoints

#For each checkpoint check if it surpasses 100 meters
for checkpoint in altitudes:
    if checkpoint > 100:
        hAC += 1

print("Total altitude", total)
print("Average altitude", Average)
print("Number of High Altitude Points", hAC)

#Print recommended status
if Average > 120:
    print("Flight Status: Altitude Warning: Exceeding standard maximum flight ceiling!")
elif Average >= 50 and Average <= 120:
    print("Flight Status: Optimal Altitude: Safe and stable drone flight path.")
else:
    print("Flight Status: Low Altitude Warning: Flying too close to ground obstacles!")


print("\nThank you for playing my game\n")