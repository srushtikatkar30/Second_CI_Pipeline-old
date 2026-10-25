"""Program 31: Check Pangram String."""
import string


def is_pangram(sentence):
    """Check whether a sentence is a pangram (contains all 26 English letters)."""
    alphabet = set(string.ascii_lowercase)
    letters_in_sentence = set(c.lower() for c in sentence if c.isalpha())
    return alphabet.issubset(letters_in_sentence)


if __name__ == "__main__":
    text = input("Enter a sentence: ")
    print("Is pangram:", is_pangram(text))
