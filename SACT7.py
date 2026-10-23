import time
from winsound import Beep

#Waiting for input to begin program
while True:
    print("Ready to start")
    if input("Type START to begin studying: ").upper() == "START":
        break
    print("** Remember to type 'start' correctly **")

#Countdown to begin
while True:
    for count in range(5):
        print("Beginning in: ", (count +1))
        time.sleep(1)
    break

print("\nStarting\n")

#Studying and resting block
for block in range(4):
    print("Beginning block ", (block+1) ,"...")
    print("Studying...")
    for study in range (10):
        print(study +1)
        time.sleep(1)

    print("Completed block: ", (block+1), ". Take a short break")
    
    for rest in range(3):
        print("Resting, ", (rest+1))
        time.sleep(1)


print("Routine finalized")

#Play finish song
C = 262
D = 294
E = 330
F = 349
G = 392
A = 440

melody = [ (C, 1000), (C, 1000),(G, 1000), (G, 1000),(A, 1000), (A, 1000),(G, 1400),
    (F, 1000), (F, 1000),(E, 1000), (E, 1000),(D, 1000), (D, 1000),(C, 1400)]

for frequency, duration in melody:
    Beep(frequency, duration)
    time.sleep(0.3)