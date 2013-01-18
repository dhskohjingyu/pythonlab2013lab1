# validate_mastervisa.py
# Author: Koh Jing Yu
# Date: 18/1/13
# Description: Output if a user input credit card number is a valid MasterCard 
#              or VISA card.

import re

def validate(number):
    # Run Luhn Algorithm to check if card number is valid
    total_sum = 0

    # Double the alternate digits starting from the first digit and add to sum
    for i in range(0, len(number), 2):
        current_number = int(number[i])
        current_number *= 2

        if(current_number > 9):
            current_number -= 9

        total_sum += current_number

    # Add the non-doubled digits
    for j in range(1, len(number), 2):
        current_number = int(number[j])
        total_sum += current_number

    # Get remainder when the sum is divided by 10
    # If remainder is 0, it is valid, otherwise it is invalid
    remainder = total_sum % 10

    if(remainder == 0):
        return True
    else:
        return False

def is_valid(number):
    number_of_digits = len(number)
    first_digit = int(number[0])
    first_two_digits = int(number[0] + number[1])

    valid_number = False

    # Check if the card is a VISA card
    if((number_of_digits == 16 or number_of_digits == 13) and first_digit == 4):
        valid_number = validate(number)
    # Check if the card is a MasterCard
    elif(number_of_digits == 16 and first_two_digits >= 51 and first_two_digits <= 55):
        valid_number = validate(number)
    else:
        valid_number = False

    if(valid_number):
        return "Card is valid."
    else:
        return "Card is invalid."

card_number = input("Enter your credit card number\n")
card_number = re.sub("[^0-9]", "", card_number)

print(is_valid(card_number))
