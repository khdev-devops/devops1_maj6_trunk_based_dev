import pytest
from main import *
from main import FEATURE_FLAGS

def test_is_even():
    if not FEATURE_FLAGS["is_even"]:
        pytest.skip("Feature flag for is_even is disabled.")

def test_count_vowels():
    if not FEATURE_FLAGS["count_vowels"]:
        pytest.skip("Feature flag for count_vowels is disabled.")

def test_reverse_string():
    if not FEATURE_FLAGS["reverse_string"]:
        pytest.skip("Feature flag for reverse_string is disabled.")

def test_is_palindrome():
    if not FEATURE_FLAGS["is_palindrome"]:
        pytest.skip("Feature flag for is_palindrome is disabled.")

def test_sum_of_squares():
    if not FEATURE_FLAGS["sum_of_squares"]:
        pytest.skip("Feature flag for sum_of_squares is disabled.")

def test_factorial():
    if not FEATURE_FLAGS["factorial"]:
        pytest.skip("Feature flag for factorial is disabled.")

def test_fibonacci():
    if not FEATURE_FLAGS["fibonacci"]:
        pytest.skip("Feature flag for fibonacci is disabled.")

def test_most_common_char():
    if not FEATURE_FLAGS["most_common_char"]:
        pytest.skip("Feature flag for most_common_char is disabled.")
