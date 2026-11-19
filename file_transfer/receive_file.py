import socket
import logging
logger = logging.getLogger(__name__)


def main():
    logger.error(">>> Entering main()", extra={"event.action": "main"})
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    logger.error("main(): sock → %s", sock, extra={"event.action": "main"})
    host = socket.gethostname()
    logger.error("main(): host → %s", host, extra={"event.action": "main"})
    port = 12312

    sock.connect((host, port))
    sock.send(b"Hello server!")

    with open("Received_file", "wb") as out_file:
        print("File opened")
        print("Receiving data...")
        while True:
            data = sock.recv(1024)
            logger.error("main(): data → %s", data, extra={"event.action": "main"})
            if not data:
                break
            out_file.write(data)

    print("Successfully received the file")
    sock.close()
    print("Connection closed")
    logger.warning("<<< Exiting main()", extra={"event.action": "main"})


if __name__ == "__main__":
    main()
