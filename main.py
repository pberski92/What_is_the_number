import random


random_num = random.randrange(1,100)
guess_num = 0
chances = 5


while chances != -1:

    print(f"You have {chances} chances.")
    guess_num = int(input("What is your number? "))
    if guess_num == random_num:
        print("You are a Winner!!")
        chances = -1
    else:
        if guess_num > random_num:
            print("Your number is smaller")
            chances -= 1
        else:
            print("Your number is biger")
            chances -= 1
    if chances == 0:
        print("You loose")
        chances -=1