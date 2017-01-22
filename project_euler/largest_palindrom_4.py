#! /usr/bin/env python3

"""
https://projecteuler.net/problem=4
"""

import argparse


def is_palindrome(n):
    """
    :param n: number
    :return: True if number is palindrome
    """
    string_n = str(n)

    return string_n == string_n[::-1]


def find_pal(bot, top):
    """
    :param top: start number from which are finding palindromes
    :param bot: number under which are finding palindromes
    :return: list of palindromes made from the product of two numbers
    """

    palindromes = []

    for x in range(bot, top):
        for y in range(bot, top):
            if is_palindrome(x * y):
                palindromes.append(x * y)

    return palindromes


def biggest_palindrome(pals):

    return max(pals)


def main():

    parser = argparse.ArgumentParser(description='Find the largest palindrome made from the product of two numbers.')
    parser.add_argument('start_number', type=int, help='Start number from which are finding palindromes')
    parser.add_argument('end_number', type=int, help='Number under which are finding palindromes')

    args = parser.parse_args()
    start_number, end_number = args.start_number, args.end_number

    print(biggest_palindrome(find_pal(start_number, end_number)))


if __name__ == "__main__":
    main()
