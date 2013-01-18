# master_or_visa.py
# Author: Koh Jing Yu
# Date: 18/1/13
# Description: Output if a user input credit card number belongs to MasterCard 
#              or VISA.

import re

def card_name(number):
    number_of_digits = len(number)
    first_digit = int(number[0])
    first_two_digits = int(number[0] + number[1])
    
# Check if the card is a VISA card (13 or 16 digits, first digit is a 4)
    if((number_of_digits == 16 or number_of_digits == 13) and first_digit == 4):
        return "This is a VISA card"
# Check if the card is a MasterCard (16 digits, first two digits are from 51-55)
    elif(number_of_digits == 16 and first_two_digits >= 51 and first_two_digits <= 55):
        return "This is a MasterCard"
    
    return "Only VISA and MasterCards are accepted"

card_number = input("Enter your credit card number\n")
# remove all non integers from the string
card_number = re.sub("[^0-9]", "", card_number)

print(card_name(card_number))
