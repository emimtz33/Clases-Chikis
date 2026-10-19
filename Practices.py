"""""
# Rock Paper Scissors game

user = input("What do you choose: Rock, Paper or Scissors").lower()

if user == "rock":
    print("I chose PAPER. I win")
elif user == "paper":
    print("I chose ROCK. I win")
elif user == "scissors":
    print("I chose PAPER. I guess you win")
else:
    print("What the hell did you choose")

#Grade Average Calculator

grades = []
average = 0

while True:
    if input("Do you wish to add a grade?\n").lower() == "yes":
        grades.append(float(input("Add a grade\n")))
    else:
        break

for grade in grades:
    average += grade

total = average / grades.__len__()

print("Here is your average:  " + str(total))

"""""



x = 6

while x == 6:
    print("X es igual a 6")
    if x == 6:
        break