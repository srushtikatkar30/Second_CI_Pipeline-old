from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))

import importlib

module = importlib.import_module("34_check_sorted")


def test_sorted_ascending():
    assert module.is_sorted([1, 2, 3, 4, 5]) is True


def test_unsorted_list():
    assert module.is_sorted([1, 3, 2, 4]) is False


def test_empty_and_single_element():
    assert module.is_sorted([]) is True
    assert module.is_sorted([10]) is True


def test_list_with_duplicates():
    assert module.is_sorted([1, 2, 2, 3]) is True
