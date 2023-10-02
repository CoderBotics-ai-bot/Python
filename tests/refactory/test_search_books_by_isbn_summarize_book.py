#from web_programming.search_books_by_isbn import *
#import pytest
#
#
#@pytest.fixture
#def sample_book_data() -> dict:
#    return {
#        "title": "Python for Dummies",
#        "publish_date": "2004",
#        "authors": [{"key": "/authors/OL27920A"}],
#        "number_of_pages": 352,
#        "first_sentence": {
#            "value": "Python is a high-level, interpreted programming language."
#        },
#        "isbn_10": ["0764548077"],
#        "isbn_13": ["9780764548077"],
#    }
#
#
#def test_summarize_book(sample_book_data: dict):
#    result = summarize_book(sample_book_data)
#    assert result is not None
#
#
#def test_summarize_book_with_missing_key(sample_book_data: dict):
#    del sample_book_data["title"]
#    with pytest.raises(KeyError):
#        summarize_book(sample_book_data)
#
#
#def test_summarize_book_with_empty_authors(sample_book_data: dict):
#    sample_book_data["authors"] = []
#    with pytest.raises(IndexError):
#        summarize_book(sample_book_data)
#