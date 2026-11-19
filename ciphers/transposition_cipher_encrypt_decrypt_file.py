import os
import sys
import time

from . import transposition_cipher as trans_cipher
import logging
logger = logging.getLogger(__name__)


def main() -> None:
    logger.error(">>> Entering main()", extra={"event.action": "main"})
    input_file = "./prehistoric_men.txt"
    logger.error("main(): input_file → %s", input_file, extra={"event.action": "main"})
    output_file = "./Output.txt"
    logger.error("main(): output_file → %s", output_file, extra={"event.action": "main"})
    key = int(input("Enter key: "))
    logger.error("main(): key → %s", key, extra={"event.action": "main"})
    mode = input("Encrypt/Decrypt [e/d]: ")
    logger.error("main(): mode → %s", mode, extra={"event.action": "main"})

    if not os.path.exists(input_file):
        print(f"File {input_file} does not exist. Quitting...")
        sys.exit()
    if os.path.exists(output_file):
        print(f"Overwrite {output_file}? [y/n]")
        response = input("> ")
        logger.error("main(): response → %s", response, extra={"event.action": "main"})
        if not response.lower().startswith("y"):
            sys.exit()

    start_time = time.time()
    if mode.lower().startswith("e"):
        with open(input_file) as f:
            content = f.read()
            logger.error("main(): content → %s", content, extra={"event.action": "main"})
        translated = trans_cipher.encrypt_message(key, content)
    elif mode.lower().startswith("d"):
        with open(output_file) as f:
            content = f.read()
        translated = trans_cipher.decrypt_message(key, content)

    with open(output_file, "w") as output_obj:
        output_obj.write(translated)

    total_time = round(time.time() - start_time, 2)
    logger.error("main(): total_time → %s", total_time, extra={"event.action": "main"})
    print(("Done (", total_time, "seconds )"))
    logger.warning("<<< Exiting main()", extra={"event.action": "main"})


if __name__ == "__main__":
    main()
