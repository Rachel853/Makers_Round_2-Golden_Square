from lib.grammar_checker import *
import pytest 

"""
Given sentence starting with a capital and ending with full stop, returns True. 
"""
def test_grammar_checker_returns_True_when_starts_with_capital_and_ends_with_full_stop():
    assert grammar_checker("This is a sentence.") == True

"""Given a sentence starting with a capital letter and ending with a !, returns True.
"""
def test_grammar_checker_returns_True_when_starts_with_capital_and_ends_with_exclamation():
    assert grammar_checker("This is a sentence!") == True

"""Given a sentence starting with a capital letter and ending with a ?, returns True.
"""
def test_grammar_checker_returns_True_when_starts_with_capital_and_ends_with_question():
    assert grammar_checker("This is a sentence?") == True

"""Given a sentence starting with a capital letter and ending with punctuation that is not '.', '!' or '?', returns False
"""
def test_grammar_checker_returns_False_when_starts_with_capital_and_ends_with_other_punction():
    assert grammar_checker("This is not a sentence,") == False

"""Given a sentence starting with a capital letter and ending with a letter, returns False
"""
def test_grammar_checker_returns_False_when_starts_with_capital_and_ends_with_letter():
    assert grammar_checker("This is not a sentence") == False

"""Given a sentence starting with NO capital letter and ending with sentence-ending punctuation, returns False
"""
def test_grammar_checker_returns_False_when_starts_with_no_capital_and_ends_with_sentence_ending_punction():
    assert grammar_checker("this is not a sentence!") == False

"""Given an empty string, raises an Exception
"""
def test_grammar_checker_throws_exception_when_empty_string_provided():
    with pytest.raises(Exception, match=r"No text provided"):
        grammar_checker("")