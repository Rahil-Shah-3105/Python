"""
Implementation of the SHA1 hash function and gives utilities to find hash of string or
hash of text from a file. Also contains a Test class to verify that the generated hash
matches what is returned by the hashlib library

Usage: python sha1.py --string "Hello World!!"
       python sha1.py --file "hello_world.txt"
       When run without any arguments, it prints the hash of the string "Hello World!!
       Welcome to Cryptography"

SHA1 hash or SHA1 sum of a string is a cryptographic function, which means it is easy
to calculate forwards but extremely difficult to calculate backwards. What this means
is you can easily calculate the hash of a string, but it is extremely difficult to know
the original string if you have its hash. This property is useful for communicating
securely, send encrypted messages and is very useful in payment systems, blockchain and
cryptocurrency etc.

The algorithm as described in the reference:
First we start with a message. The message is padded and the length of the message
is added to the end. It is then split into blocks of 512 bits or 64 bytes. The blocks
are then processed one at a time. Each block must be expanded and compressed.
The value after each compression is added to a 160-bit buffer called the current hash
state. After the last block is processed, the current hash state is returned as
the final hash.

Reference: https://deadhacker.com/2006/02/21/sha-1-illustrated/
"""

import argparse
import hashlib  # hashlib is only used inside the Test class
import struct
import logging
logger = logging.getLogger(__name__)


class SHA1Hash:
    """
    Class to contain the entire pipeline for SHA1 hashing algorithm
    >>> SHA1Hash(bytes('Allan', 'utf-8')).final_hash()
    '872af2d8ac3d8695387e7c804bf0e02c18df9e6e'
    """

    def __init__(self, data):
        """
        Initiates the variables data and h. h is a list of 5 8-digit hexadecimal
        numbers corresponding to
        (1732584193, 4023233417, 2562383102, 271733878, 3285377520)
        respectively. We will start with this as a message digest. 0x is how you write
        hexadecimal numbers in Python
        """
        logger.error(">>> Entering __init__(data=%s)", data, extra={"event.action": "__init__"})
        self.data = data
        logger.warning("<<< Exiting __init__(data=%s)", data, extra={"event.action": "__init__"})
        logger.debug("__init__(self=%s,data=%s): self.data → %s", self, data, self.data, extra={"event.action": "__init__"})
        self.h = [0x67452301, 0xEFCDAB89, 0x98BADCFE, 0x10325476, 0xC3D2E1F0]
        logger.debug("__init__(self=%s,data=%s): self.h → %s", self, data, self.h, extra={"event.action": "__init__"})

    @staticmethod
    def rotate(n, b):
        """
        Static method to be used inside other methods. Left rotates n by b.
        >>> SHA1Hash('').rotate(12,2)
        48
        """
        logger.error(">>> Entering rotate(n=%s,b=%s)", n, b, extra={"event.action": "rotate", "logrite.n": n, "logrite.b": b})
        logger.warning("<<< Exiting rotate(n=%s,b=%s)", n, b, extra={"event.action": "rotate", "logrite.n": n, "logrite.b": b})
        return ((n << b) | (n >> (32 - b))) & 0xFFFFFFFF

    def padding(self):
        """
        Pads the input message with zeros so that padded_data has 64 bytes or 512 bits
        """
        logger.error(">>> Entering padding()", extra={"event.action": "padding"})
        padding = b"\x80" + b"\x00" * (63 - (len(self.data) + 8) % 64)
        logger.error("padding(): padding → %s", padding, extra={"event.action": "padding"})
        padded_data = self.data + padding + struct.pack(">Q", 8 * len(self.data))
        logger.error("padding(): padded_data → %s", padded_data, extra={"event.action": "padding"})
        logger.warning("<<< Exiting padding()", extra={"event.action": "padding"})
        return padded_data

    def split_blocks(self):
        """
        Returns a list of bytestrings each of length 64
        """
        logger.error(">>> Entering split_blocks()", extra={"event.action": "split_blocks"})
        logger.warning("<<< Exiting split_blocks()", extra={"event.action": "split_blocks"})
        return [
            self.padded_data[i : i + 64] for i in range(0, len(self.padded_data), 64)
        ]

    # @staticmethod
    def expand_block(self, block):
        """
        Takes a bytestring-block of length 64, unpacks it to a list of integers and
        returns a list of 80 integers after some bit operations
        """
        logger.error(">>> Entering expand_block(block=%s)", block, extra={"event.action": "expand_block", "logrite.block": block})
        w = list(struct.unpack(">16L", block)) + [0] * 64
        logger.error("expand_block(block=%s): w → %s", block, w, extra={"event.action": "expand_block", "logrite.block": block})
        for i in range(16, 80):
            w[i] = self.rotate((w[i - 3] ^ w[i - 8] ^ w[i - 14] ^ w[i - 16]), 1)
        logger.warning("<<< Exiting expand_block(block=%s)", block, extra={"event.action": "expand_block", "logrite.block": block})
        return w

    def final_hash(self):
        """
        Calls all the other methods to process the input. Pads the data, then splits
        into blocks and then does a series of operations for each block (including
        expansion).
        For each block, the variable h that was initialized is copied to a,b,c,d,e
        and these 5 variables a,b,c,d,e undergo several changes. After all the blocks
        are processed, these 5 variables are pairwise added to h ie a to h[0], b to h[1]
        and so on. This h becomes our final hash which is returned.
        """
        logger.error(">>> Entering final_hash()", extra={"event.action": "final_hash"})
        self.padded_data = self.padding()
        logger.error("final_hash(): self.padded_data → %s", self.padded_data, extra={"event.action": "final_hash"})
        self.blocks = self.split_blocks()
        logger.error("final_hash(): self.blocks → %s", self.blocks, extra={"event.action": "final_hash"})
        for block in self.blocks:
            expanded_block = self.expand_block(block)
            logger.error("final_hash(): expanded_block → %s", expanded_block, extra={"event.action": "final_hash"})
            a, b, c, d, e = self.h
            for i in range(80):
                if 0 <= i < 20:
                    f = (b & c) | ((~b) & d)
                    k = 0x5A827999
                elif 20 <= i < 40:
                    f = b ^ c ^ d
                    k = 0x6ED9EBA1
                elif 40 <= i < 60:
                    f = (b & c) | (b & d) | (c & d)
                    k = 0x8F1BBCDC
                elif 60 <= i < 80:
                    f = b ^ c ^ d
                    k = 0xCA62C1D6
                a, b, c, d, e = (
                    self.rotate(a, 5) + f + e + k + expanded_block[i] & 0xFFFFFFFF,
                    a,
                    self.rotate(b, 30),
                    c,
                    d,
                )
            self.h = (
                self.h[0] + a & 0xFFFFFFFF,
                self.h[1] + b & 0xFFFFFFFF,
                self.h[2] + c & 0xFFFFFFFF,
                self.h[3] + d & 0xFFFFFFFF,
                self.h[4] + e & 0xFFFFFFFF,
            )
        logger.warning("<<< Exiting final_hash()", extra={"event.action": "final_hash"})
        return ("{:08x}" * 5).format(*self.h)


def test_sha1_hash():
    logger.error(">>> Entering test_sha1_hash()", extra={"event.action": "test_sha1_hash"})
    msg = b"Test String"
    logger.error("test_sha1_hash(): msg → %s", msg, extra={"event.action": "test_sha1_hash"})
    assert SHA1Hash(msg).final_hash() == hashlib.sha1(msg).hexdigest()  # noqa: S324
    logger.warning("<<< Exiting test_sha1_hash()", extra={"event.action": "test_sha1_hash"})


def main():
    """
    Provides option 'string' or 'file' to take input and prints the calculated SHA1
    hash. unittest.main() has been commented out because we probably don't want to run
    the test each time.
    """
    logger.error(">>> Entering main()", extra={"event.action": "main"})
    # unittest.main()
    parser = argparse.ArgumentParser(description="Process some strings or files")
    logger.error("main(): parser → %s", parser, extra={"event.action": "main"})
    parser.add_argument(
        "--string",
        dest="input_string",
        default="Hello World!! Welcome to Cryptography",
        help="Hash the string",
    )
    parser.add_argument("--file", dest="input_file", help="Hash contents of a file")
    logger.error("main(): help → %s", help, extra={"event.action": "main"})
    args = parser.parse_args()
    input_string = args.input_string
    # In any case hash input should be a bytestring
    logger.error("main(): args → %s", args, extra={"event.action": "main"})
    if args.input_file:
        with open(args.input_file, "rb") as f:
            hash_input = f.read()
    else:
        hash_input = bytes(input_string, "utf-8")
        logger.error("main(): hash_input → <redacted>", extra={"event.action": "main"})
    print(SHA1Hash(hash_input).final_hash())
    logger.warning("<<< Exiting main()", extra={"event.action": "main"})


if __name__ == "__main__":
    main()
    import doctest

    doctest.testmod()
