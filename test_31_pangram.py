import importlib
from pathlib import Path
import sys

# Ensure current directory is in Python path for module importing
sys.path.insert(0, str(Path(__file__).resolve().parent))

module = importlib.import_module("31_pangram")


def test_pangram_true():
    assert module.is_pangram("The quick brown fox jumps over the lazy dog") is True


def test_pangram_false():
    assert module.is_pangram("Hello World") is False


def test_pangram_with_numbers_and_punctuation():
    assert module.is_pangram("Pack my box with five dozen liquor jugs! 12345") is True


def test_empty_string():
    assert module.is_pangram("") is False
