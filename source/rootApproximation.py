#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Add Your Name Here

import math

def fifth_root_approximation(number, tolerance=1e-6):
    """ calculate the fifth root using approximation. """    
    # Initial guess for the fourth root
    guess = number / 2.0
    # Iterate until the approximation
    # is within the specified tolerance
    while abs(guess**5 - number) > tolerance:
            # Update the guess using the approximation formula
            guess = (4 * guess + number / (guess**4)) / 5.0
            print(f"\tguess = {guess}")
    return guess

def sixth_root_approximation(number, tolerance=1e-6):
    """ calculate the sixth root using approximation. """
    # Initial guess for the sixth root
    guess = number / 2.0
    # Iterate until the approximation
    # is within the specified tolerance
    while abs(guess**6 - number) > tolerance:
        # Update the guess using the approximation formula
        guess = (5 * guess + number / (guess**5)) / 6.0
        print(f"\tguess = {guess}")
    return guess


# Example: Calculate the fifth root: (example; 550731776)
input_number = int(input(" Enter an integer to find the fifth root :"))
result = fifth_root_approximation(input_number)
# Display the result
print(f"The six root of {input_number}")
print(f" is approximately: {result}")
print(f"The floor of the value is : {math.floor(result)}")

#########
print("\n")
# Example: Calculate the six root: (example; 30840979456)
input_number = int(input(" Enter an integer to find the sixth root :"))
result = sixth_root_approximation(input_number)
# Display the result
print(f"The six root of {input_number}")
print(f" is approximately: {result}")
print(f"The floor of the value is : {math.floor(result)}")
