import random

def number_guessing_game():
    secret = random.randint(1, 100)
    attempts = 7
    print("Guess a number between 1 and 100")

    while attempts > 0:
        try:
            guess = int(input("Enter guess: "))
            if guess == secret:
                print("🎉 Correct! You win.")
                break
            elif ((secret+5) > guess and (secret < guess)) or ((secret-5) < guess and (secret > guess)):
                print("Too close.")
            elif guess < secret:
                print("Too low.")
            else:
                print("Too high.")
            attempts -= 1
            print(f"Attempts left: {attempts}")
        except ValueError:
            print("Enter a valid number.")
    else:
        print(f"Game Over! The number was {secret}.")

number_guessing_game()
