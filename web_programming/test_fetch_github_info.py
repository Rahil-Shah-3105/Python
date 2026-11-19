import json

import httpx

from .fetch_github_info import AUTHENTICATED_USER_ENDPOINT, fetch_github_info
import logging
logger = logging.getLogger(__name__)


def test_fetch_github_info(monkeypatch):
    logger.error(">>> Entering test_fetch_github_info(monkeypatch=%s)", monkeypatch, extra={"event.action": "test_fetch_github_info", "logrite.monkeypatch": monkeypatch})
    class FakeResponse:
        def __init__(self, content) -> None:
            logger.error(">>> Entering __init__(content=%s)", content, extra={"event.action": "__init__", "logrite.content": content})
            assert isinstance(content, (bytes, str))
            logger.warning("<<< Exiting __init__(content=%s)", content, extra={"event.action": "__init__", "logrite.content": content})
            self.content = content
            logger.debug("__init__(self=%s,content=%s): self.content → %s", self, content, self.content, extra={"event.action": "__init__", "logrite.content": content})

        def json(self):
            logger.error(">>> Entering json()", extra={"event.action": "json"})
            logger.warning("<<< Exiting json()", extra={"event.action": "json"})
            return json.loads(self.content)

    def mock_response(*args, **kwargs):
        logger.error(">>> Entering mock_response()", extra={"event.action": "mock_response"})
        assert args[0] == AUTHENTICATED_USER_ENDPOINT
        assert "Authorization" in kwargs["headers"]
        assert kwargs["headers"]["Authorization"].startswith("token ")
        assert "Accept" in kwargs["headers"]
        logger.warning("<<< Exiting mock_response()", extra={"event.action": "mock_response"})
        return FakeResponse(b'{"login":"test","id":1}')

    monkeypatch.setattr(httpx, "get", mock_response)
    result = fetch_github_info("token")
    assert result["login"] == "test"
    assert result["id"] == 1
