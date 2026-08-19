# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "httpx",
# ]
# ///

import httpx
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
    logger.debug(">>> Entering current_weather(location=%s)", location)
    logger.info("current_weather(location)=%s: external service call took %s ms", location, int((time.time() - __log_start) * 1000))
    logger.debug("current_weather(location=%s): response_openweathermap → %s", location, response_openweathermap)
    logger.debug("current_weather(location=%s): params_openweathermap → %s", location, params_openweathermap)
    weather_data = []
    logger.debug("current_weather(location=%s): weather_data → %s", location, weather_data)
    if OPENWEATHERMAP_API_KEY:
        params_openweathermap = {"q": location, "appid": OPENWEATHERMAP_API_KEY}
        response_openweathermap = httpx.get(
            OPENWEATHERMAP_URL_BASE, params=params_openweathermap, timeout=10
        )
        weather_data.append({"OpenWeatherMap": response_openweathermap.json()})
        logger.debug("current_weather(location=%s): response_weatherstack → %s", location, response_weatherstack)
    if WEATHERSTACK_API_KEY:
        params_weatherstack = {"query": location, "access_key": WEATHERSTACK_API_KEY}
        logger.debug("current_weather(location=%s): params_weatherstack → %s", location, params_weatherstack)
        response_weatherstack = httpx.get(
            WEATHERSTACK_URL_BASE, params=params_weatherstack, timeout=10
        )
        weather_data.append({"Weatherstack": response_weatherstack.json()})
    if not weather_data:
        raise ValueError("No API keys provided or no valid data returned.")
    logger.debug("<<< Exiting current_weather(location=%s)", location)
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
