user=input("choose between snake(s) gun(g) and water(w): ")
while user!="s" and user!="g" and user!="w":
    print("Invalid choice,choose again")
    user=input("choose between snake(s) gun(g) and water(w): ")

#Can use this idea too
# while user not in ["snake", "gun", "water"]:
#     print("Invalid choice, choose again.")
#     user = input("Choose between snake, gun, and water: ")

if user=='s':
    user="Snake"
elif user=='g':
    user="Gun"
else:
    user="Water"

print("Your choice: ",user)

import random

myList=["Snake","Gun","Water"]
randNum=random.randint(0,2);
computer=myList[randNum]

print("My choice: ",computer)

match user:
    case "Snake":
        if computer=="Snake":
            print("It's a tie")
        elif computer=="Water":
            print("You win!")
        else:
            print("You lose")
    case "Gun":
        if computer=="Gun":
            print("It's a tie")
        elif computer=="Snake":
            print("You win!")
        else:
            print("You lose")
    case "water":
        if computer=="Water":
            print("It's a tie")
        elif computer=="Gun":
            print("You win!")
        else:
            print("You lose")
