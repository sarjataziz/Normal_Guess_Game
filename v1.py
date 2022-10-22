import random

random_number = random.randint(1, 10)        # number 1-10

guess = None
while guess != random_number:
    guess = int(input("Pick a number from 1-10 : "))

    if guess < random_number:
        print("TOO LOW!")
    elif guess > random_number:
        print("TOO HIGH!")
    else:
        print("YOU WIN!!!!!!!")
print(random_number)


