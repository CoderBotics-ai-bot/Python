from web_programming.download_images_from_google_query import *


import os

import pytest
import pytest


def test_download_images_from_google_query():
    result = download_images_from_google_query()
    assert result is not None


def test_download_images_from_google_query_param():
    result = download_images_from_google_query("potato", 10)
    assert result is not None
    assert result <= 10


def test_download_images_from_google_query_max_images():
    result = download_images_from_google_query(max_images=100)
    assert result is not None
    assert result <= 50


def test_download_images_from_google_query_max_images_negative():
    result = download_images_from_google_query(max_images=-10)
    assert result is not None
    assert result <= 0


def test_download_images_from_google_query_empty_query():
    result = download_images_from_google_query(query="")
    assert result is not None
