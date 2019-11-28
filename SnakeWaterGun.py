import random

i = 0
user = 0
computer = 0
draw = 0

while i <= 10:
    lst = ["snake","water","gun"]
    random_input = random.choice(lst)
    x = input("Enter your choice:")
    if x == "snake" and random_input == "snake":
        print("its a draw")
        print("computer has choosen:", random_input)
        draw = draw + 1
    elif x == "snake" and random_input == "water":
        print("you have won")
        print("computer has choosen:", random_input)
        user = user + 1
    elif x == "snake" and random_input == "gun":
        print("computer has won")
        print("computer has choosen:", random_input)
        computer = computer + 1
    elif x == "water" and random_input == "snake":
        print("computer has won")
        print("computer has choosen:", random_input)
        computer = computer + 1
    elif x == "water" and random_input == "water":
        print("its a draw")
        print("computer has choosen:", random_input)
        draw = draw + 1
    elif x == "water" and random_input == "gun":
        print("computer has won")
        print("computer has choosen:", random_input)
        computer = computer + 1
    elif x == "gun" and random_input == "snake":
        print("you have won")
        print("computer has choosen:", random_input)
        user = user + 1
    elif x == "gun" and random_input == "water":
        print("you have won")
        print("computer has choosen:", random_input)
        user = user + 1
    elif x == "gun" and random_input == "gun":
        print("its a draw")
        print("computer has choosen:", random_input)
        draw = draw + 1
    else:
        print("enter a valid input")

print("user has won" + user + "times")
print("computer has won" + computer + "times")
print("draw has happened" + draw + "times")
