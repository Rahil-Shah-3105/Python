"""
One of the several implementations of Lempel-Ziv-Welch decompression algorithm
https://en.wikipedia.org/wiki/Lempel%E2%80%93Ziv%E2%80%93Welch
"""

import math
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


def decompress_data(data_bits: str) -> str:
    """
    Decompresses given data_bits using Lempel-Ziv-Welch compression algorithm
    and returns the result as a string
    """
    logger.debug(">>> Entering decompress_data(data_bits=%s)", data_bits)
    lexicon = {"0": "0", "1": "1"}
    logger.debug("decompress_data(data_bits=%s): lexicon → %s", data_bits, lexicon)
    result, curr_string = "", ""
    index = len(lexicon)
    logger.debug("decompress_data(data_bits=%s): index → %s", data_bits, index)

    for i in range(len(data_bits)):
        curr_string += data_bits[i]
        if curr_string not in lexicon:
            continue

        last_match_id = lexicon[curr_string]
        logger.debug("decompress_data(data_bits=%s): last_match_id → %s", data_bits, last_match_id)
        result += last_match_id
        lexicon[curr_string] = last_match_id + "0"

        if math.log2(index).is_integer():
            new_lex = {}
            logger.debug("decompress_data(data_bits=%s): new_lex → %s", data_bits, new_lex)
            for curr_key in list(lexicon):
                new_lex["0" + curr_key] = lexicon.pop(curr_key)
            lexicon = new_lex

        lexicon[bin(index)[2:]] = last_match_id + "1"
        index += 1
        curr_string = ""
        logger.debug("decompress_data(data_bits=%s): curr_string → %s", data_bits, curr_string)
    logger.debug("<<< Exiting decompress_data(data_bits=%s)", data_bits)
    return result


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

            for elem in result_byte_array[:-1]:
                opened_file.write(int(elem, 2).to_bytes(1, byteorder="big"))
    except OSError:
        print("File not accessible")
        sys.exit()
        logger.debug("<<< Exiting write_file_binary(file_path=%s,to_write=%s)", file_path, to_write)


def remove_prefix(data_bits: str) -> str:
    """
    Removes size prefix, that compressed file should have
    Returns the result
    """
    logger.debug(">>> Entering remove_prefix(data_bits=%s)", data_bits)
    counter = 0
    logger.debug("remove_prefix(data_bits=%s): counter → %s", data_bits, counter)
    for letter in data_bits:
        if letter == "1":
            break
        counter += 1

    data_bits = data_bits[counter:]
    data_bits = data_bits[counter + 1 :]
    logger.debug("remove_prefix(data_bits=%s): data_bits → %s", data_bits, data_bits)
    logger.debug("<<< Exiting remove_prefix(data_bits=%s)", data_bits)
    return data_bits


def compress(source_path: str, destination_path: str) -> None:
    """
    Reads source file, decompresses it and writes the result in destination file
    """
    logger.debug(">>> Entering compress(source_path=%s,destination_path=%s)", source_path, destination_path)
    data_bits = read_file_binary(source_path)
    data_bits = remove_prefix(data_bits)
    logger.debug("compress(source_path=%s,destination_path=%s): data_bits → %s", source_path, destination_path, data_bits)
    decompressed = decompress_data(data_bits)
    logger.debug("compress(source_path=%s,destination_path=%s): decompressed → %s", source_path, destination_path, decompressed)
    write_file_binary(destination_path, decompressed)
    logger.debug("<<< Exiting compress(source_path=%s,destination_path=%s)", source_path, destination_path)


if __name__ == "__main__":
    compress(sys.argv[1], sys.argv[2])
