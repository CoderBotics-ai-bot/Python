from requests.exceptions import HTTPError
from unittest.mock import MagicMock, patch

import pytest
from web_programming.reddit import *
from typing import Optional


def test_get_subreddit_data_no_errors():
    with patch(
        "requests.get", return_value=MagicMock(json=lambda: {"data": {"children": [0]}})
    ):
        result = get_subreddit_data("dummy_subreddit")
        assert result is not None


def test_get_subreddit_data_with_wanted_data():
    with patch(
        "requests.get",
        return_value=MagicMock(
            json=lambda: {"data": {"children": [{"data": {"score": 10}}]}}
        ),
    ):
        result = get_subreddit_data("dummy_subreddit", wanted_data=["score"])
        assert "score" in result[0]


def test_get_subreddit_data_invalid_wanted_data():
    with pytest.raises(ValueError):
        get_subreddit_data("dummy_subreddit", wanted_data=["invalid_field"])


def test_get_subreddit_data_status_code_429():
    with patch("requests.get", return_value=MagicMock(status_code=429)):
        with pytest.raises(HTTPError):
            get_subreddit_data("dummy_subreddit")
