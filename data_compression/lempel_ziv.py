"""
One of the several implementations of Lempel-Ziv-Welch compression algorithm
https://en.wikipedia.org/wiki/Lempel%E2%80%93Ziv%E2%80%93Welch
"""

import math
import os
import sys
import logging
logger = logging.getLogger(__name__)


def read_file_binary(file_path: str) -> str:
    """
    Reads given file as bytes and returns them as a long string
    """
    logger.debug(">>> Entering read_file_binary(file_path=%s)", file_path)
    result = ""
    logger.debug("read_file_binary(file_path=%s): result → %s", file_path, result)
    try:
        with open(file_path, "rb") as binary_file:
            data = binary_file.read()
            logger.debug("read_file_binary(file_path=%s): data → %s", file_path, data)
        for dat in data:
            curr_byte = f"{dat:08b}"
            logger.debug("read_file_binary(file_path=%s): curr_byte → %s", file_path, curr_byte)
            result += curr_byte
        logger.debug("<<< Exiting read_file_binary(file_path=%s)", file_path)
        return result
    except OSError:
        print("File not accessible")
        sys.exit()


def add_key_to_lexicon(
    lexicon: dict[str, str], curr_string: str, index: int, last_match_id: str
) -> None:
    """
    Adds new strings (curr_string + "0",  curr_string + "1") to the lexicon
    """
    lexicon.pop(curr_string)
    lexicon[curr_string + "0"] = last_match_id

    if math.log2(index).is_integer():
        for curr_key, value in lexicon.items():
            lexicon[curr_key] = f"0{value}"

    lexicon[curr_string + "1"] = bin(index)[2:]


def compress_data(data_bits: str) -> str:
    """
    Compresses given data_bits using Lempel-Ziv-Welch compression algorithm
    and returns the result as a string
    """
    logger.debug(">>> Entering compress_data(data_bits=%s)", data_bits)
    lexicon = {"0": "0", "1": "1"}
    logger.debug("compress_data(data_bits=%s): lexicon → %s", data_bits, lexicon)
    result, curr_string = "", ""
    index = len(lexicon)
    logger.debug("compress_data(data_bits=%s): index → %s", data_bits, index)

    for i in range(len(data_bits)):
        curr_string += data_bits[i]
        if curr_string not in lexicon:
            continue

        last_match_id = lexicon[curr_string]
        logger.debug("compress_data(data_bits=%s): last_match_id → %s", data_bits, last_match_id)
        result += last_match_id
        add_key_to_lexicon(lexicon, curr_string, index, last_match_id)
        index += 1
        curr_string = ""
        logger.debug("compress_data(data_bits=%s): curr_string → %s", data_bits, curr_string)

    while curr_string != "" and curr_string not in lexicon:
        curr_string += "0"

    if curr_string != "":
        last_match_id = lexicon[curr_string]
        result += last_match_id

    logger.debug("<<< Exiting compress_data(data_bits=%s)", data_bits)
    return result


def add_file_length(source_path: str, compressed: str) -> str:
    """
    Adds given file's length in front (using Elias  gamma coding) of the compressed
    string
    """
    logger.debug(">>> Entering add_file_length(source_path=%s,compressed=%s)", source_path, compressed)
    file_length = os.path.getsize(source_path)
    logger.debug("add_file_length(source_path=%s,compressed=%s): file_length → %s", source_path, compressed, file_length)
    file_length_binary = bin(file_length)[2:]
    logger.debug("add_file_length(source_path=%s,compressed=%s): file_length_binary → %s", source_path, compressed, file_length_binary)
    length_length = len(file_length_binary)
    logger.debug("add_file_length(source_path=%s,compressed=%s): length_length → %s", source_path, compressed, length_length)

    logger.debug("<<< Exiting add_file_length(source_path=%s,compressed=%s)", source_path, compressed)
    return "0" * (length_length - 1) + file_length_binary + compressed


def write_file_binary(file_path: str, to_write: str) -> None:
    """
    Writes given to_write string (should only consist of 0's and 1's) as bytes in the
    file
    """
    logger.debug(">>> Entering write_file_binary(file_path=%s,to_write=%s)", file_path, to_write)
    logger.debug("write_file_binary(file_path=%s,to_write=%s): result_byte_array → %s", file_path, to_write, result_byte_array)
    byte_length = 8
    logger.debug("write_file_binary(file_path=%s,to_write=%s): byte_length → %s", file_path, to_write, byte_length)
    try:
        with open(file_path, "wb") as opened_file:
            logger.error("Exception in write_file_binary(file_path=%s,to_write=%s)", file_path, to_write, exc_info=True)
            result_byte_array = [
                to_write[i : i + byte_length]
                for i in range(0, len(to_write), byte_length)
            ]

            if len(result_byte_array[-1]) % byte_length == 0:
                result_byte_array.append("10000000")
            else:
                result_byte_array[-1] += "1" + "0" * (
                    byte_length - len(result_byte_array[-1]) - 1
                )

            for elem in result_byte_array:
                opened_file.write(int(elem, 2).to_bytes(1, byteorder="big"))
    except OSError:
        print("File not accessible")
        sys.exit()
        logger.debug("<<< Exiting write_file_binary(file_path=%s,to_write=%s)", file_path, to_write)


def compress(source_path: str, destination_path: str) -> None:
    """
    Reads source file, compresses it and writes the compressed result in destination
    file
    """
    logger.debug(">>> Entering compress(source_path=%s,destination_path=%s)", source_path, destination_path)
    data_bits = read_file_binary(source_path)
    logger.debug("compress(source_path=%s,destination_path=%s): data_bits → %s", source_path, destination_path, data_bits)
    compressed = compress_data(data_bits)
    compressed = add_file_length(source_path, compressed)
    logger.debug("compress(source_path=%s,destination_path=%s): compressed → %s", source_path, destination_path, compressed)
    write_file_binary(destination_path, compressed)
    logger.debug("<<< Exiting compress(source_path=%s,destination_path=%s)", source_path, destination_path)


if __name__ == "__main__":
    compress(sys.argv[1], sys.argv[2])
