"""Program 32: Count Words in a Sentence."""


def count_words(sentence):
    """Count the number of words in a sentence."""
    return len(sentence.split())


if __name__ == "__main__":
    text = input("Enter a sentence: ")
    print("Word count:", count_words(text))
