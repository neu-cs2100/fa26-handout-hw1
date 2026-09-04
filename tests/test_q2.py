"""HW1 Question 2 Tests"""

import sys

sys.path.append('.')
from src.q2 import validate_password

def test_validate_password_valid():
    """Test that a valid password passes validation."""
    assert validate_password("Password1!")

def test_validate_password_uppercase():
    """Test that a password with no uppercase letters fails validation, 
    but a valid password passes."""
    assert not validate_password("password1!")
    assert validate_password("Password1!")

def test_validate_password_lowercase():
    """Test that a password with no lowercase letters fails validation, 
    but a valid password passes."""
    assert not validate_password("PASSWORD1!")
    assert validate_password("Password1!")

def test_validate_password_digit():
    """Test that a password with no digits fails validation, 
    but a valid password passes."""
    assert not validate_password("Password!")
    assert validate_password("Password1!")

def test_validate_password_special_char():
    """Test that a password with no special characters fails validation, 
    but a valid password passes."""
    assert not validate_password("Password1")
    assert validate_password("Password1!")

def test_validate_password_length():
    """Test that a password that is too short fails validation, 
    but a valid password passes."""
    assert not validate_password("Pass1!")
    assert validate_password("Password1!")