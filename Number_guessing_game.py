import random
print("Welcome to number guessing game")
print("I am guessing of number between 1 to 100")

secret_number = random.randint(1,100)
attempts = 0
while True:
    guess =input("Enter your guess:")

    if not guess.isdigit():
        print("Please enter a valid number!")
        continue

    guess = int(guess)
    attempts += 1
    if guess > secret_number:
        print("The number you guess is too high, try again!")
    elif guess < secret_number:
        print("The number you guess is too low, try again! ")
    else :
        print(f" 🎉Congratulations! You have guessed the correct number in {attempts} attempts")
        break

