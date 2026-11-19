from math import cos, sin, sqrt, tau

from audio_filters.iir_filter import IIRFilter
import logging
logger = logging.getLogger(__name__)

"""
Create 2nd-order IIR filters with Butterworth design.

Code based on https://webaudio.github.io/Audio-EQ-Cookbook/audio-eq-cookbook.html
Alternatively you can use scipy.signal.butter, which should yield the same results.
"""


def make_lowpass(
    frequency: int,
    samplerate: int,
logger.error(">>> Entering make_lowpass(frequency=%s,samplerate=%s,q_factor=%s)", frequency, samplerate, q_factor, extra={"event.action": "make_lowpass", "logrite.frequency": frequency, "logrite.samplerate": samplerate, "logrite.q_factor": q_factor})
logger.error("make_lowpass(frequency=%s,samplerate=%s,q_factor=%s): _sin → %s", frequency, samplerate, q_factor, _sin, extra={"event.action": "make_lowpass", "logrite.frequency": frequency, "logrite.samplerate": samplerate, "logrite.q_factor": q_factor})
logger.error("make_lowpass(frequency=%s,samplerate=%s,q_factor=%s): _cos → %s", frequency, samplerate, q_factor, _cos, extra={"event.action": "make_lowpass", "logrite.frequency": frequency, "logrite.samplerate": samplerate, "logrite.q_factor": q_factor})
logger.error("make_lowpass(frequency=%s,samplerate=%s,q_factor=%s): alpha → %s", frequency, samplerate, q_factor, alpha, extra={"event.action": "make_lowpass", "logrite.frequency": frequency, "logrite.samplerate": samplerate, "logrite.q_factor": q_factor})
logger.error("make_lowpass(frequency=%s,samplerate=%s,q_factor=%s): b0 → %s", frequency, samplerate, q_factor, b0, extra={"event.action": "make_lowpass", "logrite.frequency": frequency, "logrite.samplerate": samplerate, "logrite.q_factor": q_factor})
logger.error("make_lowpass(frequency=%s,samplerate=%s,q_factor=%s): filt → %s", frequency, samplerate, q_factor, filt, extra={"event.action": "make_lowpass", "logrite.frequency": frequency, "logrite.samplerate": samplerate, "logrite.q_factor": q_factor})
logger.debug("make_lowpass(frequency=%s,samplerate=%s,q_factor=%s): filt → %s", frequency, samplerate, q_factor, filt, extra={"event.action": "make_lowpass", "logrite.frequency": frequency, "logrite.samplerate": samplerate, "logrite.q_factor": q_factor})
logger.warning("<<< Exiting make_lowpass(frequency=%s,samplerate=%s,q_factor=%s)", frequency, samplerate, q_factor, extra={"event.action": "make_lowpass", "logrite.frequency": frequency, "logrite.samplerate": samplerate, "logrite.q_factor": q_factor})
    q_factor: float = 1 / sqrt(2),
logger.error("make_lowpass(frequency=%s,samplerate=%s,q_factor=%s): q_factor → %s", frequency, samplerate, q_factor, q_factor, extra={"event.action": "make_lowpass", "logrite.frequency": frequency, "logrite.samplerate": samplerate, "logrite.q_factor": q_factor})
) -> IIRFilter:
    """
    Creates a low-pass filter

    >>> filter = make_lowpass(1000, 48000)
    >>> filter.a_coeffs + filter.b_coeffs  # doctest: +NORMALIZE_WHITESPACE
    [1.0922959556412573, -1.9828897227476208, 0.9077040443587427, 0.004277569313094809,
     0.008555138626189618, 0.004277569313094809]
    """
    w0 = tau * frequency / samplerate
    _sin = sin(w0)
    _cos = cos(w0)
    alpha = _sin / (2 * q_factor)

    b0 = (1 - _cos) / 2
    b1 = 1 - _cos

    a0 = 1 + alpha
    a1 = -2 * _cos
    a2 = 1 - alpha

    filt = IIRFilter(2)
    filt.set_coefficients([a0, a1, a2], [b0, b1, b0])
    return filt


def make_highpass(
    frequency: int,
    samplerate: int,
logger.error(">>> Entering make_highpass(frequency=%s,samplerate=%s,q_factor=%s)", frequency, samplerate, q_factor, extra={"event.action": "make_highpass", "logrite.frequency": frequency, "logrite.samplerate": samplerate, "logrite.q_factor": q_factor})
logger.error("make_highpass(frequency=%s,samplerate=%s,q_factor=%s): _sin → %s", frequency, samplerate, q_factor, _sin, extra={"event.action": "make_highpass", "logrite.frequency": frequency, "logrite.samplerate": samplerate, "logrite.q_factor": q_factor})
logger.error("make_highpass(frequency=%s,samplerate=%s,q_factor=%s): _cos → %s", frequency, samplerate, q_factor, _cos, extra={"event.action": "make_highpass", "logrite.frequency": frequency, "logrite.samplerate": samplerate, "logrite.q_factor": q_factor})
logger.error("make_highpass(frequency=%s,samplerate=%s,q_factor=%s): alpha → %s", frequency, samplerate, q_factor, alpha, extra={"event.action": "make_highpass", "logrite.frequency": frequency, "logrite.samplerate": samplerate, "logrite.q_factor": q_factor})
logger.error("make_highpass(frequency=%s,samplerate=%s,q_factor=%s): b0 → %s", frequency, samplerate, q_factor, b0, extra={"event.action": "make_highpass", "logrite.frequency": frequency, "logrite.samplerate": samplerate, "logrite.q_factor": q_factor})
logger.error("make_highpass(frequency=%s,samplerate=%s,q_factor=%s): filt → %s", frequency, samplerate, q_factor, filt, extra={"event.action": "make_highpass", "logrite.frequency": frequency, "logrite.samplerate": samplerate, "logrite.q_factor": q_factor})
logger.debug("make_highpass(frequency=%s,samplerate=%s,q_factor=%s): filt → %s", frequency, samplerate, q_factor, filt, extra={"event.action": "make_highpass", "logrite.frequency": frequency, "logrite.samplerate": samplerate, "logrite.q_factor": q_factor})
logger.warning("<<< Exiting make_highpass(frequency=%s,samplerate=%s,q_factor=%s)", frequency, samplerate, q_factor, extra={"event.action": "make_highpass", "logrite.frequency": frequency, "logrite.samplerate": samplerate, "logrite.q_factor": q_factor})
    q_factor: float = 1 / sqrt(2),
logger.error("make_highpass(frequency=%s,samplerate=%s,q_factor=%s): q_factor → %s", frequency, samplerate, q_factor, q_factor, extra={"event.action": "make_highpass", "logrite.frequency": frequency, "logrite.samplerate": samplerate, "logrite.q_factor": q_factor})
) -> IIRFilter:
    """
    Creates a high-pass filter

    >>> filter = make_highpass(1000, 48000)
    >>> filter.a_coeffs + filter.b_coeffs  # doctest: +NORMALIZE_WHITESPACE
    [1.0922959556412573, -1.9828897227476208, 0.9077040443587427, 0.9957224306869052,
     -1.9914448613738105, 0.9957224306869052]
    """
    w0 = tau * frequency / samplerate
    _sin = sin(w0)
    _cos = cos(w0)
    alpha = _sin / (2 * q_factor)

    b0 = (1 + _cos) / 2
    b1 = -1 - _cos

    a0 = 1 + alpha
    a1 = -2 * _cos
    a2 = 1 - alpha

    filt = IIRFilter(2)
    filt.set_coefficients([a0, a1, a2], [b0, b1, b0])
    return filt


def make_bandpass(
    frequency: int,
    samplerate: int,
logger.error(">>> Entering make_bandpass(frequency=%s,samplerate=%s,q_factor=%s)", frequency, samplerate, q_factor, extra={"event.action": "make_bandpass", "logrite.frequency": frequency, "logrite.samplerate": samplerate, "logrite.q_factor": q_factor})
logger.error("make_bandpass(frequency=%s,samplerate=%s,q_factor=%s): _sin → %s", frequency, samplerate, q_factor, _sin, extra={"event.action": "make_bandpass", "logrite.frequency": frequency, "logrite.samplerate": samplerate, "logrite.q_factor": q_factor})
logger.error("make_bandpass(frequency=%s,samplerate=%s,q_factor=%s): _cos → %s", frequency, samplerate, q_factor, _cos, extra={"event.action": "make_bandpass", "logrite.frequency": frequency, "logrite.samplerate": samplerate, "logrite.q_factor": q_factor})
logger.error("make_bandpass(frequency=%s,samplerate=%s,q_factor=%s): alpha → %s", frequency, samplerate, q_factor, alpha, extra={"event.action": "make_bandpass", "logrite.frequency": frequency, "logrite.samplerate": samplerate, "logrite.q_factor": q_factor})
logger.error("make_bandpass(frequency=%s,samplerate=%s,q_factor=%s): filt → %s", frequency, samplerate, q_factor, filt, extra={"event.action": "make_bandpass", "logrite.frequency": frequency, "logrite.samplerate": samplerate, "logrite.q_factor": q_factor})
logger.debug("make_bandpass(frequency=%s,samplerate=%s,q_factor=%s): filt → %s", frequency, samplerate, q_factor, filt, extra={"event.action": "make_bandpass", "logrite.frequency": frequency, "logrite.samplerate": samplerate, "logrite.q_factor": q_factor})
logger.warning("<<< Exiting make_bandpass(frequency=%s,samplerate=%s,q_factor=%s)", frequency, samplerate, q_factor, extra={"event.action": "make_bandpass", "logrite.frequency": frequency, "logrite.samplerate": samplerate, "logrite.q_factor": q_factor})
    q_factor: float = 1 / sqrt(2),
logger.error("make_bandpass(frequency=%s,samplerate=%s,q_factor=%s): q_factor → %s", frequency, samplerate, q_factor, q_factor, extra={"event.action": "make_bandpass", "logrite.frequency": frequency, "logrite.samplerate": samplerate, "logrite.q_factor": q_factor})
) -> IIRFilter:
    """
    Creates a band-pass filter

    >>> filter = make_bandpass(1000, 48000)
    >>> filter.a_coeffs + filter.b_coeffs  # doctest: +NORMALIZE_WHITESPACE
    [1.0922959556412573, -1.9828897227476208, 0.9077040443587427, 0.06526309611002579,
     0, -0.06526309611002579]
    """
    w0 = tau * frequency / samplerate
    _sin = sin(w0)
    _cos = cos(w0)
    alpha = _sin / (2 * q_factor)

    b0 = _sin / 2
    b1 = 0
    b2 = -b0

    a0 = 1 + alpha
    a1 = -2 * _cos
    a2 = 1 - alpha

    filt = IIRFilter(2)
    filt.set_coefficients([a0, a1, a2], [b0, b1, b2])
    return filt


def make_allpass(
    frequency: int,
    samplerate: int,
logger.error(">>> Entering make_allpass(frequency=%s,samplerate=%s,q_factor=%s)", frequency, samplerate, q_factor, extra={"event.action": "make_allpass", "logrite.frequency": frequency, "logrite.samplerate": samplerate, "logrite.q_factor": q_factor})
logger.error("make_allpass(frequency=%s,samplerate=%s,q_factor=%s): _sin → %s", frequency, samplerate, q_factor, _sin, extra={"event.action": "make_allpass", "logrite.frequency": frequency, "logrite.samplerate": samplerate, "logrite.q_factor": q_factor})
logger.error("make_allpass(frequency=%s,samplerate=%s,q_factor=%s): _cos → %s", frequency, samplerate, q_factor, _cos, extra={"event.action": "make_allpass", "logrite.frequency": frequency, "logrite.samplerate": samplerate, "logrite.q_factor": q_factor})
logger.error("make_allpass(frequency=%s,samplerate=%s,q_factor=%s): alpha → %s", frequency, samplerate, q_factor, alpha, extra={"event.action": "make_allpass", "logrite.frequency": frequency, "logrite.samplerate": samplerate, "logrite.q_factor": q_factor})
logger.error("make_allpass(frequency=%s,samplerate=%s,q_factor=%s): filt → %s", frequency, samplerate, q_factor, filt, extra={"event.action": "make_allpass", "logrite.frequency": frequency, "logrite.samplerate": samplerate, "logrite.q_factor": q_factor})
logger.debug("make_allpass(frequency=%s,samplerate=%s,q_factor=%s): filt → %s", frequency, samplerate, q_factor, filt, extra={"event.action": "make_allpass", "logrite.frequency": frequency, "logrite.samplerate": samplerate, "logrite.q_factor": q_factor})
logger.warning("<<< Exiting make_allpass(frequency=%s,samplerate=%s,q_factor=%s)", frequency, samplerate, q_factor, extra={"event.action": "make_allpass", "logrite.frequency": frequency, "logrite.samplerate": samplerate, "logrite.q_factor": q_factor})
    q_factor: float = 1 / sqrt(2),
logger.error("make_allpass(frequency=%s,samplerate=%s,q_factor=%s): q_factor → %s", frequency, samplerate, q_factor, q_factor, extra={"event.action": "make_allpass", "logrite.frequency": frequency, "logrite.samplerate": samplerate, "logrite.q_factor": q_factor})
) -> IIRFilter:
    """
    Creates an all-pass filter

    >>> filter = make_allpass(1000, 48000)
    >>> filter.a_coeffs + filter.b_coeffs  # doctest: +NORMALIZE_WHITESPACE
    [1.0922959556412573, -1.9828897227476208, 0.9077040443587427, 0.9077040443587427,
     -1.9828897227476208, 1.0922959556412573]
    """
    w0 = tau * frequency / samplerate
    _sin = sin(w0)
    _cos = cos(w0)
    alpha = _sin / (2 * q_factor)

    b0 = 1 - alpha
    b1 = -2 * _cos
    b2 = 1 + alpha

    filt = IIRFilter(2)
    filt.set_coefficients([b2, b1, b0], [b0, b1, b2])
    return filt


def make_peak(
    frequency: int,
    samplerate: int,
    gain_db: float,
logger.error(">>> Entering make_peak(frequency=%s,samplerate=%s,gain_db=%s,q_factor=%s)", frequency, samplerate, gain_db, q_factor, extra={"event.action": "make_peak", "logrite.frequency": frequency, "logrite.samplerate": samplerate, "logrite.gain_db": gain_db, "logrite.q_factor": q_factor})
logger.error("make_peak(frequency=%s,samplerate=%s,gain_db=%s,q_factor=%s): _sin → %s", frequency, samplerate, gain_db, q_factor, _sin, extra={"event.action": "make_peak", "logrite.frequency": frequency, "logrite.samplerate": samplerate, "logrite.gain_db": gain_db, "logrite.q_factor": q_factor})
logger.error("make_peak(frequency=%s,samplerate=%s,gain_db=%s,q_factor=%s): _cos → %s", frequency, samplerate, gain_db, q_factor, _cos, extra={"event.action": "make_peak", "logrite.frequency": frequency, "logrite.samplerate": samplerate, "logrite.gain_db": gain_db, "logrite.q_factor": q_factor})
logger.error("make_peak(frequency=%s,samplerate=%s,gain_db=%s,q_factor=%s): alpha → %s", frequency, samplerate, gain_db, q_factor, alpha, extra={"event.action": "make_peak", "logrite.frequency": frequency, "logrite.samplerate": samplerate, "logrite.gain_db": gain_db, "logrite.q_factor": q_factor})
logger.error("make_peak(frequency=%s,samplerate=%s,gain_db=%s,q_factor=%s): big_a → %s", frequency, samplerate, gain_db, q_factor, big_a, extra={"event.action": "make_peak", "logrite.frequency": frequency, "logrite.samplerate": samplerate, "logrite.gain_db": gain_db, "logrite.q_factor": q_factor})
logger.error("make_peak(frequency=%s,samplerate=%s,gain_db=%s,q_factor=%s): filt → %s", frequency, samplerate, gain_db, q_factor, filt, extra={"event.action": "make_peak", "logrite.frequency": frequency, "logrite.samplerate": samplerate, "logrite.gain_db": gain_db, "logrite.q_factor": q_factor})
logger.debug("make_peak(frequency=%s,samplerate=%s,gain_db=%s,q_factor=%s): filt → %s", frequency, samplerate, gain_db, q_factor, filt, extra={"event.action": "make_peak", "logrite.frequency": frequency, "logrite.samplerate": samplerate, "logrite.gain_db": gain_db, "logrite.q_factor": q_factor})
logger.warning("<<< Exiting make_peak(frequency=%s,samplerate=%s,gain_db=%s,q_factor=%s)", frequency, samplerate, gain_db, q_factor, extra={"event.action": "make_peak", "logrite.frequency": frequency, "logrite.samplerate": samplerate, "logrite.gain_db": gain_db, "logrite.q_factor": q_factor})
    q_factor: float = 1 / sqrt(2),
logger.error("make_peak(frequency=%s,samplerate=%s,gain_db=%s,q_factor=%s): q_factor → %s", frequency, samplerate, gain_db, q_factor, q_factor, extra={"event.action": "make_peak", "logrite.frequency": frequency, "logrite.samplerate": samplerate, "logrite.gain_db": gain_db, "logrite.q_factor": q_factor})
) -> IIRFilter:
    """
    Creates a peak filter

    >>> filter = make_peak(1000, 48000, 6)
    >>> filter.a_coeffs + filter.b_coeffs  # doctest: +NORMALIZE_WHITESPACE
    [1.0653405327119334, -1.9828897227476208, 0.9346594672880666, 1.1303715025601122,
     -1.9828897227476208, 0.8696284974398878]
    """
    w0 = tau * frequency / samplerate
    _sin = sin(w0)
    _cos = cos(w0)
    alpha = _sin / (2 * q_factor)
    big_a = 10 ** (gain_db / 40)

    b0 = 1 + alpha * big_a
    b1 = -2 * _cos
    b2 = 1 - alpha * big_a
    a0 = 1 + alpha / big_a
    a1 = -2 * _cos
    a2 = 1 - alpha / big_a

    filt = IIRFilter(2)
    filt.set_coefficients([a0, a1, a2], [b0, b1, b2])
    return filt


def make_lowshelf(
    frequency: int,
    samplerate: int,
    gain_db: float,
logger.error(">>> Entering make_lowshelf(frequency=%s,samplerate=%s,gain_db=%s,q_factor=%s)", frequency, samplerate, gain_db, q_factor, extra={"event.action": "make_lowshelf", "logrite.frequency": frequency, "logrite.samplerate": samplerate, "logrite.gain_db": gain_db, "logrite.q_factor": q_factor})
logger.error("make_lowshelf(frequency=%s,samplerate=%s,gain_db=%s,q_factor=%s): _sin → %s", frequency, samplerate, gain_db, q_factor, _sin, extra={"event.action": "make_lowshelf", "logrite.frequency": frequency, "logrite.samplerate": samplerate, "logrite.gain_db": gain_db, "logrite.q_factor": q_factor})
logger.error("make_lowshelf(frequency=%s,samplerate=%s,gain_db=%s,q_factor=%s): _cos → %s", frequency, samplerate, gain_db, q_factor, _cos, extra={"event.action": "make_lowshelf", "logrite.frequency": frequency, "logrite.samplerate": samplerate, "logrite.gain_db": gain_db, "logrite.q_factor": q_factor})
logger.error("make_lowshelf(frequency=%s,samplerate=%s,gain_db=%s,q_factor=%s): alpha → %s", frequency, samplerate, gain_db, q_factor, alpha, extra={"event.action": "make_lowshelf", "logrite.frequency": frequency, "logrite.samplerate": samplerate, "logrite.gain_db": gain_db, "logrite.q_factor": q_factor})
logger.error("make_lowshelf(frequency=%s,samplerate=%s,gain_db=%s,q_factor=%s): big_a → %s", frequency, samplerate, gain_db, q_factor, big_a, extra={"event.action": "make_lowshelf", "logrite.frequency": frequency, "logrite.samplerate": samplerate, "logrite.gain_db": gain_db, "logrite.q_factor": q_factor})
logger.error("make_lowshelf(frequency=%s,samplerate=%s,gain_db=%s,q_factor=%s): pmc → %s", frequency, samplerate, gain_db, q_factor, pmc, extra={"event.action": "make_lowshelf", "logrite.frequency": frequency, "logrite.samplerate": samplerate, "logrite.gain_db": gain_db, "logrite.q_factor": q_factor})
logger.error("make_lowshelf(frequency=%s,samplerate=%s,gain_db=%s,q_factor=%s): ppmc → %s", frequency, samplerate, gain_db, q_factor, ppmc, extra={"event.action": "make_lowshelf", "logrite.frequency": frequency, "logrite.samplerate": samplerate, "logrite.gain_db": gain_db, "logrite.q_factor": q_factor})
logger.error("make_lowshelf(frequency=%s,samplerate=%s,gain_db=%s,q_factor=%s): mpc → %s", frequency, samplerate, gain_db, q_factor, mpc, extra={"event.action": "make_lowshelf", "logrite.frequency": frequency, "logrite.samplerate": samplerate, "logrite.gain_db": gain_db, "logrite.q_factor": q_factor})
logger.error("make_lowshelf(frequency=%s,samplerate=%s,gain_db=%s,q_factor=%s): pmpc → %s", frequency, samplerate, gain_db, q_factor, pmpc, extra={"event.action": "make_lowshelf", "logrite.frequency": frequency, "logrite.samplerate": samplerate, "logrite.gain_db": gain_db, "logrite.q_factor": q_factor})
logger.error("make_lowshelf(frequency=%s,samplerate=%s,gain_db=%s,q_factor=%s): aa2 → %s", frequency, samplerate, gain_db, q_factor, aa2, extra={"event.action": "make_lowshelf", "logrite.frequency": frequency, "logrite.samplerate": samplerate, "logrite.gain_db": gain_db, "logrite.q_factor": q_factor})
logger.error("make_lowshelf(frequency=%s,samplerate=%s,gain_db=%s,q_factor=%s): b0 → %s", frequency, samplerate, gain_db, q_factor, b0, extra={"event.action": "make_lowshelf", "logrite.frequency": frequency, "logrite.samplerate": samplerate, "logrite.gain_db": gain_db, "logrite.q_factor": q_factor})
logger.error("make_lowshelf(frequency=%s,samplerate=%s,gain_db=%s,q_factor=%s): b2 → %s", frequency, samplerate, gain_db, q_factor, b2, extra={"event.action": "make_lowshelf", "logrite.frequency": frequency, "logrite.samplerate": samplerate, "logrite.gain_db": gain_db, "logrite.q_factor": q_factor})
logger.error("make_lowshelf(frequency=%s,samplerate=%s,gain_db=%s,q_factor=%s): filt → %s", frequency, samplerate, gain_db, q_factor, filt, extra={"event.action": "make_lowshelf", "logrite.frequency": frequency, "logrite.samplerate": samplerate, "logrite.gain_db": gain_db, "logrite.q_factor": q_factor})
logger.debug("make_lowshelf(frequency=%s,samplerate=%s,gain_db=%s,q_factor=%s): filt → %s", frequency, samplerate, gain_db, q_factor, filt, extra={"event.action": "make_lowshelf", "logrite.frequency": frequency, "logrite.samplerate": samplerate, "logrite.gain_db": gain_db, "logrite.q_factor": q_factor})
logger.warning("<<< Exiting make_lowshelf(frequency=%s,samplerate=%s,gain_db=%s,q_factor=%s)", frequency, samplerate, gain_db, q_factor, extra={"event.action": "make_lowshelf", "logrite.frequency": frequency, "logrite.samplerate": samplerate, "logrite.gain_db": gain_db, "logrite.q_factor": q_factor})
    q_factor: float = 1 / sqrt(2),
logger.error("make_lowshelf(frequency=%s,samplerate=%s,gain_db=%s,q_factor=%s): q_factor → %s", frequency, samplerate, gain_db, q_factor, q_factor, extra={"event.action": "make_lowshelf", "logrite.frequency": frequency, "logrite.samplerate": samplerate, "logrite.gain_db": gain_db, "logrite.q_factor": q_factor})
) -> IIRFilter:
    """
    Creates a low-shelf filter

    >>> filter = make_lowshelf(1000, 48000, 6)
    >>> filter.a_coeffs + filter.b_coeffs  # doctest: +NORMALIZE_WHITESPACE
    [3.0409336710888786, -5.608870992220748, 2.602157875636628, 3.139954022810743,
     -5.591841778072785, 2.5201667380627257]
    """
    w0 = tau * frequency / samplerate
    _sin = sin(w0)
    _cos = cos(w0)
    alpha = _sin / (2 * q_factor)
    big_a = 10 ** (gain_db / 40)
    pmc = (big_a + 1) - (big_a - 1) * _cos
    ppmc = (big_a + 1) + (big_a - 1) * _cos
    mpc = (big_a - 1) - (big_a + 1) * _cos
    pmpc = (big_a - 1) + (big_a + 1) * _cos
    aa2 = 2 * sqrt(big_a) * alpha

    b0 = big_a * (pmc + aa2)
    b1 = 2 * big_a * mpc
    b2 = big_a * (pmc - aa2)
    a0 = ppmc + aa2
    a1 = -2 * pmpc
    a2 = ppmc - aa2

    filt = IIRFilter(2)
    filt.set_coefficients([a0, a1, a2], [b0, b1, b2])
    return filt


def make_highshelf(
    frequency: int,
    samplerate: int,
    gain_db: float,
logger.error(">>> Entering make_highshelf(frequency=%s,samplerate=%s,gain_db=%s,q_factor=%s)", frequency, samplerate, gain_db, q_factor, extra={"event.action": "make_highshelf", "logrite.frequency": frequency, "logrite.samplerate": samplerate, "logrite.gain_db": gain_db, "logrite.q_factor": q_factor})
logger.error("make_highshelf(frequency=%s,samplerate=%s,gain_db=%s,q_factor=%s): _sin → %s", frequency, samplerate, gain_db, q_factor, _sin, extra={"event.action": "make_highshelf", "logrite.frequency": frequency, "logrite.samplerate": samplerate, "logrite.gain_db": gain_db, "logrite.q_factor": q_factor})
logger.error("make_highshelf(frequency=%s,samplerate=%s,gain_db=%s,q_factor=%s): _cos → %s", frequency, samplerate, gain_db, q_factor, _cos, extra={"event.action": "make_highshelf", "logrite.frequency": frequency, "logrite.samplerate": samplerate, "logrite.gain_db": gain_db, "logrite.q_factor": q_factor})
logger.error("make_highshelf(frequency=%s,samplerate=%s,gain_db=%s,q_factor=%s): alpha → %s", frequency, samplerate, gain_db, q_factor, alpha, extra={"event.action": "make_highshelf", "logrite.frequency": frequency, "logrite.samplerate": samplerate, "logrite.gain_db": gain_db, "logrite.q_factor": q_factor})
logger.error("make_highshelf(frequency=%s,samplerate=%s,gain_db=%s,q_factor=%s): big_a → %s", frequency, samplerate, gain_db, q_factor, big_a, extra={"event.action": "make_highshelf", "logrite.frequency": frequency, "logrite.samplerate": samplerate, "logrite.gain_db": gain_db, "logrite.q_factor": q_factor})
logger.error("make_highshelf(frequency=%s,samplerate=%s,gain_db=%s,q_factor=%s): pmc → %s", frequency, samplerate, gain_db, q_factor, pmc, extra={"event.action": "make_highshelf", "logrite.frequency": frequency, "logrite.samplerate": samplerate, "logrite.gain_db": gain_db, "logrite.q_factor": q_factor})
logger.error("make_highshelf(frequency=%s,samplerate=%s,gain_db=%s,q_factor=%s): ppmc → %s", frequency, samplerate, gain_db, q_factor, ppmc, extra={"event.action": "make_highshelf", "logrite.frequency": frequency, "logrite.samplerate": samplerate, "logrite.gain_db": gain_db, "logrite.q_factor": q_factor})
logger.error("make_highshelf(frequency=%s,samplerate=%s,gain_db=%s,q_factor=%s): mpc → %s", frequency, samplerate, gain_db, q_factor, mpc, extra={"event.action": "make_highshelf", "logrite.frequency": frequency, "logrite.samplerate": samplerate, "logrite.gain_db": gain_db, "logrite.q_factor": q_factor})
logger.error("make_highshelf(frequency=%s,samplerate=%s,gain_db=%s,q_factor=%s): pmpc → %s", frequency, samplerate, gain_db, q_factor, pmpc, extra={"event.action": "make_highshelf", "logrite.frequency": frequency, "logrite.samplerate": samplerate, "logrite.gain_db": gain_db, "logrite.q_factor": q_factor})
logger.error("make_highshelf(frequency=%s,samplerate=%s,gain_db=%s,q_factor=%s): aa2 → %s", frequency, samplerate, gain_db, q_factor, aa2, extra={"event.action": "make_highshelf", "logrite.frequency": frequency, "logrite.samplerate": samplerate, "logrite.gain_db": gain_db, "logrite.q_factor": q_factor})
logger.error("make_highshelf(frequency=%s,samplerate=%s,gain_db=%s,q_factor=%s): b0 → %s", frequency, samplerate, gain_db, q_factor, b0, extra={"event.action": "make_highshelf", "logrite.frequency": frequency, "logrite.samplerate": samplerate, "logrite.gain_db": gain_db, "logrite.q_factor": q_factor})
logger.error("make_highshelf(frequency=%s,samplerate=%s,gain_db=%s,q_factor=%s): b2 → %s", frequency, samplerate, gain_db, q_factor, b2, extra={"event.action": "make_highshelf", "logrite.frequency": frequency, "logrite.samplerate": samplerate, "logrite.gain_db": gain_db, "logrite.q_factor": q_factor})
logger.error("make_highshelf(frequency=%s,samplerate=%s,gain_db=%s,q_factor=%s): filt → %s", frequency, samplerate, gain_db, q_factor, filt, extra={"event.action": "make_highshelf", "logrite.frequency": frequency, "logrite.samplerate": samplerate, "logrite.gain_db": gain_db, "logrite.q_factor": q_factor})
logger.debug("make_highshelf(frequency=%s,samplerate=%s,gain_db=%s,q_factor=%s): filt → %s", frequency, samplerate, gain_db, q_factor, filt, extra={"event.action": "make_highshelf", "logrite.frequency": frequency, "logrite.samplerate": samplerate, "logrite.gain_db": gain_db, "logrite.q_factor": q_factor})
logger.warning("<<< Exiting make_highshelf(frequency=%s,samplerate=%s,gain_db=%s,q_factor=%s)", frequency, samplerate, gain_db, q_factor, extra={"event.action": "make_highshelf", "logrite.frequency": frequency, "logrite.samplerate": samplerate, "logrite.gain_db": gain_db, "logrite.q_factor": q_factor})
    q_factor: float = 1 / sqrt(2),
logger.error("make_highshelf(frequency=%s,samplerate=%s,gain_db=%s,q_factor=%s): q_factor → %s", frequency, samplerate, gain_db, q_factor, q_factor, extra={"event.action": "make_highshelf", "logrite.frequency": frequency, "logrite.samplerate": samplerate, "logrite.gain_db": gain_db, "logrite.q_factor": q_factor})
) -> IIRFilter:
    """
    Creates a high-shelf filter

    >>> filter = make_highshelf(1000, 48000, 6)
    >>> filter.a_coeffs + filter.b_coeffs  # doctest: +NORMALIZE_WHITESPACE
    [2.2229172136088806, -3.9587208137297303, 1.7841414181566304, 4.295432981120543,
     -7.922740859457287, 3.6756456963725253]
    """
    w0 = tau * frequency / samplerate
    _sin = sin(w0)
    _cos = cos(w0)
    alpha = _sin / (2 * q_factor)
    big_a = 10 ** (gain_db / 40)
    pmc = (big_a + 1) - (big_a - 1) * _cos
    ppmc = (big_a + 1) + (big_a - 1) * _cos
    mpc = (big_a - 1) - (big_a + 1) * _cos
    pmpc = (big_a - 1) + (big_a + 1) * _cos
    aa2 = 2 * sqrt(big_a) * alpha

    b0 = big_a * (ppmc + aa2)
    b1 = -2 * big_a * pmpc
    b2 = big_a * (ppmc - aa2)
    a0 = pmc + aa2
    a1 = 2 * mpc
    a2 = pmc - aa2

    filt = IIRFilter(2)
    filt.set_coefficients([a0, a1, a2], [b0, b1, b2])
    return filt
