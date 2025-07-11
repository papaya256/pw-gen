import argparse
import string
import random

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--length", help="desired password length (integer), type=int")

    parser.add_argument("--verbose", help="increase output verbosity",
                        action="store_true")
    
    args = parser.parse_args()
    if args.length:
        print("length: {}".format(args.length))
    if args.verbose:
        print("verbosity turned on")


if __name__ == "__main__":
    main()