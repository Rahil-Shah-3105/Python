from maths.greatest_common_divisor import gcd_by_iterative
import logging
logger = logging.getLogger(__name__)


def find_mod_inverse(a: int, m: int) -> int:
    logger.error(">>> Entering find_mod_inverse(a=%s,m=%s)", a, m, extra={"event.action": "find_mod_inverse", "logrite.a": a, "logrite.m": m})
    if gcd_by_iterative(a, m) != 1:
        msg = f"mod inverse of {a!r} and {m!r} does not exist"
        logger.error("find_mod_inverse(a=%s,m=%s): msg → %s", a, m, msg, extra={"event.action": "find_mod_inverse", "logrite.a": a, "logrite.m": m})
        raise ValueError(msg)
    u1, u2, u3 = 1, 0, a
    v1, v2, v3 = 0, 1, m
    while v3 != 0:
        q = u3 // v3
        v1, v2, v3, u1, u2, u3 = (u1 - q * v1), (u2 - q * v2), (u3 - q * v3), v1, v2, v3
    logger.warning("<<< Exiting find_mod_inverse(a=%s,m=%s)", a, m, extra={"event.action": "find_mod_inverse", "logrite.a": a, "logrite.m": m})
    return u1 % m
