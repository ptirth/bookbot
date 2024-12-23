#!/usr/bin/env python3
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


def print_word_count(content: str):
    word_count = len(content.split())
    print(f"The document contains a total of {word_count} words.")


if __name__ == "__main__":
    main()
