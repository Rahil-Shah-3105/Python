import logging
logger = logging.getLogger(__name__)
def send_file(filename: str = "mytext.txt", testing: bool = False) -> None:
    logger.debug(">>> Entering send_file(filename=%s,testing=%s)", filename, testing)
    logger.debug("send_file(filename=%s,testing=%s): host → %s", filename, testing, host)
    import socket

    port = 12312  # Reserve a port for your service.
    logger.info("send_file(filename=%s,testing=%s): port → %s", filename, testing, port)
    sock = socket.socket()  # Create a socket object
    logger.debug("send_file(filename=%s,testing=%s): sock → %s", filename, testing, sock)
    host = socket.gethostname()  # Get local machine name
    logger.info("send_file(filename=%s,testing=%s): host → %s", filename, testing, host)
    sock.bind((host, port))  # Bind to the port
    sock.listen(5)  # Now wait for client connection.

    print("Server listening....")

    while True:
        conn, addr = sock.accept()  # Establish connection with client.
        print(f"Got connection from {addr}")
        data = conn.recv(1024)
        logger.debug("send_file(filename=%s,testing=%s): data → %s", filename, testing, data)
        print(f"Server received: {data = }")

        with open(filename, "rb") as in_file:
            data = in_file.read(1024)
            while data:
                conn.send(data)
                print(f"Sent {data!r}")
                data = in_file.read(1024)

        print("Done sending")
        conn.close()
        if testing:  # Allow the test to complete
            break

    sock.shutdown(1)
    sock.close()
    logger.debug("<<< Exiting send_file(filename=%s,testing=%s)", filename, testing)


if __name__ == "__main__":
    send_file()
