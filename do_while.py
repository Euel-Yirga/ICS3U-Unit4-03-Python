#!/usr/bin/env python3

# Created by:Euel Yirga
# Created on:October 2019
# This program gets the power of a user input integer

def main():
    while True:
        try:
            number = int(input("Enter a positive number: "))
            print()

            for loop_counter in range(number + 1):
                calculation = loop_counter ** 2
                print(str(loop_counter) + "^2", "=", str(calculation))

            if number < 0:
                print("Invalid Input")
                print()
                continue

        except ValueError:
            print()
            print("Invalid Input")
            print()
            continue

        else:
            break


if __name__ == "__main__":
    main()
