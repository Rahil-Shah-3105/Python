import json

import httpx

from .fetch_github_info import AUTHENTICATED_USER_ENDPOINT, fetch_github_info
import logging
logger = logging.getLogger(__name__)


def test_fetch_github_info(monkeypatch):
    logger.debug(">>> Entering test_fetch_github_info(monkeypatch=%s)", monkeypatch)
    class FakeResponse:
        def __init__(self, content) -> None:
            logger.debug(">>> Entering __init__(content=%s)", content)
            logger.debug("__init__(self=%s,content=%s): self.content → %s", self, content, self.content)
            assert isinstance(content, (bytes, str))
            logger.debug("<<< Exiting __init__(content=%s)", content)
            self.content = content

        def json(self):
            logger.debug(">>> Entering json()")
            logger.debug("<<< Exiting json()")
            return json.loads(self.content)

    def mock_response(*args, **kwargs):
        logger.debug(">>> Entering mock_response()")
        assert args[0] == AUTHENTICATED_USER_ENDPOINT
        assert "Authorization" in kwargs["headers"]
        assert kwargs["headers"]["Authorization"].startswith("token ")
        assert "Accept" in kwargs["headers"]
        logger.debug("<<< Exiting mock_response()")
        return FakeResponse(b'{"login":"test","id":1}')

    monkeypatch.setattr(httpx, "get", mock_response)
    result = fetch_github_info("token")
    assert result["login"] == "test"
    assert result["id"] == 1
