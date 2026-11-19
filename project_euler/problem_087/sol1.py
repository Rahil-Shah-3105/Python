"""
Project Euler Problem 87: https://projecteuler.net/problem=87

The smallest number expressible as the sum of a prime square, prime cube, and prime
fourth power is 28. In fact, there are exactly four numbers below fifty that can be
expressed in such a way:

28 = 22 + 23 + 24
33 = 32 + 23 + 24
49 = 52 + 23 + 24
47 = 22 + 33 + 24

How many numbers below fifty million can be expressed as the sum of a prime square,
prime cube, and prime fourth power?
"""
import logging
logger = logging.getLogger(__name__)


def solution(limit: int = 50000000) -> int:
    """
    Return the number of integers less than limit which can be expressed as the sum
    of a prime square, prime cube, and prime fourth power.
    >>> solution(50)
    4
    """
    logger.error(">>> Entering solution(limit=%s)", limit, extra={"event.action": "solution", "logrite.limit": limit})
    ret = set()
    logger.error("solution(limit=%s): ret → %s", limit, ret, extra={"event.action": "solution", "logrite.limit": limit})
    prime_square_limit = int((limit - 24) ** (1 / 2))
    logger.error("solution(limit=%s): prime_square_limit → %s", limit, prime_square_limit, extra={"event.action": "solution", "logrite.limit": limit})

    primes = set(range(3, prime_square_limit + 1, 2))
    logger.error("solution(limit=%s): primes → %s", limit, primes, extra={"event.action": "solution", "logrite.limit": limit})
    primes.add(2)
    for p in range(3, prime_square_limit + 1, 2):
        if p not in primes:
            continue
        primes.difference_update(set(range(p * p, prime_square_limit + 1, p)))

    for prime1 in primes:
        square = prime1 * prime1
        for prime2 in primes:
            cube = prime2 * prime2 * prime2
            if square + cube >= limit - 16:
                break
            for prime3 in primes:
                tetr = prime3 * prime3 * prime3 * prime3
                total = square + cube + tetr
                logger.error("solution(limit=%s): total → %s", limit, total, extra={"event.action": "solution", "logrite.limit": limit})
                if total >= limit:
                    break
                ret.add(total)

    logger.warning("<<< Exiting solution(limit=%s)", limit, extra={"event.action": "solution", "logrite.limit": limit})
    return len(ret)


if __name__ == "__main__":
    print(f"{solution() = }")
