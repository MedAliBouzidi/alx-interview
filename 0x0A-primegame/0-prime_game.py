#!/usr/bin/python3
""" Prime Game """


def primes(n):
    """
    Prime numbers

    Args:
        n: integer

    Returns:
        list of prime
    """
    prime = []
    for i in range(2, n + 1):
        if i == 2:
            prime.append(i)
        else:
            for j in range(2, i):
                if j == i - 1:
                    prime.append(i)
                elif i % j == 0:
                    break
    return prime


def isWinner(x, nums):
    """
    Prime Game

    Args:
        x: integer
        nums: list of integers

    Returns:
        name of the player that won the most rounds
    """
    if x is None or nums is None or x == 0 or len(nums) == 0:
        return None

    maria = ben = 0
    for i in range(x):
        prime = primes(nums[i])
        if len(prime) % 2 == 0:
            ben += 1
        else:
            maria += 1

    if maria == ben:
        return None
    return "Maria" if maria > ben else "Ben"
