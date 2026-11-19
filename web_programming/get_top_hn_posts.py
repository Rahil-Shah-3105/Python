# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "httpx",
# ]
# ///

from __future__ import annotations

import httpx
import time
import logging
logger = logging.getLogger(__name__)


def get_hackernews_story(story_id: str) -> dict:
    logger.error(">>> Entering get_hackernews_story(story_id=%s)", story_id, extra={"event.action": "get_hackernews_story", "logrite.story_id": story_id})
    __log_start = time.time()
    url = f"https://hacker-news.firebaseio.com/v0/item/{story_id}.json?print=pretty"
    logger.error("get_hackernews_story(story_id=%s): url → %s", story_id, url, extra={"event.action": "get_hackernews_story", "logrite.story_id": story_id})
    logger.error("get_hackernews_story(story_id)=%s: external service call took %s ms", story_id, int((time.time() - __log_start) * 1000), extra={"event.action": "get_hackernews_story", "event.category": "network", "logrite.story_id": story_id})
    logger.warning("<<< Exiting get_hackernews_story(story_id=%s)", story_id, extra={"event.action": "get_hackernews_story", "logrite.story_id": story_id})
    return httpx.get(url, timeout=10).json()


def hackernews_top_stories(max_stories: int = 10) -> list[dict]:
    """
    Get the top max_stories posts from HackerNews - https://news.ycombinator.com/
    """
    logger.error(">>> Entering hackernews_top_stories(max_stories=%s)", max_stories, extra={"event.action": "hackernews_top_stories", "logrite.max_stories": max_stories})
    __log_start = time.time()
    url = "https://hacker-news.firebaseio.com/v0/topstories.json?print=pretty"
    logger.error("hackernews_top_stories(max_stories)=%s: external service call took %s ms", max_stories, int((time.time() - __log_start) * 1000), extra={"event.action": "hackernews_top_stories", "event.category": "network", "logrite.max_stories": max_stories})
    story_ids = httpx.get(url, timeout=10).json()[:max_stories]
    logger.error("hackernews_top_stories(max_stories=%s): url → %s", max_stories, url, extra={"event.action": "hackernews_top_stories", "logrite.max_stories": max_stories})
    logger.error("hackernews_top_stories(max_stories=%s): story_ids → %s", max_stories, story_ids, extra={"event.action": "hackernews_top_stories", "logrite.max_stories": max_stories})
    logger.warning("<<< Exiting hackernews_top_stories(max_stories=%s)", max_stories, extra={"event.action": "hackernews_top_stories", "logrite.max_stories": max_stories})
    return [get_hackernews_story(story_id) for story_id in story_ids]


def hackernews_top_stories_as_markdown(max_stories: int = 10) -> str:
    logger.error(">>> Entering hackernews_top_stories_as_markdown(max_stories=%s)", max_stories, extra={"event.action": "hackernews_top_stories_as_markdown", "logrite.max_stories": max_stories})
    stories = hackernews_top_stories(max_stories)
    logger.error("hackernews_top_stories_as_markdown(max_stories=%s): stories → %s", max_stories, stories, extra={"event.action": "hackernews_top_stories_as_markdown", "logrite.max_stories": max_stories})
    logger.warning("<<< Exiting hackernews_top_stories_as_markdown(max_stories=%s)", max_stories, extra={"event.action": "hackernews_top_stories_as_markdown", "logrite.max_stories": max_stories})
    return "\n".join("* [{title}]({url})".format(**story) for story in stories)


if __name__ == "__main__":
    print(hackernews_top_stories_as_markdown())
