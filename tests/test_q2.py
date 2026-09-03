import pytest
import sys

sys.path.append('.')
from src.q2 import validate_password

def test_validate_password_valid():
    assert validate_password("Password1!")

def test_validate_password_no_uppercase():
    assert not validate_password("password1!")

def test_validate_password_no_lowercase():
    assert not validate_password("PASSWORD1!")

def test_validate_password_no_digit():
    assert not validate_password("Password!")

def test_validate_password_no_special_char():
    assert not validate_password("Password1")

def test_validate_password_too_short():
    assert not validate_password("Pass1!")