import pytest
from lib.password_checker import PasswordChecker

def test_check_with_10_char_password_returns_true():
    password_checker = PasswordChecker()
    assert password_checker.check("1234567890") == True

def test_check_with_8_char_password_returns_true():
    password_checker = PasswordChecker()
    assert password_checker.check("12345678") == True

def test_check_with_7_char_password_returns_false():
    password_checker = PasswordChecker()
    with pytest.raises(Exception) as e:
        password_checker.check("1234567")
    assert str(e.value) == "Invalid password, must be 8+ characters."

def test_check_with_1_char_password_returns_false():
    password_checker = PasswordChecker()
    with pytest.raises(Exception) as e:
        password_checker.check("1")
    assert str(e.value) == "Invalid password, must be 8+ characters."
