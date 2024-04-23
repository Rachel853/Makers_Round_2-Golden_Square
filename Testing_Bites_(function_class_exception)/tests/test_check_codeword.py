from lib.check_codeword import check_codeword

# "horse","hose", "he", "h", "e", "catapult"

def test_returns_correct_if_horse():
    assert check_codeword("horse") == "Correct! Come in."

def test_returns_close_with_correct_first_last_letter():
    assert check_codeword("hose") == "Close, but nope."

def test_returns_close_with_he():
    assert check_codeword("he") == "Close, but nope."

def test_returns_wrong_with_h():
    assert check_codeword("h") == "WRONG!"

def test_returns_wrong_with_e():
    assert check_codeword("e") == "WRONG!"

def test_returns_wrong_with_catapult():
    assert check_codeword("catapult") == "WRONG!"