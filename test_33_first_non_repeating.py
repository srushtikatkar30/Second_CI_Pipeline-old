from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))

import importlib

module = importlib.import_module("33_first_non_repeating")


def test_standard_case():
    assert module.first_non_repeating("swiss") == "w"


def test_first_character_is_unique():
    assert module.first_non_repeating("python") == "p"


def test_all_repeating_characters():
    assert module.first_non_repeating("aabbcc") is None


def test_empty_string():
    assert module.first_non_repeating("") is None
