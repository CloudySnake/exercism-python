from collections import Counter
from string import whitespace, punctuation
import re


def count_words(sentence):
    # Remove ' from punctuation as we want to handle that differently.
    punc = punctuation.replace("'", "")

    # Strip whitespace
    sentence = sentence.translate(str.maketrans({w: " " for w in whitespace}))
    # Strip punctuation
    sentence = sentence.translate(str.maketrans({p: " " for p in punc}))

    # Remove quote marks unless they are inbetween a letter
    sentence = re.sub(r"'|([a-z]'[a-z])", r"\g<1>", sentence)

    res = Counter([word for word in sentence.lower().split(" ") if word])
    return dict(res)
