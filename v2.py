import random

random_number = random.randint(1,10)    # number 1-10 

while True:
	guess = int(input("Pick a number from 1-10 : "))

	if guess < random_number:
		print("TOO LOW!")
	elif guess > random_number:
		print("TOO HIGH!")
	else:
		print("YOU WIN!!!!!!!")

		play_again = input("Do you want to play again? (y/n) : ")
		if play_again == "y":
			random_number = random.randint(1,10)
			guess = None
		else:
			print("Thanks for playing......")
			break
