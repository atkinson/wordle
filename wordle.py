import argparse

from words import WORDS

WORD_LENGTH = 5
BAD_CHARS = ["'", "%"]

parser = argparse.ArgumentParser(
    description="""Wordle helper. Enter chars to include and exclude. 
    example" `python ./wordle.py ins xsv`"""
)
parser.add_argument(
    "include",
    nargs=1,
    type=str,
    help="chars to include",
)
parser.add_argument(
    "exclude",
    nargs=1,
    type=str,
    help="chars to exclude",
)


def file_as_list(filename):
    return open(filename, "r").read().splitlines()


def filter_len(size, words):
    return filter(lambda x: len(x) == size, words)


def exclude_bad_chars(letters, words):
    return filter(lambda x: all(letter not in x for letter in letters), words)


def filter_good_chars(letters, words):
    return filter(lambda x: all(letter in x for letter in letters), words)


if __name__ == "__main__":

    args = parser.parse_args()

    print(
        list(
            filter_good_chars(
                args.include,
                exclude_bad_chars(
                    args.exclude + BAD_CHARS,
                    filter_len(
                        WORD_LENGTH,
                        WORDS,
                    ),
                ),
            ),
        ),
    )
