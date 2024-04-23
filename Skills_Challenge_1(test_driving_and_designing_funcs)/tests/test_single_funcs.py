from lib.single_funcs import *

def test_make_snippet_returns_string_if_fewer_than_five_words():
    assert make_snippet("This is four words") == "This is four words"

def test_make_snippet_returns_string_if_five_words():
    assert make_snippet("This is now five words") == "This is now five words"

def test_make_snippet_returns_string_if_five_words_with_full_stop():
    assert make_snippet("This is now five words.") == "This is now five words."

def test_make_snippet_returns_string_followed_by_ellipses_if_over_five_words():
    assert make_snippet("This is now more than five words") == "This is now more than..."


def test_count_words_returns_three_when_three_words_given():
    assert count_words("Three words here") == 3

def test_count_words_returns_0_when_no_words_given():
    assert count_words("") == 0

def test_count_words_returns_1_when_one_word_given():
    assert count_words("one") == 1