import random

def play_game():
    number = random.randint(1, 100)
    attempts = 0

    print("🎲 Guess the Number")
    print("I have chosen a number from 1 to 100.")

    while True:
        guess = input("Enter your guess: ")

        if not guess.isdigit():
            print("❌ Please enter a valid number.")
            continue

        guess = int(guess)
        attempts += 1

        if guess < number:
            print("🔽 Too low!")
        elif guess > number:
            print("🔼 Too high!")
        else:
            print(f"🎉 Correct! The number was {number}.")
            print(f"🔢 Attempts: {attempts}")
            break


if __name__ == "__main__":
    play_game()
