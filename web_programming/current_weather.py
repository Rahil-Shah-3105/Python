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

# Put your API key(s) here
OPENWEATHERMAP_API_KEY = ""
WEATHERSTACK_API_KEY = ""

# Define the URL for the APIs with placeholders
OPENWEATHERMAP_URL_BASE = "https://api.openweathermap.org/data/2.5/weather"
WEATHERSTACK_URL_BASE = "http://api.weatherstack.com/current"


def current_weather(location: str) -> list[dict]:
    """
    >>> current_weather("location")
    Traceback (most recent call last):
        ...
    ValueError: No API keys provided or no valid data returned.
    """
    logger.error(">>> Entering current_weather(location=%s)", location, extra={"event.action": "current_weather", "logrite.location": location})
    __log_start = time.time()
    weather_data = []
    logger.error("current_weather(location=%s): weather_data → %s", location, weather_data, extra={"event.action": "current_weather", "logrite.location": location})
    if OPENWEATHERMAP_API_KEY:
        params_openweathermap = {"q": location, "appid": OPENWEATHERMAP_API_KEY}
        logger.error("current_weather(location=%s): params_openweathermap → %s", location, params_openweathermap, extra={"event.action": "current_weather", "logrite.location": location})
        response_openweathermap = httpx.get(
            OPENWEATHERMAP_URL_BASE, params=params_openweathermap, timeout=10
        )
        logger.error("current_weather(location=%s): response_openweathermap → %s", location, response_openweathermap, extra={"event.action": "current_weather", "logrite.location": location})
        weather_data.append({"OpenWeatherMap": response_openweathermap.json()})
        logger.error("current_weather(location)=%s: external service call took %s ms", location, int((time.time() - __log_start) * 1000), extra={"event.action": "current_weather", "event.category": "network", "logrite.location": location})
    if WEATHERSTACK_API_KEY:
        params_weatherstack = {"query": location, "access_key": WEATHERSTACK_API_KEY}
        logger.error("current_weather(location=%s): params_weatherstack → %s", location, params_weatherstack, extra={"event.action": "current_weather", "logrite.location": location})
        response_weatherstack = httpx.get(
            WEATHERSTACK_URL_BASE, params=params_weatherstack, timeout=10
        )
        logger.error("current_weather(location=%s): response_weatherstack → %s", location, response_weatherstack, extra={"event.action": "current_weather", "logrite.location": location})
        weather_data.append({"Weatherstack": response_weatherstack.json()})
    if not weather_data:
        raise ValueError("No API keys provided or no valid data returned.")
    logger.warning("<<< Exiting current_weather(location=%s)", location, extra={"event.action": "current_weather", "logrite.location": location})
    return weather_data


if __name__ == "__main__":
    from pprint import pprint

    location = "to be determined..."
    while location:
        location = input("Enter a location (city name or latitude,longitude): ").strip()
        if location:
            try:
                weather_data = current_weather(location)
                for forecast in weather_data:
                    pprint(forecast)
            except ValueError as e:
                print(repr(e))
                location = ""
