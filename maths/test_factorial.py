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
    logger.debug(">>> Entering test_zero(function=%s)", function)
    assert function(0) == 1
    logger.debug("<<< Exiting test_zero(function=%s)", function)


@pytest.mark.parametrize("function", [factorial, factorial_recursive])
def test_positive_integers(function):
    logger.debug(">>> Entering test_positive_integers(function=%s)", function)
    assert function(1) == 1
    assert function(5) == 120
    assert function(7) == 5040
    logger.debug("<<< Exiting test_positive_integers(function=%s)", function)


@pytest.mark.parametrize("function", [factorial, factorial_recursive])
def test_large_number(function):
    logger.debug(">>> Entering test_large_number(function=%s)", function)
    assert function(10) == 3628800
    logger.debug("<<< Exiting test_large_number(function=%s)", function)


@pytest.mark.parametrize("function", [factorial, factorial_recursive])
def test_negative_number(function):
    logger.debug(">>> Entering test_negative_number(function=%s)", function)
    with pytest.raises(ValueError):
        logger.error("Exception in test_negative_number(function=%s)", function, exc_info=True)
        function(-3)
        logger.debug("<<< Exiting test_negative_number(function=%s)", function)


@pytest.mark.parametrize("function", [factorial, factorial_recursive])
def test_float_number(function):
    logger.debug(">>> Entering test_float_number(function=%s)", function)
    with pytest.raises(ValueError):
        logger.error("Exception in test_float_number(function=%s)", function, exc_info=True)
        function(1.5)
        logger.debug("<<< Exiting test_float_number(function=%s)", function)


if __name__ == "__main__":
    pytest.main(["-v", __file__])
