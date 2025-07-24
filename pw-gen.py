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

    if not any([use_upper, use_lower, use_numbers, use_special]):
        return "Error: You must select at least one character type (e.g., --upper, --lower, --numbers, --special)."
    
    if use_lower:
        all_characters.extend(list(lowercase_chars))
        guaranteed_characters.append(random.choice(lowercase_chars))
    if use_upper:
        all_characters.extend(list(uppercase_chars))
        guaranteed_characters.append(random.choice(uppercase_chars))
    if use_numbers:
        all_characters.extend(list(digit_chars))
        guaranteed_characters.append(random.choice(digit_chars))
    if use_special:
        all_characters.extend(list(special_chars))
        guaranteed_characters.append(random.choice(special_chars))

    if len(all_characters) == 0:
        return "Error: No character types selected."

    if length < len(guaranteed_characters):
        return f"Error: Password length ({length}) is too short. It must be at least {len(guaranteed_characters)} to include all selected character types."

    # Fill the rest of the password length with random choices from all_characters
    password_list = guaranteed_characters[:] # Start with the guaranteed characters
    remaining_length = length - len(guaranteed_characters)

    for _ in range(remaining_length):
        password_list.append(random.choice(all_characters))

    # Shuffle the list to randomize the position of the guaranteed characters
    random.shuffle(password_list)

    return "".join(password_list)

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