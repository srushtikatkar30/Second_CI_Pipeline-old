"""Program 33: Find the First Non-Repeating Character."""
from collections import Counter


def first_non_repeating(s):
    """Find the first non-repeating character in a string.

    Returns the character, or None if no such character exists.
    """
    counts = Counter(s)
    for char in s:
        if counts[char] == 1:
            return char
    return None


if __name__ == "__main__":
    text = input("Enter a string: ")
    print("First non-repeating character:", first_non_repeating(text))
