#! /usr/bin/env python3

"""
https://projecteuler.net/problem=2.
"""

import argparse


def fibonacci_sequence(end_number):
    """
    :param end_number: number under which we want finding terms in the Fibonacci sequence
    :return: list of terms in the Fibonacci sequence
    """
    new_list = [1, 2]

    while True:

        num = new_list[-1] + new_list[-2]

        if num >= end_number:
            break
        else:
            new_list.append(num)

    return new_list


def sum_even_numbers(list_nums):
    """
    :param list_nums: list of numbers
    :return: sum of even numbers
    """

    return sum(list(filter(lambda x: x % 2 == 0, list_nums)))


def main():

    parser = argparse.ArgumentParser(description='Sum of even numbers in Fibonacci sequence')
    parser.add_argument('ending_number', type=int, help='Number under which we want finding terms in the Fibonacci sequence')

    args = parser.parse_args()
    ending_number = args.ending_number

    print(sum_even_numbers(fibonacci_sequence(ending_number)))


if __name__ == "__main__":
    main()
