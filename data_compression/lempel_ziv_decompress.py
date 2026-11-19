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
    logger.error(">>> Entering read_file_binary(file_path=%s)", file_path, extra={"event.action": "read_file_binary", "logrite.file_path": file_path})
    result = ""
    logger.error("read_file_binary(file_path=%s): result → %s", file_path, result, extra={"event.action": "read_file_binary", "logrite.file_path": file_path})
    try:
        with open(file_path, "rb") as binary_file:
            data = binary_file.read()
            logger.error("read_file_binary(file_path=%s): data → %s", file_path, data, extra={"event.action": "read_file_binary", "logrite.file_path": file_path})
        for dat in data:
            curr_byte = f"{dat:08b}"
            logger.error("read_file_binary(file_path=%s): curr_byte → %s", file_path, curr_byte, extra={"event.action": "read_file_binary", "logrite.file_path": file_path})
            result += curr_byte
        return result
    except OSError:
        logger.warning("<<< Exiting read_file_binary(file_path=%s)", file_path, extra={"event.action": "read_file_binary", "logrite.file_path": file_path})
        print("File not accessible")
        sys.exit()


def decompress_data(data_bits: str) -> str:
    """
    Decompresses given data_bits using Lempel-Ziv-Welch compression algorithm
    and returns the result as a string
    """
    logger.error(">>> Entering decompress_data(data_bits=%s)", data_bits, extra={"event.action": "decompress_data", "logrite.data_bits": data_bits})
    lexicon = {"0": "0", "1": "1"}
    result, curr_string = "", ""
    index = len(lexicon)

    for i in range(len(data_bits)):
        curr_string += data_bits[i]
        if curr_string not in lexicon:
            continue

        last_match_id = lexicon[curr_string]
        result += last_match_id
        lexicon[curr_string] = last_match_id + "0"

        if math.log2(index).is_integer():
            new_lex = {}
            for curr_key in list(lexicon):
                new_lex["0" + curr_key] = lexicon.pop(curr_key)
            lexicon = new_lex

        lexicon[bin(index)[2:]] = last_match_id + "1"
        index += 1
        curr_string = ""
    logger.error("decompress_data(data_bits=%s): curr_string → %s", data_bits, curr_string, extra={"event.action": "decompress_data", "logrite.data_bits": data_bits})
    logger.warning("<<< Exiting decompress_data(data_bits=%s)", data_bits, extra={"event.action": "decompress_data", "logrite.data_bits": data_bits})
    return result


def write_file_binary(file_path: str, to_write: str) -> None:
    """
    Writes given to_write string (should only consist of 0's and 1's) as bytes in the
    file
    """
    logger.error(">>> Entering write_file_binary(file_path=%s,to_write=%s)", file_path, to_write, extra={"event.action": "write_file_binary", "logrite.file_path": file_path, "logrite.to_write": to_write})
    byte_length = 8
    try:
        with open(file_path, "wb") as opened_file:
            result_byte_array = [
                to_write[i : i + byte_length]
                for i in range(0, len(to_write), byte_length)
            ]
            logger.error("write_file_binary(file_path=%s,to_write=%s): result_byte_array → %s", file_path, to_write, result_byte_array, extra={"event.action": "write_file_binary", "logrite.file_path": file_path, "logrite.to_write": to_write})

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
        logger.warning("<<< Exiting write_file_binary(file_path=%s,to_write=%s)", file_path, to_write, extra={"event.action": "write_file_binary", "logrite.file_path": file_path, "logrite.to_write": to_write})


def remove_prefix(data_bits: str) -> str:
    """
    Removes size prefix, that compressed file should have
    Returns the result
    """
    logger.error(">>> Entering remove_prefix(data_bits=%s)", data_bits, extra={"event.action": "remove_prefix", "logrite.data_bits": data_bits})
    counter = 0
    for letter in data_bits:
        if letter == "1":
            break
        counter += 1

    data_bits = data_bits[counter:]
    data_bits = data_bits[counter + 1 :]
    logger.error("remove_prefix(data_bits=%s): data_bits → %s", data_bits, data_bits, extra={"event.action": "remove_prefix", "logrite.data_bits": data_bits})
    logger.warning("<<< Exiting remove_prefix(data_bits=%s)", data_bits, extra={"event.action": "remove_prefix", "logrite.data_bits": data_bits})
    return data_bits


def compress(source_path: str, destination_path: str) -> None:
    """
    Reads source file, decompresses it and writes the result in destination file
    """
    logger.error(">>> Entering compress(source_path=%s,destination_path=%s)", source_path, destination_path, extra={"event.action": "compress", "logrite.source_path": source_path, "logrite.destination_path": destination_path})
    data_bits = read_file_binary(source_path)
    data_bits = remove_prefix(data_bits)
    logger.error("compress(source_path=%s,destination_path=%s): data_bits → %s", source_path, destination_path, data_bits, extra={"event.action": "compress", "logrite.source_path": source_path, "logrite.destination_path": destination_path})
    decompressed = decompress_data(data_bits)
    logger.error("compress(source_path=%s,destination_path=%s): decompressed → %s", source_path, destination_path, decompressed, extra={"event.action": "compress", "logrite.source_path": source_path, "logrite.destination_path": destination_path})
    write_file_binary(destination_path, decompressed)
    logger.warning("<<< Exiting compress(source_path=%s,destination_path=%s)", source_path, destination_path, extra={"event.action": "compress", "logrite.source_path": source_path, "logrite.destination_path": destination_path})


if __name__ == "__main__":
    compress(sys.argv[1], sys.argv[2])
