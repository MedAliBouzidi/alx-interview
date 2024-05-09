#!/usr/bin/python3
""" UTF-8 Validation """


def validUTF8(data):
    """
    Data: a list of integers
    Return: True if data is a valid UTF-8
        encoding, else return False
    """
    bytes_counter = 0

    for i in data:
        if bytes_counter == 0:
            if i >> 5 == 0b110 or i >> 5 == 0b1110:
                bytes_counter = 1
            elif i >> 4 == 0b1110:
                bytes_counter = 2
            elif i >> 3 == 0b11110:
                bytes_counter = 3
            elif i >> 7 == 0b1:
                return False
        else:
            if i >> 6 != 0b10:
                return False
            bytes_counter -= 1

    return bytes_counter == 0
