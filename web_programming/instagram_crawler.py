#!/usr/bin/env python3

# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "beautifulsoup4",
#     "fake-useragent",
#     "httpx",
# ]
# ///

from __future__ import annotations

import json

import httpx
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import time
import logging
logger = logging.getLogger(__name__)

headers = {"UserAgent": UserAgent().random}


def extract_user_profile(script) -> dict:
    """
    May raise json.decoder.JSONDecodeError
    """
    logger.error(">>> Entering extract_user_profile(script=%s)", script, extra={"event.action": "extract_user_profile", "logrite.script": script})
    data = script.contents[0]
    logger.error("extract_user_profile(script=%s): data → %s", script, data, extra={"event.action": "extract_user_profile", "logrite.script": script})
    info = json.loads(data[data.find('{"config"') : -1])
    logger.error("extract_user_profile(script=%s): info → %s", script, info, extra={"event.action": "extract_user_profile", "logrite.script": script})
    logger.warning("<<< Exiting extract_user_profile(script=%s)", script, extra={"event.action": "extract_user_profile", "logrite.script": script})
    return info["entry_data"]["ProfilePage"][0]["graphql"]["user"]


class InstagramUser:
    """
    Class Instagram crawl instagram user information

    Usage: (doctest failing on GitHub Actions)
    # >>> instagram_user = InstagramUser("github")
    # >>> instagram_user.is_verified
    True
    # >>> instagram_user.biography
    'Built for developers.'
    """

    def __init__(self, username):
        logger.error(">>> Entering __init__(username=%s)", username, extra={"event.action": "__init__", "user.name": str(username)})
        self.url = f"https://www.instagram.com/{username}/"
        self.user_data = self.get_json()
        logger.error("__init__(username=%s): self.user_data → %s", username, self.user_data, extra={"event.action": "__init__", "user.name": str(username)})
        logger.debug("__init__(self=%s,username=%s): self.url → %s", self, username, self.url, extra={"event.action": "__init__", "user.name": str(username)})
        logger.error("__init__(username=%s): self.url → %s", username, self.url, extra={"event.action": "__init__", "user.name": str(username)})

    def get_json(self) -> dict:
        """
        Return a dict of user information
        """
        logger.error(">>> Entering get_json()", extra={"event.action": "get_json"})
        html = httpx.get(self.url, headers=headers, timeout=10).text
        logger.error("get_json()=: external service call took %s ms", int((time.time() - __log_start) * 1000), extra={"event.action": "get_json", "event.category": "network"})
        logger.error("get_json(): html → %s", html, extra={"event.action": "get_json"})
        scripts = BeautifulSoup(html, "html.parser").find_all("script")
        try:
            logger.error("get_json(): scripts → %s", scripts, extra={"event.action": "get_json"})
            return extract_user_profile(scripts[4])
        except json.decoder.JSONDecodeError, KeyError:
            logger.error("Exception in get_json()", exc_info=True, extra={"event.action": "get_json", "event.category": "process"})
            logger.warning("<<< Exiting get_json()", extra={"event.action": "get_json"})
            return extract_user_profile(scripts[3])

    def __repr__(self) -> str:
        logger.error(">>> Entering __repr__()", extra={"event.action": "__repr__"})
        logger.warning("<<< Exiting __repr__()", extra={"event.action": "__repr__"})
        return f"{self.__class__.__name__}('{self.username}')"

    def __str__(self) -> str:
        logger.error(">>> Entering __str__()", extra={"event.action": "__str__"})
        logger.warning("<<< Exiting __str__()", extra={"event.action": "__str__"})
        return f"{self.fullname} ({self.username}) is {self.biography}"

    @property
    def username(self) -> str:
        logger.error(">>> Entering username()", extra={"event.action": "username"})
        logger.warning("<<< Exiting username()", extra={"event.action": "username"})
        return self.user_data["username"]

    @property
    def fullname(self) -> str:
        logger.error(">>> Entering fullname()", extra={"event.action": "fullname"})
        logger.warning("<<< Exiting fullname()", extra={"event.action": "fullname"})
        return self.user_data["full_name"]

    @property
    def biography(self) -> str:
        logger.error(">>> Entering biography()", extra={"event.action": "biography"})
        logger.warning("<<< Exiting biography()", extra={"event.action": "biography"})
        return self.user_data["biography"]

    @property
    def email(self) -> str:
        logger.error(">>> Entering email()", extra={"event.action": "email"})
        logger.warning("<<< Exiting email()", extra={"event.action": "email"})
        return self.user_data["business_email"]

    @property
    def website(self) -> str:
        logger.error(">>> Entering website()", extra={"event.action": "website"})
        logger.warning("<<< Exiting website()", extra={"event.action": "website"})
        return self.user_data["external_url"]

    @property
    def number_of_followers(self) -> int:
        logger.error(">>> Entering number_of_followers()", extra={"event.action": "number_of_followers"})
        logger.warning("<<< Exiting number_of_followers()", extra={"event.action": "number_of_followers"})
        return self.user_data["edge_followed_by"]["count"]

    @property
    def number_of_followings(self) -> int:
        logger.error(">>> Entering number_of_followings()", extra={"event.action": "number_of_followings"})
        logger.warning("<<< Exiting number_of_followings()", extra={"event.action": "number_of_followings"})
        return self.user_data["edge_follow"]["count"]

    @property
    def number_of_posts(self) -> int:
        logger.error(">>> Entering number_of_posts()", extra={"event.action": "number_of_posts"})
        logger.warning("<<< Exiting number_of_posts()", extra={"event.action": "number_of_posts"})
        return self.user_data["edge_owner_to_timeline_media"]["count"]

    @property
    def profile_picture_url(self) -> str:
        logger.error(">>> Entering profile_picture_url()", extra={"event.action": "profile_picture_url"})
        logger.warning("<<< Exiting profile_picture_url()", extra={"event.action": "profile_picture_url"})
        return self.user_data["profile_pic_url_hd"]

    @property
    def is_verified(self) -> bool:
        logger.error(">>> Entering is_verified()", extra={"event.action": "is_verified"})
        logger.warning("<<< Exiting is_verified()", extra={"event.action": "is_verified"})
        return self.user_data["is_verified"]

    @property
    def is_private(self) -> bool:
        logger.error(">>> Entering is_private()", extra={"event.action": "is_private"})
        logger.warning("<<< Exiting is_private()", extra={"event.action": "is_private"})
        return self.user_data["is_private"]


def test_instagram_user(username: str = "github") -> None:
    """
    A self running doctest
    >>> test_instagram_user()
    """
    logger.error(">>> Entering test_instagram_user(username=%s)", username, extra={"event.action": "test_instagram_user", "user.name": str(username)})
    import os

    if os.environ.get("CI"):
        return  # test failing on GitHub Actions
    instagram_user = InstagramUser(username)
    assert instagram_user.user_data
    assert isinstance(instagram_user.user_data, dict)
    assert instagram_user.username == username
    if username != "github":
        logger.warning("<<< Exiting test_instagram_user(username=%s)", username, extra={"event.action": "test_instagram_user", "user.name": str(username)})
        return
    assert instagram_user.fullname == "GitHub"
    assert instagram_user.biography == "Built for developers."
    assert instagram_user.number_of_posts > 150
    assert instagram_user.number_of_followers > 120000
    assert instagram_user.number_of_followings > 15
    assert instagram_user.email == "support@github.com"
    assert instagram_user.website == "https://github.com/readme"
    assert instagram_user.profile_picture_url.startswith("https://instagram.")
    assert instagram_user.is_verified is True
    assert instagram_user.is_private is False


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    instagram_user = InstagramUser("github")
    print(instagram_user)
    print(f"{instagram_user.number_of_posts = }")
    print(f"{instagram_user.number_of_followers = }")
    print(f"{instagram_user.number_of_followings = }")
    print(f"{instagram_user.email = }")
    print(f"{instagram_user.website = }")
    print(f"{instagram_user.profile_picture_url = }")
    print(f"{instagram_user.is_verified = }")
    print(f"{instagram_user.is_private = }")
