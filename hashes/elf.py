import logging
logger = logging.getLogger(__name__)
def elf_hash(data: str) -> int:
    """
    Implementation of ElfHash Algorithm, a variant of PJW hash function.

    >>> elf_hash('lorem ipsum')
    253956621
    """
    logger.debug(">>> Entering elf_hash(data=%s)", data)
    hash_ = x = 0
    logger.debug("elf_hash(data=%s): hash_ → %s", data, hash_)
    for letter in data:
        hash_ = (hash_ << 4) + ord(letter)
        x = hash_ & 0xF0000000
        if x != 0:
            hash_ ^= x >> 24
        hash_ &= ~x
    logger.debug("<<< Exiting elf_hash(data=%s)", data)
    return hash_


if __name__ == "__main__":
    import doctest

    doctest.testmod()
