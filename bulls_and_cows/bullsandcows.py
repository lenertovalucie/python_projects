#! /usr/bin/env python3

"""
Bulls and cows game: https://en.wikipedia.org/wiki/Bulls_and_Cows
"""

import random


def generate_number():
    """
    :return: string which contain 4 different digit
    """

    digits = 0
    random_num = 0

    while digits != 4:
        random_num = str(random.randint(1000, 9999))
        digits = len(set([x for x in random_num]))

    return random_num


def count_bulls_cows(user_string, comp_string):
    """
    Function compare two strings and count bulls and cows
    :param user_string: string which has the same length as comp_string
    :param comp_string: string which has the same length as user_string
    :return: tuple with number of cows and bulls
    """

    bulls = 0
    cows = 0

    for index, num in enumerate(user_string):
        if comp_string[index] == user_string[index]:
            bulls += 1
        if num in comp_string and comp_string[index] != user_string[index]:
            cows += 1

    return bulls, cows


def main():

    print("Welcome, welcome, welcome...You are playing game Bulls and Cows!")
    print("The goal of the game is to uncover the 4-digit secret number with a minimal number of questions.")
    print("""Rules:
    - All digits in the secret number are different.
    - The secret number can not start with zero.
    - If your try has matching digits on the exact places, they are Bulls.
    - If you have digits from the secret number, but not on the right places, they are Cows.
    """)

    while True:
        secret_num = generate_number()
        guess_num = ""
        guesses = 0

        print("I am thinking 4-digit number... If you get lost during the game, type 'give up'.")

        while guess_num != secret_num:
            guess_num = input("What is the secret number? ")

            if guess_num.lower() == "give up":
                print("Secret number is: {}".format(secret_num))
                break

            try:
                int(guess_num)
            except ValueError:
                print("Sorry, you must write number. Try again or type 'give up'.")
                continue

            if not len(guess_num) == 4:
                print("Sorry, your number must have 4 digits. Try again or type 'give up'.")
                continue
            elif not (len(set([x for x in guess_num])) == 4):
                print("Sorry, your number must contain different digits. Try again or type 'give up'.")
                continue
            elif not (guess_num[0] != "0"):
                print("Sorry, your number can not start with zero. Try again or type 'give up'.")
                continue
            else:
                score = count_bulls_cows(guess_num, secret_num)
                print("\n{}: {} bulls and {} cows\n".format(guess_num, score[0], score[1]))
                guesses += 1

        else:
            words = {"amazing": guesses <= 7, "average": 8 <= guesses <= 10, "not so good": guesses >= 11}
            print("Yes, this is the secret number: {}!".format(secret_num))
            print("You've done it in {} guesses! That's {}!".format(guesses, [key for key,value in words.items() if value][0]))

        game_again = input("If you don't want play again, type 'exit' or type anything else for another game! ")

        if game_again.lower() == "exit":
            print("See you next time!")
            return False


if __name__ == "__main__":
    main()
