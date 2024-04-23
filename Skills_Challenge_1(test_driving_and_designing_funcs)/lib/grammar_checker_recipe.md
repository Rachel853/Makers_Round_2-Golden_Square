# grammar_checker Function Design Recipe

## 1. Describe the Problem

As a user
So that I can improve my grammar
I want to verify that a text starts with a capital letter and ends with a suitable sentence-ending punctuation mark.

## 2. Design the Function Signature

_Include the name of the function, its parameters, return value, and side effects._

```python

def grammar_checker(text):
    """Returns True if given text starts with capital letter and ends with sentence-ending punctuation mark
    
    Paramenters: 
        text: String of words to be checked for punctuation
        
    Returns:
        Boolean: True if text starts with capital AND ends with sentence-ending punctuation mark (.!?). False if either of these conditions are not met

    Side effects:
        None"""
    pass 
```

## 3. Create Examples as Tests

_Make a list of examples of what the function will take and return._

```python

"""
Given sentence starting with a capital and ending with full stop, returns True. 
"""
grammar_checker("This is a sentence.") => True

"""Given a sentence starting with a capital letter and ending with a !, returns True.
"""
grammar_checker("This is a sentence!") => True

"""Given a sentence starting with a capital letter and ending with a ?, returns True.
"""
grammar_checker("Is this a sentence?") => True

"""Given a sentence starting with a capital letter and ending with punctuation that is not '.', '!' or '?', returns False
"""
grammar_checker("This is not a sentence,") => False

"""Given a sentence starting with a capital letter and ending with a letter, returns False
"""
grammar_checker("This is not a sentence") => False

"""Given a sentence starting with NO capital letter and ending with sentence-ending punctuation, returns False
"""
grammar_checker("this is not a sentence!") => False

"""Given an empty string, raises an Exception
"""
grammar_checker("") => "No text provided"
```


## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

Here's an example for you to start with:

```python

from lib/grammar_checker import *
import pytest
"""
Given sentence starting with a capital and ending with full stop, returns True. 
"""
def test_grammar_checker_returns_True_when_starts_with_capital_and_ends_with_full_stop():
    assert grammar_checker("This is a sentence.") == True

"""Given a sentence starting with a capital letter and ending with a !, returns True.
"""
grammar_checker("This is a sentence!") => True
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
```