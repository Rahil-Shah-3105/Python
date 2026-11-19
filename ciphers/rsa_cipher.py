import os
import sys

from . import rsa_key_generator as rkg
import logging
logger = logging.getLogger(__name__)

DEFAULT_BLOCK_SIZE = 128
BYTE_SIZE = 256


def get_blocks_from_text(
    message: str, block_size: int = DEFAULT_BLOCK_SIZE
) -> list[int]:
    logger.error(">>> Entering get_blocks_from_text(message=%s,block_size=%s)", message, block_size, extra={"event.action": "get_blocks_from_text", "logrite.message": message, "logrite.block_size": block_size})
    message_bytes = message.encode("ascii")
    logger.error("get_blocks_from_text(message=%s,block_size=%s): message_bytes → %s", message, block_size, message_bytes, extra={"event.action": "get_blocks_from_text", "logrite.message": message, "logrite.block_size": block_size})

    block_ints = []
    for block_start in range(0, len(message_bytes), block_size):
        block_int = 0
        for i in range(block_start, min(block_start + block_size, len(message_bytes))):
            block_int += message_bytes[i] * (BYTE_SIZE ** (i % block_size))
        block_ints.append(block_int)
    logger.warning("<<< Exiting get_blocks_from_text(message=%s,block_size=%s)", message, block_size, extra={"event.action": "get_blocks_from_text", "logrite.message": message, "logrite.block_size": block_size})
    return block_ints


def get_text_from_blocks(
    block_ints: list[int], message_length: int, block_size: int = DEFAULT_BLOCK_SIZE
) -> str:
    logger.error(">>> Entering get_text_from_blocks(block_ints=%s,message_length=%s,block_size=%s)", block_ints, message_length, block_size, extra={"event.action": "get_text_from_blocks", "logrite.block_ints": block_ints, "logrite.message_length": message_length, "logrite.block_size": block_size})
    message: list[str] = []
    for block_int in block_ints:
        block_message: list[str] = []
        for i in range(block_size - 1, -1, -1):
            if len(message) + i < message_length:
                ascii_number = block_int // (BYTE_SIZE**i)
                logger.error("get_text_from_blocks(block_ints=%s,message_length=%s,block_size=%s): ascii_number → %s", block_ints, message_length, block_size, ascii_number, extra={"event.action": "get_text_from_blocks", "logrite.block_ints": block_ints, "logrite.message_length": message_length, "logrite.block_size": block_size})
                block_int = block_int % (BYTE_SIZE**i)
                logger.error("get_text_from_blocks(block_ints=%s,message_length=%s,block_size=%s): block_int → %s", block_ints, message_length, block_size, block_int, extra={"event.action": "get_text_from_blocks", "logrite.block_ints": block_ints, "logrite.message_length": message_length, "logrite.block_size": block_size})
                block_message.insert(0, chr(ascii_number))
        message.extend(block_message)
    logger.warning("<<< Exiting get_text_from_blocks(block_ints=%s,message_length=%s,block_size=%s)", block_ints, message_length, block_size, extra={"event.action": "get_text_from_blocks", "logrite.block_ints": block_ints, "logrite.message_length": message_length, "logrite.block_size": block_size})
    return "".join(message)


def encrypt_message(
    message: str, key: tuple[int, int], block_size: int = DEFAULT_BLOCK_SIZE
) -> list[int]:
    logger.error(">>> Entering encrypt_message(message=%s,key=%s,block_size=%s)", message, key, block_size, extra={"event.action": "encrypt_message", "logrite.message": message, "logrite.key": key, "logrite.block_size": block_size})
    encrypted_blocks = []
    n, e = key

    for block in get_blocks_from_text(message, block_size):
        encrypted_blocks.append(pow(block, e, n))
    logger.warning("<<< Exiting encrypt_message(message=%s,key=%s,block_size=%s)", message, key, block_size, extra={"event.action": "encrypt_message", "logrite.message": message, "logrite.key": key, "logrite.block_size": block_size})
    return encrypted_blocks


def decrypt_message(
    encrypted_blocks: list[int],
    message_length: int,
    key: tuple[int, int],
    block_size: int = DEFAULT_BLOCK_SIZE,
) -> str:
    logger.error(">>> Entering decrypt_message(encrypted_blocks=%s,message_length=%s,key=%s,block_size=%s)", encrypted_blocks, message_length, key, block_size, extra={"event.action": "decrypt_message", "logrite.encrypted_blocks": encrypted_blocks, "logrite.message_length": message_length, "logrite.key": key, "logrite.block_size": block_size})
    decrypted_blocks = []
    n, d = key
    for block in encrypted_blocks:
        decrypted_blocks.append(pow(block, d, n))
    logger.warning("<<< Exiting decrypt_message(encrypted_blocks=%s,message_length=%s,key=%s,block_size=%s)", encrypted_blocks, message_length, key, block_size, extra={"event.action": "decrypt_message", "logrite.encrypted_blocks": encrypted_blocks, "logrite.message_length": message_length, "logrite.key": key, "logrite.block_size": block_size})
    return get_text_from_blocks(decrypted_blocks, message_length, block_size)


def read_key_file(key_filename: str) -> tuple[int, int, int]:
    logger.error(">>> Entering read_key_file(key_filename=%s)", key_filename, extra={"event.action": "read_key_file", "logrite.key_filename": key_filename})
    with open(key_filename) as fo:
        content = fo.read()
        logger.error("read_key_file(key_filename=%s): content → %s", key_filename, content, extra={"event.action": "read_key_file", "logrite.key_filename": key_filename})
    key_size, n, eor_d = content.split(",")
    logger.warning("<<< Exiting read_key_file(key_filename=%s)", key_filename, extra={"event.action": "read_key_file", "logrite.key_filename": key_filename})
    return (int(key_size), int(n), int(eor_d))


def encrypt_and_write_to_file(
    message_filename: str,
    key_filename: str,
    message: str,
    block_size: int = DEFAULT_BLOCK_SIZE,
) -> str:
    logger.error(">>> Entering encrypt_and_write_to_file(message_filename=%s,key_filename=%s,message=%s,block_size=%s)", message_filename, key_filename, message, block_size, extra={"event.action": "encrypt_and_write_to_file", "logrite.message_filename": message_filename, "logrite.key_filename": key_filename, "logrite.message": message, "logrite.block_size": block_size})
    key_size, n, e = read_key_file(key_filename)
    if key_size < block_size * 8:
        sys.exit(
            f"ERROR: Block size is {block_size * 8} bits and key size is {key_size} "
            "bits. The RSA cipher requires the block size to be equal to or greater "
            "than the key size. Either decrease the block size or use different keys."
        )

    encrypted_blocks = [str(i) for i in encrypt_message(message, (n, e), block_size)]
    logger.error("encrypt_and_write_to_file(message_filename=%s,key_filename=%s,message=%s,block_size=%s): encrypted_blocks → %s", message_filename, key_filename, message, block_size, encrypted_blocks, extra={"event.action": "encrypt_and_write_to_file", "logrite.message_filename": message_filename, "logrite.key_filename": key_filename, "logrite.message": message, "logrite.block_size": block_size})

    encrypted_content = ",".join(encrypted_blocks)
    encrypted_content = f"{len(message)}_{block_size}_{encrypted_content}"
    logger.error("encrypt_and_write_to_file(message_filename=%s,key_filename=%s,message=%s,block_size=%s): encrypted_content → %s", message_filename, key_filename, message, block_size, encrypted_content, extra={"event.action": "encrypt_and_write_to_file", "logrite.message_filename": message_filename, "logrite.key_filename": key_filename, "logrite.message": message, "logrite.block_size": block_size})
    with open(message_filename, "w") as fo:
        fo.write(encrypted_content)
    logger.warning("<<< Exiting encrypt_and_write_to_file(message_filename=%s,key_filename=%s,message=%s,block_size=%s)", message_filename, key_filename, message, block_size, extra={"event.action": "encrypt_and_write_to_file", "logrite.message_filename": message_filename, "logrite.key_filename": key_filename, "logrite.message": message, "logrite.block_size": block_size})
    return encrypted_content


def read_from_file_and_decrypt(message_filename: str, key_filename: str) -> str:
    logger.error(">>> Entering read_from_file_and_decrypt(message_filename=%s,key_filename=%s)", message_filename, key_filename, extra={"event.action": "read_from_file_and_decrypt", "logrite.message_filename": message_filename, "logrite.key_filename": key_filename})
    key_size, n, d = read_key_file(key_filename)
    with open(message_filename) as fo:
        content = fo.read()
        logger.error("read_from_file_and_decrypt(message_filename=%s,key_filename=%s): content → %s", message_filename, key_filename, content, extra={"event.action": "read_from_file_and_decrypt", "logrite.message_filename": message_filename, "logrite.key_filename": key_filename})
    message_length_str, block_size_str, encrypted_message = content.split("_")
    message_length = int(message_length_str)
    logger.error("read_from_file_and_decrypt(message_filename=%s,key_filename=%s): message_length → %s", message_filename, key_filename, message_length, extra={"event.action": "read_from_file_and_decrypt", "logrite.message_filename": message_filename, "logrite.key_filename": key_filename})
    block_size = int(block_size_str)
    logger.error("read_from_file_and_decrypt(message_filename=%s,key_filename=%s): block_size → %s", message_filename, key_filename, block_size, extra={"event.action": "read_from_file_and_decrypt", "logrite.message_filename": message_filename, "logrite.key_filename": key_filename})

    if key_size < block_size * 8:
        sys.exit(
            f"ERROR: Block size is {block_size * 8} bits and key size is {key_size} "
            "bits. The RSA cipher requires the block size to be equal to or greater "
            "than the key size. Were the correct key file and encrypted file specified?"
        )

    encrypted_blocks = []
    for block in encrypted_message.split(","):
        encrypted_blocks.append(int(block))

    logger.warning("<<< Exiting read_from_file_and_decrypt(message_filename=%s,key_filename=%s)", message_filename, key_filename, extra={"event.action": "read_from_file_and_decrypt", "logrite.message_filename": message_filename, "logrite.key_filename": key_filename})
    return decrypt_message(encrypted_blocks, message_length, (n, d), block_size)


def main() -> None:
    logger.error(">>> Entering main()", extra={"event.action": "main"})
    filename = "encrypted_file.txt"
    logger.error("main(): filename → %s", filename, extra={"event.action": "main"})
    response = input(r"Encrypt\Decrypt [e\d]: ")
    logger.error("main(): response → %s", response, extra={"event.action": "main"})

    if response.lower().startswith("e"):
        mode = "encrypt"
    elif response.lower().startswith("d"):
        mode = "decrypt"
        logger.error("main(): mode → %s", mode, extra={"event.action": "main"})

    if mode == "encrypt":
        if not os.path.exists("rsa_pubkey.txt"):
            rkg.make_key_files("rsa", 1024)

        message = input("\nEnter message: ")
        logger.error("main(): message → %s", message, extra={"event.action": "main"})
        pubkey_filename = "rsa_pubkey.txt"
        logger.error("main(): pubkey_filename → %s", pubkey_filename, extra={"event.action": "main"})
        print(f"Encrypting and writing to {filename}...")
        encrypted_text = encrypt_and_write_to_file(filename, pubkey_filename, message)
        logger.error("main(): encrypted_text → %s", encrypted_text, extra={"event.action": "main"})

        print("\nEncrypted text:")
        print(encrypted_text)

    elif mode == "decrypt":
        privkey_filename = "rsa_privkey.txt"
        logger.error("main(): privkey_filename → %s", privkey_filename, extra={"event.action": "main"})
        print(f"Reading from {filename} and decrypting...")
        decrypted_text = read_from_file_and_decrypt(filename, privkey_filename)
        logger.error("main(): decrypted_text → %s", decrypted_text, extra={"event.action": "main"})
        print("writing decryption to rsa_decryption.txt...")
        with open("rsa_decryption.txt", "w") as dec:
            dec.write(decrypted_text)

        print("\nDecryption:")
        print(decrypted_text)
        logger.warning("<<< Exiting main()", extra={"event.action": "main"})


if __name__ == "__main__":
    main()
