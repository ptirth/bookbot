#!/usr/bin/env python3
from collections import defaultdict
import sys


def main():
    cmd_args = sys.argv[1:]
    if len(cmd_args) == 1:
        print_statistics(cmd_args[0])
    else:
        print("Usage: bookbot.py [document]")


def print_statistics(filename: str):
    content = ""
    try:
        with open(filename) as f:
            content = f.read()
    except FileNotFoundError:
        print(f"File '{filename}' not found!")

    print_word_count(content)
    print_alphabets_count(content)


def print_word_count(content: str):
    word_count = len(content.split())
    print(f"The document contains a total of {word_count} words.")


def print_alphabets_count(content: str):
    alphabets_count = defaultdict(lambda: 0)

    for char in content.lower():
        if char < "a" or char > "z":
            continue

        alphabets_count[char] += 1

    for char, count in sorted(alphabets_count.items()):
        print(f"Alphabet {char} was found {count} times.")


if __name__ == "__main__":
    main()
