"""Program 36: Find the Most Frequent Element in a List."""
from collections import Counter


def most_frequent(items):
    """Find the most frequent element in a list.

    Returns the element with the highest frequency, or None if empty.
    """
    if not items:
        return None
    counts = Counter(items)
    return counts.most_common(1)[0][0]


if __name__ == "__main__":
    nums = [1, 3, 2, 1, 4, 1]
    print("List:", nums)
    print("Most frequent:", most_frequent(nums))
