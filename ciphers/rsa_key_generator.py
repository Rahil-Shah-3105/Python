import os
import random
import sys

from maths.greatest_common_divisor import gcd_by_iterative

from . import cryptomath_module, rabin_miller
import logging
logger = logging.getLogger(__name__)


def main() -> None:
    logger.error(">>> Entering main()", extra={"event.action": "main"})
    print("Making key files...")
    make_key_files("rsa", 1024)
    print("Key files generation successful.")
    logger.warning("<<< Exiting main()", extra={"event.action": "main"})


def generate_key(key_size: int) -> tuple[tuple[int, int], tuple[int, int]]:
    """
    >>> random.seed(0) # for repeatability
    >>> public_key, private_key = generate_key(8)
    >>> public_key
    (26569, 239)
    >>> private_key
    (26569, 2855)
    """
    logger.error(">>> Entering generate_key(key_size=%s)", key_size, extra={"event.action": "generate_key", "logrite.key_size": key_size})
    p = rabin_miller.generate_large_prime(key_size)
    logger.error("generate_key(key_size=%s): p → %s", key_size, p, extra={"event.action": "generate_key", "logrite.key_size": key_size})
    q = rabin_miller.generate_large_prime(key_size)
    logger.error("generate_key(key_size=%s): q → %s", key_size, q, extra={"event.action": "generate_key", "logrite.key_size": key_size})
    n = p * q

    # Generate e that is relatively prime to (p - 1) * (q - 1)
    while True:
        e = random.randrange(2 ** (key_size - 1), 2 ** (key_size))
        logger.error("generate_key(key_size=%s): e → %s", key_size, e, extra={"event.action": "generate_key", "logrite.key_size": key_size})
        if gcd_by_iterative(e, (p - 1) * (q - 1)) == 1:
            break

    # Calculate d that is mod inverse of e
    d = cryptomath_module.find_mod_inverse(e, (p - 1) * (q - 1))
    logger.error("generate_key(key_size=%s): d → %s", key_size, d, extra={"event.action": "generate_key", "logrite.key_size": key_size})

    public_key = (n, e)
    logger.error("generate_key(key_size=%s): public_key → %s", key_size, public_key, extra={"event.action": "generate_key", "logrite.key_size": key_size})
    private_key = (n, d)
    logger.error("generate_key(key_size=%s): private_key → <redacted>", key_size, extra={"event.action": "generate_key", "logrite.key_size": key_size})
    logger.warning("<<< Exiting generate_key(key_size=%s)", key_size, extra={"event.action": "generate_key", "logrite.key_size": key_size})
    return (public_key, private_key)


def make_key_files(name: str, key_size: int) -> None:
    logger.error(">>> Entering make_key_files(name=%s,key_size=%s)", name, key_size, extra={"event.action": "make_key_files", "logrite.name": name, "logrite.key_size": key_size})
    if os.path.exists(f"{name}_pubkey.txt") or os.path.exists(f"{name}_privkey.txt"):
        print("\nWARNING:")
        print(
            f'"{name}_pubkey.txt" or "{name}_privkey.txt" already exists. \n'
            "Use a different name or delete these files and re-run this program."
        )
        sys.exit()

    public_key, private_key = generate_key(key_size)
    print(f"\nWriting public key to file {name}_pubkey.txt...")
    with open(f"{name}_pubkey.txt", "w") as out_file:
        out_file.write(f"{key_size},{public_key[0]},{public_key[1]}")

    print(f"Writing private key to file {name}_privkey.txt...")
    with open(f"{name}_privkey.txt", "w") as out_file:
        out_file.write(f"{key_size},{private_key[0]},{private_key[1]}")
        logger.warning("<<< Exiting make_key_files(name=%s,key_size=%s)", name, key_size, extra={"event.action": "make_key_files", "logrite.name": name, "logrite.key_size": key_size})


if __name__ == "__main__":
    main()
