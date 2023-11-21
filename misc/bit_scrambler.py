#!/usr/bin/env python3

import sys, random

def bitflip(byte, bit):
    bits = [
        0b00000001,
        0b00000010,
        0b00000100,
        0b00001000,
        0b00010000,
        0b00100000,
        0b01000000,
        0b10000000
    ]
    negbits = [
        0b11111110,
        0b11111101,
        0b11111011,
        0b11110111,
        0b11101111,
        0b11011111,
        0b10111111,
        0b01111111
    ]
    if byte | bits[bit] == byte:
        return byte & bits[bit]
    return byte | bits[bit]

def n_bits_off(byte, n):
    if n>8:
        raise Error

    bits = []

    while len(bits) < n:
        bit = random.randint(0,7)
        if bit in bits:
            continue
        bits.append(bit)

    for bit in bits:
        byte = bitflip(byte, bit)

    return byte


if __name__ == "__main__":
    if not len(sys.argv) == 2:
        print("This program takes exactly one argument: the string to scramble.")

    output = []
    for character in list(sys.argv[1]):
        a = random.randint(0, 36)
        if ord(character)<33 or ord(character) > 126:
            output.append(character)
        elif a%18==0:
            byte = n_bits_off(ord(character), 3)
            if byte > 32 and byte < 127:
                output.append(chr(byte))
            else:
                output.append(character)
        elif a%12==0:
            byte = n_bits_off(ord(character), 2)
            if byte > 32 and byte < 127:
                output.append(chr(byte))
            else:
                output.append(character)
        elif a%9==0:
            byte = n_bits_off(ord(character), 1)
            if byte > 32 and byte < 127:
                output.append(chr(byte))
            else:
                output.append(character)
        else:
            output.append(character)

    print("".join(output))
