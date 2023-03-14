import string
import random


def create_substitution_table():
    # Create an empty dictionary to store letters as keys and their substitution as values.
    substitution_table = {}

    # Create a string of the English alphabet letters (including capitals).
    letters = string.ascii_lowercase + string.ascii_uppercase

    # Create and randomly shuffle a list of the English alphabet letters (including capitals) to get substitutions.
    substitutions = list(string.ascii_lowercase + string.ascii_uppercase)
    random.shuffle(substitutions)

    # Insert the English alphabet letters (including capitals) to the substitution table with their shuffled values.
    for letter, substitution in zip(letters, substitutions):
        substitution_table[letter] = substitution

    # Finally, whitespace should go to itself.
    substitution_table[' '] = ' '

    return substitution_table


def encrypt(plaintext, substitution_table):
    # Create an empty string that will store the encrypted plaintext.
    cipher = ""

    # Substitute according to the substitution table.
    for symbol in plaintext:
        if symbol in substitution_table.keys():
            cipher += substitution_table[symbol]

    return cipher


