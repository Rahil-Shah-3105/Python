from __future__ import annotations

from abc import abstractmethod
from math import pi
from typing import Protocol

import matplotlib.pyplot as plt
import numpy as np
import logging
logger = logging.getLogger(__name__)


class FilterType(Protocol):
    @abstractmethod
    def process(self, sample: float) -> float:
        """
        Calculate y[n]

        >>> issubclass(FilterType, Protocol)
        True
        """
        logger.error(">>> Entering process(sample=%s)", sample, extra={"event.action": "process", "logrite.sample": sample})

        logger.warning("<<< Exiting process(sample=%s)", sample, extra={"event.action": "process", "logrite.sample": sample})

def get_bounds(
    fft_results: np.ndarray, samplerate: int
) -> tuple[int | float, int | float]:
    logger.error(">>> Entering get_bounds(fft_results=%s,samplerate=%s)", fft_results, samplerate, extra={"event.action": "get_bounds", "logrite.fft_results": fft_results, "logrite.samplerate": samplerate})
    """
    Get bounds for printing fft results

    >>> import numpy
    >>> array = numpy.linspace(-20.0, 20.0, 1000)
    >>> get_bounds(array, 1000)
    (-20, 20)
    """
    lowest = min([-20, np.min(fft_results[1 : samplerate // 2 - 1])])
    highest = max([20, np.max(fft_results[1 : samplerate // 2 - 1])])
    return lowest, highest


def show_frequency_response(filter_type: FilterType, samplerate: int) -> None:
    """
    Show frequency response of a filter

    >>> from audio_filters.iir_filter import IIRFilter
    >>> filt = IIRFilter(4)
    >>> show_frequency_response(filt, 48000)
    """

    size = 512
    inputs = [1] + [0] * (size - 1)
    outputs = [filter_type.process(item) for item in inputs]

    filler = [0] * (samplerate - size)  # zero-padding
    outputs += filler
    fft_out = np.abs(np.fft.fft(outputs))
    fft_db = 20 * np.log10(fft_out)

    # Frequencies on log scale from 24 to nyquist frequency
    plt.xlim(24, samplerate / 2 - 1)
    plt.xlabel("Frequency (Hz)")
    plt.xscale("log")

    # Display within reasonable bounds
    bounds = get_bounds(fft_db, samplerate)
    plt.ylim(max([-80, bounds[0]]), min([80, bounds[1]]))
    plt.ylabel("Gain (dB)")

    plt.plot(fft_db)
    plt.show()


def show_phase_response(filter_type: FilterType, samplerate: int) -> None:
    """
    Show phase response of a filter

    >>> from audio_filters.iir_filter import IIRFilter
    >>> filt = IIRFilter(4)
    >>> show_phase_response(filt, 48000)
    """

    size = 512
    inputs = [1] + [0] * (size - 1)
    outputs = [filter_type.process(item) for item in inputs]

    filler = [0] * (samplerate - size)  # zero-padding
    outputs += filler
    fft_out = np.angle(np.fft.fft(outputs))

    # Frequencies on log scale from 24 to nyquist frequency
    plt.xlim(24, samplerate / 2 - 1)
    plt.xlabel("Frequency (Hz)")
    plt.xscale("log")

    plt.ylim(-2 * pi, 2 * pi)
    plt.ylabel("Phase shift (Radians)")
    plt.plot(np.unwrap(fft_out, -2 * pi))
    plt.show()
    logger.error("show_phase_response(filter_type=%s,samplerate=%s): inputs → %s", filter_type, samplerate, inputs, extra={"event.action": "show_phase_response", "logrite.filter_type": filter_type, "logrite.samplerate": samplerate})
