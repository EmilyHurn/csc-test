import random

def binary_guessing_game():
    """Plays a binary guessing game with the user."""

    low = 1
    high = 100
    attempts = 0

    number = random.randint(low, high)
    guess = None

    print("I am thinking of a number between 1 and 100.")
    print("You only have 10 chances to get it right!")

    while guess != number:
        guess = input("What is your guess? ")

        try :
            guess = int(guess)
        except ValueError:
            print("please guess a number.")
            continue

        if guess < low or guess > high:
            print("please guess a number between 1 and 100.")
            continue

        if guess < number:
            print("guess higher! ")
            attempts += 1

        if guess > number:
            print("guess lower! ")
            attempts += 1

        if guess == number:
            print("you got it! ")
            break

        if attempts == 10:
            print("You lose! Maybe next time")

if __name__ == "__main__":
    binary_guessing_game()