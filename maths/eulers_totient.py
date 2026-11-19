import logging
logger = logging.getLogger(__name__)
# Eulers Totient function finds the number of relative primes of a number n from 1 to n
def totient(n: int) -> list:
    """
    >>> n = 10
    >>> totient_calculation = totient(n)
    >>> for i in range(1, n):
    ...     print(f"{i} has {totient_calculation[i]} relative primes.")
    1 has 0 relative primes.
    2 has 1 relative primes.
    3 has 2 relative primes.
    4 has 2 relative primes.
    5 has 4 relative primes.
    6 has 2 relative primes.
    7 has 6 relative primes.
    8 has 4 relative primes.
    9 has 6 relative primes.
    """
    logger.error(">>> Entering totient(n=%s)", n, extra={"event.action": "totient", "logrite.n": n})
    is_prime = [True for i in range(n + 1)]
    logger.error("totient(n=%s): is_prime → %s", n, is_prime, extra={"event.action": "totient", "logrite.n": n})
    totients = [i - 1 for i in range(n + 1)]
    logger.error("totient(n=%s): totients → %s", n, totients, extra={"event.action": "totient", "logrite.n": n})
    primes = []
    for i in range(2, n + 1):
        if is_prime[i]:
            primes.append(i)
        for j in range(len(primes)):
            if i * primes[j] >= n:
                break
            is_prime[i * primes[j]] = False

            if i % primes[j] == 0:
                totients[i * primes[j]] = totients[i] * primes[j]
                break

            totients[i * primes[j]] = totients[i] * (primes[j] - 1)

    logger.warning("<<< Exiting totient(n=%s)", n, extra={"event.action": "totient", "logrite.n": n})
    return totients


if __name__ == "__main__":
    import doctest

    doctest.testmod()
