import random

def computer_guess(min_value, max_value, secret_number):
    """
    The computer makes a guess for the secret number.
    :param min_value: The minimum value of the range.
    :param max_value: The maximum value of the range.
    :param secret_number: The secret number that the user has in mind.
    :return: The computer's guess.
    """
    if max_value - min_value == 1:
        return min_value

    max_guess_number = min_value + (max_value - min_value) // 2
    if computer_guess(min_value, max_guess_number, secret_number) == secret_number:
        return computer_guess(max_guess_number, max_value, secret_number)
    else:
        return computer_guess(min_value, max_guess_number, secret_number)

def main():
    """
    The main function that runs the game.
    """
    print('Please think of a number between 0 and 100!')
    secret_number = int(input('Now tell me your secret number: '))
    guess = computer_guess(0, 100, secret_number)
    print(f'The computer guessed {guess} and it was correct!')

if __name__ == '__main__':
    main()