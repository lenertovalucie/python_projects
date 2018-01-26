#! /usr/bin/env python3

"""
https://projecteuler.net/problem=3
"""
import argparse


def factors(n):
    """
    :param n: number for which are finding factors
    :return: list of factors for number n
    """

    return [x for x in range(2, n) if n % x == 0]


def prime_factor(n):
    """
    :param n: number for which are finding prime factors
    :return: list of prime factors for number n
    """
    list_f = factors(n)
    list_prime = []

    for num in list_f:
        for f in list_f:
            if num % f == 0:
                if num > f:
                    break
                else:
                    list_prime.append(num)

    return list_prime


def greatest_prime(n):
    return max(n)


def main():

    parser = argparse.ArgumentParser(description='Largest prime factor of the number')
    parser.add_argument('number', type=int, help='Number for which are finding prime factors')

    args = parser.parse_args()
    number = args.number

    print(greatest_prime(prime_factor(number)))


if __name__ == "__main__":
    main()
