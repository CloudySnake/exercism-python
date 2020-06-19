VERSES = {
    12: ("twelve Drummers Drumming, ", "twelfth"),
    11: ("eleven Pipers Piping, ", "eleventh"),
    10: ("ten Lords-a-Leaping, ", "tenth"),
    9: ("nine Ladies Dancing, ", "ninth"),
    8: ("eight Maids-a-Milking, ", "eighth"),
    7: ("seven Swans-a-Swimming, ", "seventh"),
    6: ("six Geese-a-Laying, ", "sixth"),
    5: ("five Gold Rings, ", "fifth"),
    4: ("four Calling Birds, ", "fourth"),
    3: ("three French Hens, ", "third"),
    2: ("two Turtle Doves, ", "second"),
    1: ("and a Partridge in a Pear Tree.", "first"),
}


def build_verse(verse_num):
    if verse_num == 1:
        return "On the first day of Christmas my true love gave to me: " \
               "a Partridge in a Pear Tree."

    verse = f"On the {VERSES[verse_num][1]} day of Christmas my true love gave to me: "

    days = [VERSES[num][0] for num in range(verse_num, 0, -1)]
    verse += "".join(days)

    return verse


def recite(start_verse, end_verse):
    verses = [build_verse(verse_num) for verse_num in range(start_verse, end_verse + 1)]
    return verses
