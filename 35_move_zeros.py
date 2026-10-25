"""Program 35: Move All Zeros to the End."""


def move_zeros(numbers):
    """Move all zeros to the end of the list while maintaining relative order."""
    non_zeros = [x for x in numbers if x != 0]
    zeros = [0] * (len(numbers) - len(non_zeros))
    return non_zeros + zeros


if __name__ == "__main__":
    nums = [0, 1, 0, 3, 12]
    print("Original:", nums)
    print("Zeros moved:", move_zeros(nums))
