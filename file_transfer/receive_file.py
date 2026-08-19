import socket
import logging
logger = logging.getLogger(__name__)


def main():
    logger.debug(">>> Entering main()")
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    logger.debug("main(): sock → %s", sock)
    host = socket.gethostname()
    port = 12312
    logger.info("main(): host → %s", host)
    logger.debug("main(): host → %s", host)
    logger.info("main(): port → %s", port)

    sock.connect((host, port))
    sock.send(b"Hello server!")

    with open("Received_file", "wb") as out_file:
        print("File opened")
        print("Receiving data...")
        while True:
            data = sock.recv(1024)
            logger.debug("main(): data → %s", data)
            if not data:
                break
            out_file.write(data)

    print("Successfully received the file")
    sock.close()
    print("Connection closed")
    logger.debug("<<< Exiting main()")


if __name__ == "__main__":
    main()
