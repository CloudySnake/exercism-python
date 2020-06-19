from collections import Counter
from string import ascii_lowercase


def is_isogram(string):
    return (
        True
        if not string
        else Counter([l for l in string.lower() if l in ascii_lowercase]).most_common(
            1
        )[0][1]
        == 1
    )
