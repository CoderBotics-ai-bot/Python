from web_programming.emails_from_url import *

import pytest
from unittest.mock import Mock, patch


@patch("requests.get")
def test_emails_from_url_no_errors(mock_get):
    """
    Test emails_from_url function for not throwing any errors
    """
    mock_get.return_value.text = "mock@example.com"
    result = emails_from_url("https://dummy.com")
    assert result is not None


@patch("requests.get")
def test_emails_from_url_valueerror(mock_get):
    """
    Test emails_from_url function for ValueError
    """
    mock_get.side_effect = ValueError("Exception")
    with pytest.raises(SystemExit):
        emails_from_url("https://dummy.com")


@patch("requests.get")
def test_emails_from_url_email_list(mock_get):
    """
    Test emails_from_url function returns correct list
    """
    mock_get.return_value.text = "mock@example.com"
    result = emails_from_url("https://dummy.com")
    assert isinstance(result, list)


@patch("requests.get")
def test_emails_from_url_empty_result(mock_get):
    """
    Test emails_from_url function for empty response
    """
    mock_get.return_value.text = ""
    result = emails_from_url("https://dummy.com")
    assert result == []
