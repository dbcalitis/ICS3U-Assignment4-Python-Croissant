#!/usr/bin/env python3

# Created by: Daria Bernice Calitis
# Created on: Oct 2021
# This program is the croissant store

import constants


def main():
    # This program calculates the total cost of the croissants
    total = 0
    print("Croissants are ${0} each.".format(constants.CROISSANT_PRICE))

    # input
    number_of_croissants = input("How many croissants would you like?: ")

    # process & ouput
    try:
        number_of_croissants = int(number_of_croissants)
        # if the user buys 6 or more croissants then they will get the tax off
        if number_of_croissants >= 6:
            total = number_of_croissants * constants.CROISSANT_PRICE
            print("The total cost will be ${:,.2f} (no HST)".format(total))
        else:
            total = (number_of_croissants * constants.CROISSANT_PRICE) * constants.HST
            print("The total cost will be ${:,.2f} (with HST)".format(total))
    except (Exception):
        print("Invalid Input.")

    print("\nDone.")


if __name__ == "__main__":
    main()
