#!/usr/bin/python3

import argparse

from words import WORDS

parser = argparse.ArgumentParser(
    description="""Wordle helper. Enter chars to include and exclude. 
    example" `python ./wordle.py bort chile`"""
)
parser.add_argument(
    "include",
    type=str,
    help="chars to include",
)
parser.add_argument(
    "exclude",
    type=str,
    help="chars to exclude",
)


def exclude_chars(letters, words):
    return filter(lambda x: all(letter not in x for letter in letters), words)


def include_chars(letters, words):
    return filter(lambda x: all(letter in x for letter in letters), words)


if __name__ == "__main__":

    args = parser.parse_args()

    print(
        list(
            include_chars(
                args.include,
                exclude_chars(
                    args.exclude,
                    WORDS,
                ),
            ),
        ),
    )
