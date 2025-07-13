#!/usr/bin/env python3
import argparse
import string
import random

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


if __name__ == "__main__":
    main()