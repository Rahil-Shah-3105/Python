# Created by sarathkaul on 12/11/19

# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "httpx",
# ]
# ///

import httpx
import time
import logging
logger = logging.getLogger(__name__)


def send_slack_message(message_body: str, slack_url: str) -> None:
    logger.error(">>> Entering send_slack_message(message_body=%s,slack_url=%s)", message_body, slack_url, extra={"event.action": "send_slack_message", "logrite.message_body": message_body, "logrite.slack_url": slack_url})
    __log_start = time.time()
    headers = {"Content-Type": "application/json"}
    logger.error("send_slack_message(message_body=%s,slack_url=%s): headers → %s", message_body, slack_url, headers, extra={"event.action": "send_slack_message", "logrite.message_body": message_body, "logrite.slack_url": slack_url})
    response = httpx.post(
        slack_url, json={"text": message_body}, headers=headers, timeout=10
    )
    logger.error("send_slack_message(message_body,slack_url)=%s,%s: external service call %s took %s ms", message_body, slack_url, slack_url, int((time.time() - __log_start) * 1000), extra={"event.action": "send_slack_message", "event.category": "network", "logrite.message_body": message_body, "logrite.slack_url": slack_url})
    logger.error("send_slack_message(message_body=%s,slack_url=%s): response → %s", message_body, slack_url, response, extra={"event.action": "send_slack_message", "logrite.message_body": message_body, "logrite.slack_url": slack_url})
    if response.status_code != 200:
        msg = (
            "Request to slack returned an error "
            f"{response.status_code}, the response is:\n{response.text}"
        )
        logger.warning("<<< Exiting send_slack_message(message_body=%s,slack_url=%s)", message_body, slack_url, extra={"event.action": "send_slack_message", "logrite.message_body": message_body, "logrite.slack_url": slack_url})
        raise ValueError(msg)


if __name__ == "__main__":
    # Set the slack url to the one provided by Slack when you create the webhook at
    # https://my.slack.com/services/new/incoming-webhook/
    send_slack_message("<YOUR MESSAGE BODY>", "<SLACK CHANNEL URL>")
