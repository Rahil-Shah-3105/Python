# Primality Testing with the Rabin-Miller Algorithm

import random
import logging
logger = logging.getLogger(__name__)


def rabin_miller(num: int) -> bool:
    logger.error(">>> Entering rabin_miller(num=%s)", num, extra={"event.action": "rabin_miller", "logrite.num": num})
    s = num - 1
    t = 0

    while s % 2 == 0:
        s = s // 2
        t += 1

    for _ in range(5):
        a = random.randrange(2, num - 1)
        logger.error("rabin_miller(num=%s): a → %s", num, a, extra={"event.action": "rabin_miller", "logrite.num": num})
        v = pow(a, s, num)
        logger.error("rabin_miller(num=%s): v → %s", num, v, extra={"event.action": "rabin_miller", "logrite.num": num})
        if v != 1:
            i = 0
            while v != (num - 1):
                if i == t - 1:
                    return False
                else:
                    i = i + 1
                    v = (v**2) % num
    logger.warning("<<< Exiting rabin_miller(num=%s)", num, extra={"event.action": "rabin_miller", "logrite.num": num})
    return True


def is_prime_low_num(num: int) -> bool:
    logger.error(">>> Entering is_prime_low_num(num=%s)", num, extra={"event.action": "is_prime_low_num", "logrite.num": num})
    if num < 2:
        return False

    low_primes = [
        2,
        3,
        5,
        7,
        11,
        13,
        17,
        19,
        23,
        29,
        31,
        37,
        41,
        43,
        47,
        53,
        59,
        61,
        67,
        71,
        73,
        79,
        83,
        89,
        97,
        101,
        103,
        107,
        109,
        113,
        127,
        131,
        137,
        139,
        149,
        151,
        157,
        163,
        167,
        173,
        179,
        181,
        191,
        193,
        197,
        199,
        211,
        223,
        227,
        229,
        233,
        239,
        241,
        251,
        257,
        263,
        269,
        271,
        277,
        281,
        283,
        293,
        307,
        311,
        313,
        317,
        331,
        337,
        347,
        349,
        353,
        359,
        367,
        373,
        379,
        383,
        389,
        397,
        401,
        409,
        419,
        421,
        431,
        433,
        439,
        443,
        449,
        457,
        461,
        463,
        467,
        479,
        487,
        491,
        499,
        503,
        509,
        521,
        523,
        541,
        547,
        557,
        563,
        569,
        571,
        577,
        587,
        593,
        599,
        601,
        607,
        613,
        617,
        619,
        631,
        641,
        643,
        647,
        653,
        659,
        661,
        673,
        677,
        683,
        691,
        701,
        709,
        719,
        727,
        733,
        739,
        743,
        751,
        757,
        761,
        769,
        773,
        787,
        797,
        809,
        811,
        821,
        823,
        827,
        829,
        839,
        853,
        857,
        859,
        863,
        877,
        881,
        883,
        887,
        907,
        911,
        919,
        929,
        937,
        941,
        947,
        953,
        967,
        971,
        977,
        983,
        991,
        997,
    ]

    if num in low_primes:
        return True

    for prime in low_primes:
        if (num % prime) == 0:
            return False

    logger.warning("<<< Exiting is_prime_low_num(num=%s)", num, extra={"event.action": "is_prime_low_num", "logrite.num": num})
    return rabin_miller(num)


def generate_large_prime(keysize: int = 1024) -> int:
    logger.error(">>> Entering generate_large_prime(keysize=%s)", keysize, extra={"event.action": "generate_large_prime", "logrite.keysize": keysize})
    while True:
        num = random.randrange(2 ** (keysize - 1), 2 ** (keysize))
        logger.error("generate_large_prime(keysize=%s): num → %s", keysize, num, extra={"event.action": "generate_large_prime", "logrite.keysize": keysize})
        if is_prime_low_num(num):
            logger.warning("<<< Exiting generate_large_prime(keysize=%s)", keysize, extra={"event.action": "generate_large_prime", "logrite.keysize": keysize})
            return num


if __name__ == "__main__":
    num = generate_large_prime()
    print(("Prime number:", num))
    print(("is_prime_low_num:", is_prime_low_num(num)))
