"""
See https://en.wikipedia.org/wiki/Bloom_filter

The use of this data structure is to test membership in a set.
Compared to Python's built-in set() it is more space-efficient.
In the following example, only 8 bits of memory will be used:
>>> bloom = Bloom(size=8)

Initially, the filter contains all zeros:
>>> bloom.bitstring
'00000000'

When an element is added, two bits are set to 1
since there are 2 hash functions in this implementation:
>>> "Titanic" in bloom
False
>>> bloom.add("Titanic")
>>> bloom.bitstring
'01100000'
>>> "Titanic" in bloom
True

However, sometimes only one bit is added
because both hash functions return the same value
>>> bloom.add("Avatar")
>>> "Avatar" in bloom
True
>>> bloom.format_hash("Avatar")
'00000100'
>>> bloom.bitstring
'01100100'

Not added elements should return False ...
>>> not_present_films = ("The Godfather", "Interstellar", "Parasite", "Pulp Fiction")
>>> {
...   film: bloom.format_hash(film) for film in not_present_films
... } # doctest: +NORMALIZE_WHITESPACE
{'The Godfather': '00000101',
 'Interstellar': '00000011',
 'Parasite': '00010010',
 'Pulp Fiction': '10000100'}
>>> any(film in bloom for film in not_present_films)
False

but sometimes there are false positives:
>>> "Ratatouille" in bloom
True
>>> bloom.format_hash("Ratatouille")
'01100000'

The probability increases with the number of elements added.
The probability decreases with the number of bits in the bitarray.
>>> bloom.estimated_error_rate
0.140625
>>> bloom.add("The Godfather")
>>> bloom.estimated_error_rate
0.25
>>> bloom.bitstring
'01100101'
"""

from hashlib import md5, sha256
import logging
logger = logging.getLogger(__name__)

HASH_FUNCTIONS = (sha256, md5)


class Bloom:
    def __init__(self, size: int = 8) -> None:
        logger.error(">>> Entering __init__(size=%s)", size, extra={"event.action": "__init__", "logrite.size": size})
        self.bitarray = 0b0
        logger.debug("__init__(self=%s,size=%s): self.bitarray → %s", self, size, self.bitarray, extra={"event.action": "__init__", "logrite.size": size})
        self.size = size
        logger.warning("<<< Exiting __init__(size=%s)", size, extra={"event.action": "__init__", "logrite.size": size})
        logger.debug("__init__(self=%s,size=%s): self.size → %s", self, size, self.size, extra={"event.action": "__init__", "logrite.size": size})

    def add(self, value: str) -> None:
        logger.error(">>> Entering add(value=%s)", value, extra={"event.action": "add", "logrite.value": value})
        h = self.hash_(value)
        logger.error("add(value=%s): h → %s", value, h, extra={"event.action": "add", "logrite.value": value})
        self.bitarray |= h
        logger.warning("<<< Exiting add(value=%s)", value, extra={"event.action": "add", "logrite.value": value})

    def exists(self, value: str) -> bool:
        logger.error(">>> Entering exists(value=%s)", value, extra={"event.action": "exists", "logrite.value": value})
        h = self.hash_(value)
        logger.error("exists(value=%s): h → %s", value, h, extra={"event.action": "exists", "logrite.value": value})
        logger.warning("<<< Exiting exists(value=%s)", value, extra={"event.action": "exists", "logrite.value": value})
        return (h & self.bitarray) == h

    def __contains__(self, other: str) -> bool:
        logger.error(">>> Entering __contains__(other=%s)", other, extra={"event.action": "__contains__", "logrite.other": other})
        logger.warning("<<< Exiting __contains__(other=%s)", other, extra={"event.action": "__contains__", "logrite.other": other})
        return self.exists(other)

    def format_bin(self, bitarray: int) -> str:
        logger.error(">>> Entering format_bin(bitarray=%s)", bitarray, extra={"event.action": "format_bin", "logrite.bitarray": bitarray})
        res = bin(bitarray)[2:]
        logger.error("format_bin(bitarray=%s): res → %s", bitarray, res, extra={"event.action": "format_bin", "logrite.bitarray": bitarray})
        logger.warning("<<< Exiting format_bin(bitarray=%s)", bitarray, extra={"event.action": "format_bin", "logrite.bitarray": bitarray})
        return res.zfill(self.size)

    @property
    def bitstring(self) -> str:
        logger.error(">>> Entering bitstring()", extra={"event.action": "bitstring"})
        logger.warning("<<< Exiting bitstring()", extra={"event.action": "bitstring"})
        return self.format_bin(self.bitarray)

    def hash_(self, value: str) -> int:
        logger.error(">>> Entering hash_(value=<redacted>)", extra={"event.action": "hash_"})
        res = 0b0
        for func in HASH_FUNCTIONS:
            position = (
                int.from_bytes(func(value.encode()).digest(), "little") % self.size
            )
            res |= 2**position
        logger.warning("<<< Exiting hash_(value=<redacted>)", extra={"event.action": "hash_"})
        return res

    def format_hash(self, value: str) -> str:
        logger.error(">>> Entering format_hash(value=<redacted>)", extra={"event.action": "format_hash"})
        logger.warning("<<< Exiting format_hash(value=<redacted>)", extra={"event.action": "format_hash"})
        return self.format_bin(self.hash_(value))

    @property
    def estimated_error_rate(self) -> float:
        logger.error(">>> Entering estimated_error_rate()", extra={"event.action": "estimated_error_rate"})
        n_ones = bin(self.bitarray).count("1")
        logger.error("estimated_error_rate(): n_ones → %s", n_ones, extra={"event.action": "estimated_error_rate"})
        logger.warning("<<< Exiting estimated_error_rate()", extra={"event.action": "estimated_error_rate"})
        return (n_ones / self.size) ** len(HASH_FUNCTIONS)
