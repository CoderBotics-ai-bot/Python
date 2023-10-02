import json

import requests

from .fetch_github_info import AUTHENTICATED_USER_ENDPOINT, fetch_github_info


from typing import Union








def test_fetch_github_info(monkeypatch):
    class FakeResponse:
        def __init__(self, content) -> None:
            assert isinstance(content, (bytes, str))
            self.content = content

        def json(self):
            return json.loads(self.content)

    def mock_response(*args, **kwargs) -> "FakeResponse":
        """
        This static method returns a mocked response that has the expected properties of an
        actual authenticated response from the Github API. It serves for testing purposes.

        Args:
            *args: Arguments passed to this function, the first argument should be the
                expected authenticated user endpoint provided by the API.
            **kwargs: Keyword arguments passed to this function. The headers argument
                should contain "Authorization" and "Accept" keys with relevant values.

        Returns:
            Instance of the FakeResponse.

        Raises:
            AssertionError: If the arguments supplied do not match the expected values.

        """
        assert args[0] == AUTHENTICATED_USER_ENDPOINT
        assert "Authorization" in kwargs["headers"]
        assert kwargs["headers"]["Authorization"].startswith("token ")
        assert "Accept" in kwargs["headers"]
        return FakeResponse(b'{"login":"test","id":1}')


    def json(self):
        # Try to deserialize `_content` into a JSON object.
        return json.loads(self._content)
