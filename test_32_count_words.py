import importlib
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))

module = importlib.import_module("32_count_words")


def test_standard_sentence():
    assert module.count_words("The quick brown fox") == 4


def test_empty_string():
    assert module.count_words("") == 0


def test_multiple_spaces():
    assert module.count_words("   hello    world   ") == 2


def test_single_word():
    assert module.count_words("Python") == 1
