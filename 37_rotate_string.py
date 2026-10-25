"""Program 37: Rotate a String by K Positions."""


def rotate_string(s, k):
    """Rotate a string to the right by k positions."""
    if not s:
        return ""
    n = len(s)
    k = k % n
    if k == 0:
        return s
    return s[-k:] + s[:-k]


if __name__ == "__main__":
    text = "abcdef"
    print("Original:", text)
    print("Rotated by 2:", rotate_string(text, 2))
