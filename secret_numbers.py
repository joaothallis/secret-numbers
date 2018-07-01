from random import randint


# Functions
def __welcome_message():
    """Welcome message displayed when you start the game"""
    print("Welcome to Secret Numbers.")


def __generate_secret_number():
    """Generate a random number between 1 and 10 for the player to guess"""
    return randint(1, 10)


def __hit(secret_number, choice):
    """Check if the choice is equal to secret number"""
    return secret_number == choice
