import pytest
from utils.urlstools import get_domain, valid, clean


def test_get_domain():
    assert get_domain("https://www.bbc.co.uk/test") == "www.bbc.co.uk"


def test_valid_true():
    assert valid("https://www.bbc.co.uk/test", "www.bbc.co.uk")


def test_valid_false():
    assert not valid("https://www.bbc.co.uk/test", "stackoverflow.com")


def test_clean():
    assert clean("https://www.bbc.co.uk/test/6544") == "https://www.bbc.co.uk/test/6544"
    assert clean("https://www.bbc.co.uk/test/6544/") == "https://www.bbc.co.uk/test/6544"
    assert clean("www.bbc.co.uk/test/6544/#") == "http://www.bbc.co.uk/test/6544"


def test_dummy():
    assert True
