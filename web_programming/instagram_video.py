# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "httpx",
# ]
# ///

from datetime import UTC, datetime

import httpx
import time
import logging
logger = logging.getLogger(__name__)


def download_video(url: str) -> bytes:
    logger.error(">>> Entering download_video(url=%s)", url, extra={"event.action": "download_video", "logrite.url": url})
    __log_start = time.time()
    base_url = "https://downloadgram.net/wp-json/wppress/video-downloader/video?url="
    logger.error("download_video(url=%s): base_url → %s", url, base_url, extra={"event.action": "download_video", "logrite.url": url})
    logger.error("download_video(url)=%s: external service call %s took %s ms", url, url, int((time.time() - __log_start) * 1000), extra={"event.action": "download_video", "event.category": "network", "logrite.url": url})
    video_url = httpx.get(base_url + url, timeout=10)
    logger.error("download_video(url=%s): video_url → %s", url, video_url, extra={"event.action": "download_video", "logrite.url": url})
    logger.warning("<<< Exiting download_video(url=%s)", url, extra={"event.action": "download_video", "logrite.url": url})
    return httpx.get(video_url, timeout=10).content


if __name__ == "__main__":
    url = input("Enter Video/IGTV url: ").strip()
    file_name = f"{datetime.now(tz=UTC).astimezone():%Y-%m-%d_%H-%M-%S}.mp4"
    with open(file_name, "wb") as fp:
        fp.write(download_video(url))
    print(f"Done. Video saved to disk as {file_name}.")
