# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "pytest",
# ]
# ///

import pytest

from maths.factorial import factorial, factorial_recursive
import logging
logger = logging.getLogger(__name__)


@pytest.mark.parametrize("function", [factorial, factorial_recursive])
def test_zero(function):
    logger.error(">>> Entering test_zero(function=%s)", function, extra={"event.action": "test_zero", "logrite.function": function})
    assert function(0) == 1
    logger.warning("<<< Exiting test_zero(function=%s)", function, extra={"event.action": "test_zero", "logrite.function": function})


@pytest.mark.parametrize("function", [factorial, factorial_recursive])
def test_positive_integers(function):
    logger.error(">>> Entering test_positive_integers(function=%s)", function, extra={"event.action": "test_positive_integers", "logrite.function": function})
    assert function(1) == 1
    assert function(5) == 120
    assert function(7) == 5040
    logger.warning("<<< Exiting test_positive_integers(function=%s)", function, extra={"event.action": "test_positive_integers", "logrite.function": function})


@pytest.mark.parametrize("function", [factorial, factorial_recursive])
def test_large_number(function):
    logger.error(">>> Entering test_large_number(function=%s)", function, extra={"event.action": "test_large_number", "logrite.function": function})
    assert function(10) == 3628800
    logger.warning("<<< Exiting test_large_number(function=%s)", function, extra={"event.action": "test_large_number", "logrite.function": function})


@pytest.mark.parametrize("function", [factorial, factorial_recursive])
def test_negative_number(function):
    logger.error(">>> Entering test_negative_number(function=%s)", function, extra={"event.action": "test_negative_number", "logrite.function": function})
    with pytest.raises(ValueError):
        function(-3)
        logger.warning("<<< Exiting test_negative_number(function=%s)", function, extra={"event.action": "test_negative_number", "logrite.function": function})


@pytest.mark.parametrize("function", [factorial, factorial_recursive])
def test_float_number(function):
    logger.error(">>> Entering test_float_number(function=%s)", function, extra={"event.action": "test_float_number", "logrite.function": function})
    with pytest.raises(ValueError):
        function(1.5)
        logger.warning("<<< Exiting test_float_number(function=%s)", function, extra={"event.action": "test_float_number", "logrite.function": function})


if __name__ == "__main__":
    pytest.main(["-v", __file__])
