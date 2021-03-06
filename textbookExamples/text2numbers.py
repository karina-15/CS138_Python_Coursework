#! /usr/bin/python
#
# text2numbers.py - pg.134
#   A program to convert a textual message into a sequence of
#       numbers, utilizing the underlying Unicode encoding.


def main():
    print("This program converts a textual message into a sequence"
          "\nof numbers representing the Unicode encoding of the message.\n")

    # Get the message to encode
    message = input("Please enter the message to encode: ")

    print("\nHere are the Unicode codes:")

    # Loop through the message and print out the Unicode values
    # space also has a value of 32 Unicode
    for ch in message:
        print(ord(ch), end=" ")

    print()  # blank line before prompt


main()
