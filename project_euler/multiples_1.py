#! /usr/bin/env python3

"""
https://projecteuler.net/problem=1
"""

import argparse


def sum_multiples(first_m, second_m, range_num):
    """
    :param first_m: first multiple of number
    :param second_m: second multiple of number
    :param range_num: number under which we want finding multiples
    :return: sum of all multiples below given number
    """

    new_list = list(range(range_num))
    multiples = list(filter(lambda x: x % first_m == 0 or x % second_m == 0, new_list))

    return sum(multiples)


def main():

    parser = argparse.ArgumentParser(description='Sum of all multiples below given number')
    parser.add_argument('first', type=int, help='First multiple of number')
    parser.add_argument('second', type=int, help='Second multiple of number')
    parser.add_argument('range_n', type=int, help='Number under which we want finding multiples')

    args = parser.parse_args()
    first, second, range_n = args.first, args.second, args.range_n

    print(sum_multiples(first, second, range_n))


if __name__ == "__main__":
    main()
