#
#import pytest
#from typing import Generator
#from unittest.mock import patch
#from web_programming.test_fetch_github_info import *
#
#from .fake_response import FakeResponse, mock_response
#
#
#from io import BytesIO
#import requests
#from io import BytesIO
#
#
#def test_mock_response() -> None:
#    args = ["https://api.github.com/user"]
#    kwargs = {
#        "headers": {
#            "Authorization": "token test",
#            "Accept": "application/vnd.github.v3+json",
#        }
#    }
#    response = mock_response(*args, **kwargs)
#    assert response is not None
#
#
#def test_content_in_fake_response() -> None:
#    response = FakeResponse(b'{"login":"test","id":1}')
#    assert response is not None
#    assert response.json() is not None
#    assert response.json()["login"] == "test"
#    assert response.json()["id"] == 1
#