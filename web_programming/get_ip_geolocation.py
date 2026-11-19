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


# Function to get geolocation data for an IP address
def get_ip_geolocation(ip_address: str) -> str:
    logger.error(">>> Entering get_ip_geolocation(ip_address=%s)", ip_address, extra={"event.action": "get_ip_geolocation", "logrite.ip_address": ip_address})
    try:
        # Construct the URL for the IP geolocation API
        url = f"https://ipinfo.io/{ip_address}/json"
        logger.error("get_ip_geolocation(ip_address=%s): url → %s", ip_address, url, extra={"event.action": "get_ip_geolocation", "logrite.ip_address": ip_address})
        __log_start = time.time()

        # Send a GET request to the API
        response = httpx.get(url, timeout=10)
        logger.error("get_ip_geolocation(ip_address=%s): response → %s", ip_address, response, extra={"event.action": "get_ip_geolocation", "logrite.ip_address": ip_address})
        logger.error("get_ip_geolocation(ip_address)=%s: external service call %s took %s ms", ip_address, url, int((time.time() - __log_start) * 1000), extra={"event.action": "get_ip_geolocation", "event.category": "network", "logrite.ip_address": ip_address})

        # Check if the HTTP request was successful
        response.raise_for_status()

        # Parse the response as JSON
        data = response.json()
        logger.error("get_ip_geolocation(ip_address=%s): data → %s", ip_address, data, extra={"event.action": "get_ip_geolocation", "logrite.ip_address": ip_address})

        # Check if city, region, and country information is available
        if "city" in data and "region" in data and "country" in data:
            location = f"Location: {data['city']}, {data['region']}, {data['country']}"
        else:
            location = "Location data not found."
        logger.error("get_ip_geolocation(ip_address=%s): location → %s", ip_address, location, extra={"event.action": "get_ip_geolocation", "logrite.ip_address": ip_address})

        return location
    except httpx.RequestError as e:
        logger.error("Exception in get_ip_geolocation(ip_address=%s): %s", ip_address, str(e), exc_info=True, extra={"event.action": "get_ip_geolocation", "event.category": "process", "logrite.ip_address": ip_address})
        # Handle network-related exceptions
        return f"Request error: {e}"
    except ValueError as e:
        # Handle JSON parsing errors
        logger.warning("<<< Exiting get_ip_geolocation(ip_address=%s)", ip_address, extra={"event.action": "get_ip_geolocation", "logrite.ip_address": ip_address})
        return f"JSON parsing error: {e}"


if __name__ == "__main__":
    # Prompt the user to enter an IP address
    ip_address = input("Enter an IP address: ")

    # Get the geolocation data and print it
    location = get_ip_geolocation(ip_address)
    print(location)
