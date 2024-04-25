#!/usr/bin/python3
""" Min Operations """


def minOperations(n):
    """
    A method that calculates the fewest number of operations
    needed to result in exactly n H characters in the file.
    """
    pasted_content = 1  # chars in the file
    registry = 0  # H's copied
    counter = 0  # operations counter

    while pasted_content < n:
        # if did not copy anything yet
        if registry == 0:
            registry = pasted_content
            counter += 1

        # if haven't pasted anything yet
        if pasted_content == 1:
            pasted_content += registry
            counter += 1
            continue

        remaining = n - pasted_content  # remaining chars to Paste
        if remaining < registry:
            return 0

        # if can't be devided
        if remaining % pasted_content != 0:
            pasted_content += registry
            counter += 1
        else:
            registry = pasted_content
            pasted_content += registry
            counter += 2

    # if got the desired result
    if pasted_content == n:
        return counter
    else:
        return 0
