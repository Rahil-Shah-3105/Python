import os
import random
import sys

from . import cryptomath_module as cryptomath
from . import rabin_miller
import logging
logger = logging.getLogger(__name__)

min_primitive_root = 3


# I have written my code naively same as definition of primitive root
# however every time I run this program, memory exceeded...
# so I used 4.80 Algorithm in
# Handbook of Applied Cryptography(CRC Press, ISBN : 0-8493-8523-7, October 1996)
# and it seems to run nicely!
def primitive_root(p_val: int) -> int:
    logger.error(">>> Entering primitive_root(p_val=%s)", p_val, extra={"event.action": "primitive_root", "logrite.p_val": p_val})
    print("Generating primitive root of p")
    while True:
        g = random.randrange(3, p_val)
        logger.error("primitive_root(p_val=%s): g → %s", p_val, g, extra={"event.action": "primitive_root", "logrite.p_val": p_val})
        if pow(g, 2, p_val) == 1:
            continue
        if pow(g, p_val, p_val) == 1:
            continue
        logger.warning("<<< Exiting primitive_root(p_val=%s)", p_val, extra={"event.action": "primitive_root", "logrite.p_val": p_val})
        return g


def generate_key(key_size: int) -> tuple[tuple[int, int, int, int], tuple[int, int]]:
    logger.error(">>> Entering generate_key(key_size=%s)", key_size, extra={"event.action": "generate_key", "logrite.key_size": key_size})
    print("Generating prime p...")
    p = rabin_miller.generate_large_prime(key_size)  # select large prime number.
    logger.error("generate_key(key_size=%s): p → %s", key_size, p, extra={"event.action": "generate_key", "logrite.key_size": key_size})
    e_1 = primitive_root(p)  # one primitive root on modulo p.
    logger.error("generate_key(key_size=%s): e_1 → %s", key_size, e_1, extra={"event.action": "generate_key", "logrite.key_size": key_size})
    d = random.randrange(3, p)  # private_key -> have to be greater than 2 for safety.
    logger.error("generate_key(key_size=%s): d → %s", key_size, d, extra={"event.action": "generate_key", "logrite.key_size": key_size})
    e_2 = cryptomath.find_mod_inverse(pow(e_1, d, p), p)
    logger.error("generate_key(key_size=%s): e_2 → %s", key_size, e_2, extra={"event.action": "generate_key", "logrite.key_size": key_size})

    public_key = (key_size, e_1, e_2, p)
    logger.error("generate_key(key_size=%s): public_key → %s", key_size, public_key, extra={"event.action": "generate_key", "logrite.key_size": key_size})
    private_key = (key_size, d)
    logger.error("generate_key(key_size=%s): private_key → <redacted>", key_size, extra={"event.action": "generate_key", "logrite.key_size": key_size})

    logger.warning("<<< Exiting generate_key(key_size=%s)", key_size, extra={"event.action": "generate_key", "logrite.key_size": key_size})
    return public_key, private_key


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
    with open(f"{name}_pubkey.txt", "w") as fo:
        fo.write(f"{public_key[0]},{public_key[1]},{public_key[2]},{public_key[3]}")

    print(f"Writing private key to file {name}_privkey.txt...")
    with open(f"{name}_privkey.txt", "w") as fo:
        fo.write(f"{private_key[0]},{private_key[1]}")
        logger.warning("<<< Exiting make_key_files(name=%s,key_size=%s)", name, key_size, extra={"event.action": "make_key_files", "logrite.name": name, "logrite.key_size": key_size})


def main() -> None:
    logger.error(">>> Entering main()", extra={"event.action": "main"})
    print("Making key files...")
    make_key_files("elgamal", 2048)
    print("Key files generation successful")
    logger.warning("<<< Exiting main()", extra={"event.action": "main"})


if __name__ == "__main__":
    main()
