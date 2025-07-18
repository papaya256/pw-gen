#!/usr/bin/env python3
import argparse
import string
import random

def generate_password(length, use_upper, use_lower, use_numbers, use_special):
    """
    Generates a random password based on specified criteria.

    Args:
        length (int): The desired length of the password.
        use_upper (bool): True to include uppercase letters.
        use_lower (bool): True to include lowercase letters.
        use_numbers (bool): True to include numbers.
        use_special (bool): True to include special characters.

    Returns:
        str: The generated password, or an error message if criteria are insufficient.
    """

    all_characters = []
    guaranteed_characters = []

    # Define character sets
    lowercase_chars = string.ascii_lowercase
    uppercase_chars = string.ascii_uppercase
    digit_chars = string.digits
    special_chars = string.punctuation

    # TODO: Display an error message if no character types are selected
    # HINT: Use an if statement to check if all options are False

def main():
    parser = argparse.ArgumentParser(
        description="Generate a random password with specified length and character types.",
        formatter_class=argparse.RawTextHelpFormatter
    )

    parser.add_argument(
        "-l", "--length",
        type=int,
        default=12,
        help="Desired password length (integer). Default is 12."
    )

    parser.add_argument(
        "-u", "--upper",
        action="store_true",
        help="Include uppercase letters (A-Z)."
    )
    parser.add_argument(
        "-o", "--lower",
        action="store_true",
        help="Include lowercase letters (a-z)."
    )

    parser.add_argument(
        "-n", "--numbers",
        action="store_true",
        help="Include numbers (0-9)."
    )

    parser.add_argument(
        "-s", "--special",
        action="store_true",
        help="Include special characters (e.g., !@#$*()-+=[]{}|;:,.<>?/)."
    )

    args = parser.parse_args()

    password = generate_password(
        args.length,
        args.upper,
        args.lower,
        args.numbers,
        args.special
    )

    print(password)


if __name__ == "__main__":
    main()