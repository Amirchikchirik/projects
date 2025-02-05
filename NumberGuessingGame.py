import random

win = cont =  True

while cont:
    if win:
        num = random.randint(1,10)
        win = False
    guess = int(input("guess number: "))
    if guess == num:
        win = True
        print("you won!")
        if input("continue?(y/n): ").lower == "n":
            cont = False
    elif guess > num:
        print("lower")
    else:
        print("higher")