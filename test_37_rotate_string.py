from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))

import importlib

module = importlib.import_module("37_rotate_string")


def test_standard_rotation():
    assert module.rotate_string("abcdef", 2) == "efabcd"


def test_k_larger_than_length():
    assert module.rotate_string("abc", 5) == "bca"


def test_negative_k_rotates_left():
    assert module.rotate_string("abcdef", -1) == "bcdefa"


def test_empty_string():
    assert module.rotate_string("", 3) == ""
