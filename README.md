# pw-gen
password generator

## Command-Line Arguments

- `--length` (or -l): Specifies the desired password length (integer).

- `--upper` (or -u): Includes uppercase letters.

- `--lower` (or -o): Includes lowercase letters.

- `--numbers` (or -n): Includes numbers.

- `--special` (or -s): Includes special characters.

## Usage

pw-gen -l 8 -u -o -n -s

Will output an 8-character, random password with at least 1 upper, lower, number, and special character.