import random


def number_guessing_game():
    number_to_guess = random.randint(1, 10)
    attempts = 5

    for attempt in range(1, attempts + 1):
        user_input = input(f"Attempt {attempt}: Guess the number between 1 and 10: ")

        # Validate input
        if not user_input.isdigit():
            print("Invalid input. Please enter a number.")
            continue

        guess = int(user_input)

        if guess == number_to_guess:
            print(f"Congratulations! You guessed the number {number_to_guess} correctly!")
            break
        elif guess < number_to_guess:
            print("Your guess is too low.")
        else:
            print("Your guess is too high.")
    else:
        print(f"Sorry, you've used all attempts. The number was {number_to_guess}.")


number_guessing_game()