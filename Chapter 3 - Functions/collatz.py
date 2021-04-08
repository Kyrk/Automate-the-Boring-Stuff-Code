#!/usr/bin/env python3
"""
Program that lets the user type in an integer to keep
calling a collatz sequence on that number until the
function returns the value 1.
"""

def collatz(number):
    if number % 2 == 0:
        return number / 2
    else:
        return 3 * number + 1

def main():
    print("Enter number:")

    try:
        number = int(input())
        while number > 1:
            number = collatz(number)
            print(int(number))
    except ValueError:
        # Throws error if non-integer is inputted
        print("Please enter an integer.")

main()
