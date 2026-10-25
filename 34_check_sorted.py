"""Program 34: Check Whether a List Is Sorted."""


def is_sorted(numbers):
    """Check whether a list is sorted in ascending (non-decreasing) order."""
    for i in range(len(numbers) - 1):
        if numbers[i] > numbers[i + 1]:
            return False
    return True


if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5]
    print("List:", nums)
    print("Is sorted:", is_sorted(nums))
