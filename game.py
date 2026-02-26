# i want to make a game that asks user to first choose easy, medium, difficult and then easy-10 attempts , medium - 7, hard -5 
import random

num = random.randint(1, 50)
a = input("Choose difficulty level : easy, medium, hard\n")

match a:
    case "easy":
        for i in range(1, 11):
            b = int(input("guess the number:\n"))
            if b == num:
                print("win")
                break
        else:
            print("loose")
        print(f"number was {num}")

    case "medium":
        for i in range(1, 8):
            b = int(input("guess the number:\n"))
            if b == num:
                print("win")
                break
        else:
            print("loose")
        print(f"number was {num}")

    case "hard":
        for i in range(1, 6):
            b = int(input("guess the number:\n"))
            if b == num:
                print("win")
                break
        else:
            print("loose")
        print(f"number was {num}")

    case _:
        print("Invalid difficulty level")




import random
num=random.randint(1,50)
a=input("Choose difficulty level : easy, medium, hard\n")
if(a=="easy"):
    for i in range(1,11):
            b=int(input("guess the number:\n"))
            if(b==num):
                print("win")
                break
    else:
             print("loose\n")
    print(f"the number was {num}")
if(a=="medium"):
    for i in range(1,8):
            b=int(input("guess the number:\n"))
            if(b==num):
                print("win")
                break
    else:
             print("loose\n")
if(a=="hard"):
    for i in range(1,6):
            b=int(input("guess the number:\n"))
            if(b==num):
                print("win")
                break
    else:
             print("loose\n")





import random

num = random.randint(1, 50)
levels = {"easy": 10, "medium": 7, "hard": 5}

a = input("Choose difficulty level : easy, medium, hard\n")

if a in levels:
    for i in range(levels[a]):
        b = int(input("guess the number:\n"))
        if b == num:
            print("win")
            break
    else:
        print("loose")
    print(f"number was {num}")
else:
    print("Invalid level")




import random

def play(attempts, num):
    for i in range(attempts):
        b = int(input("guess the number:\n"))
        if b == num:
            print("win")
            break
    else:
        print("loose")
    print(f"number was {num}")

num = random.randint(1, 50)
a = input("Choose difficulty level : easy, medium, hard\n")

if a == "easy":
    play(10, num)
elif a == "medium":
    play(7, num)
elif a == "hard":
    play(5, num)
else:
    print("Invalid level")