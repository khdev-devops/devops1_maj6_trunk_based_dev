FEATURE_FLAGS = {
    "is_even": False,
    "count_vowels": False,
    "reverse_string": False,
    "is_palindrome": False,
    "sum_of_squares": False,
    "factorial": False,
    "fibonacci": False,
    "most_common_char": False,
}

def is_even(n):
    """Return True if the number is even."""
    if not FEATURE_FLAGS["is_even"]:
        return NotImplemented
    pass

def count_vowels(text):
    """Return the number of vowels in the given string."""
    if not FEATURE_FLAGS["count_vowels"]:
        return NotImplemented
    pass

def reverse_string(text):
    """Return the reversed string."""
    if not FEATURE_FLAGS["reverse_string"]:
        return NotImplemented
    pass

def is_palindrome(text):
    """Return True if the text is a palindrome (ignoring spaces and case)."""
    if not FEATURE_FLAGS["is_palindrome"]:
        return NotImplemented
    pass

def sum_of_squares(lst):
    """Return the sum of squares of a list of numbers."""
    if not FEATURE_FLAGS["sum_of_squares"]:
        return NotImplemented
    pass

def factorial(n):
    """Return the factorial of a non-negative integer."""
    if not FEATURE_FLAGS["factorial"]:
        return NotImplemented
    pass

def fibonacci(n):
    """Return the n-th Fibonacci number (0-indexed)."""
    if not FEATURE_FLAGS["fibonacci"]:
        return NotImplemented
    pass

def most_common_char(text):
    """Return the most common character in the string (excluding spaces)."""
    if not FEATURE_FLAGS["most_common_char"]:
        return NotImplemented
    pass