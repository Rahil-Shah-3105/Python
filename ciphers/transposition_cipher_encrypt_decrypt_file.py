import os
import sys
import time

from . import transposition_cipher as trans_cipher
import logging
logger = logging.getLogger(__name__)


def main() -> None:
    logger.debug(">>> Entering main()")
    input_file = "./prehistoric_men.txt"
    logger.debug("main(): input_file → %s", input_file)
    output_file = "./Output.txt"
    key = int(input("Enter key: "))
    logger.debug("main(): output_file → %s", output_file)
    mode = input("Encrypt/Decrypt [e/d]: ")

    logger.warning("main(): key → %s", key)
    logger.debug("main(): key → %s", key)
    logger.debug("main(): mode → %s", mode)
    if not os.path.exists(input_file):
        print(f"File {input_file} does not exist. Quitting...")
        sys.exit()
    if os.path.exists(output_file):
        print(f"Overwrite {output_file}? [y/n]")
        response = input("> ")
        logger.debug("main(): response → %s", response)
        if not response.lower().startswith("y"):
            sys.exit()

    start_time = time.time()
    logger.debug("main(): start_time → %s", start_time)
    if mode.lower().startswith("e"):
        with open(input_file) as f:
            logger.error("Exception in main()", exc_info=True)
            content = f.read()
            logger.debug("main(): content → %s", content)
        translated = trans_cipher.encrypt_message(key, content)
        logger.debug("main(): translated → %s", translated)
    elif mode.lower().startswith("d"):
        with open(output_file) as f:
            content = f.read()
        translated = trans_cipher.decrypt_message(key, content)

    with open(output_file, "w") as output_obj:
        output_obj.write(translated)

    total_time = round(time.time() - start_time, 2)
    logger.debug("main(): total_time → %s", total_time)
    print(("Done (", total_time, "seconds )"))
    logger.debug("<<< Exiting main()")


if __name__ == "__main__":
    main()
