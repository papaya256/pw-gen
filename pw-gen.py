import argparse
import string
import random

def main():
    # 1st figure out how to use argparse to parse command line arguments
    randomLetter = random.choice(string.ascii_letters)
    print(randomLetter)

if __name__ == "__main__":
    main()