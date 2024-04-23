import pytest
from lib.present import Present

def test_wrap_adds_content_when_first_called():
    present = Present()
    present.wrap("book")
    assert present.contents == "book"

def test_wrap_raises_exception_if_wrap_called_twice():
    present = Present()
    present.wrap("Book")
    with pytest.raises(Exception) as e:
        present.wrap("Toy")
    assert str(e.value) == "A contents has already been wrapped."

def test_unwrap_with_contents_returns_contents():
    present = Present()
    present.wrap("Book")
    assert present.unwrap() == "Book"

def test_unwrap_no_contents_raises_exception():
    present = Present()
    # Note - using alternative to 'assert (x) == (y)' - by using regex match in .raises() method
    with pytest.raises(Exception, match=r"No contents have been wrapped."):
        present.unwrap()
    # assert str(e.value) == "No contents have been wrapped."
