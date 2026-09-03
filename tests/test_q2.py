import pytest
import sys

sys.path.append('.')
from src.q2 import validate_password

def test_validate_password_valid():
    """Test that a valid password passes validation."""
    assert validate_password("Password1!")

def test_validate_password_no_uppercase():
    """Test that a password with no uppercase letters fails validation."""
    assert not validate_password("password1!")

def test_validate_password_no_lowercase():
    """Test that a password with no lowercase letters fails validation."""
    assert not validate_password("PASSWORD1!")

def test_validate_password_no_digit():
    """Test that a password with no digits fails validation."""
    assert not validate_password("Password!")

def test_validate_password_no_special_char():
    """Test that a password with no special characters fails validation."""
    assert not validate_password("Password1")

def test_validate_password_too_short():
    """Test that a password that is too short fails validation."""
    assert not validate_password("Pass1!")