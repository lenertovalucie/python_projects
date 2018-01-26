#! /usr/bin/env python3

"""
https://projecteuler.net/problem=5
"""

import argparse


def find_multiple(step, top):
    """
    :param step: largest factor
    :param top: number which stop finding
    :return: smallest positive number that is evenly divisible by all of the numbers from 1 to 'largest actor'
    """

    for x in range(step**2, top, step):
        for y in range(step//2, step + 1):
            if x % y != 0:
                break
            if y == step:
                return x


def main():

    parser = argparse.ArgumentParser(description='Find smallest positive number that is evenly divisible by all of the numbers from 1 to n')
    parser.add_argument('factor', type=int, help='Largest factor (n)')
    parser.add_argument('end_number', type=int, help='Number which stop finding')

    args = parser.parse_args()
    end_number, factor = args.end_number, args.factor

    print(find_multiple(factor, end_number))


if __name__ == "__main__":
    main()
