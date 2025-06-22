import random
def guess_num_game():

    random_num = random.randint(1, 100)
    attempt = 0
    max_attempt = 10

    print("Welcome to the Number Guessing Game!")
    print("\nGuess the number between 1 and 100.")
    print(f"You have {max_attempt} attempts.\n")

    while attempt < max_attempt:

        try:
            guess = int(input("Guess a number : "))
            attempt += 1

            if guess == random_num:
                print(f"\nCorrect! The number was {random_num}.")
                print(f"You guessed it in {attempt} attempts.")
                return

            elif guess > random_num:
                print("Your guess is too high. Try again.\n")

            else:
                print("Your guess is too low. Try again.\n")

        except ValueError:
            print("Invalid input! Please enter a valid number.\n")

    print(f"\nGame Over! You've used all {max_attempt} attempts.")
    print(f"The correct number was: {random_num}")


guess_num_game()
