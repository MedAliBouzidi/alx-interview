#!/usr/bin/env python3
""" Min Operations """


def minOperations(n: int) -> int:
    """
    A method that calculates the fewest number of operations
    needed to result in exactly n H characters in the file.
    """
    content = "H"
    copied = content * 2
    number_of_operations = 0
    while True:
        if len(content) == n:
            return number_of_operations
        elif len(content) > n:
            return 0
        if len(content) * 2 > n:
            number_of_operations += 1
            content += copied
            continue

        number_of_operations += 2
        copied = content
        content = content * 2
