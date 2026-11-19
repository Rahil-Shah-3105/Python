import logging
logger = logging.getLogger(__name__)
def send_file(filename: str = "mytext.txt", testing: bool = False) -> None:
    logger.error(">>> Entering send_file(filename=%s,testing=%s)", filename, testing, extra={"event.action": "send_file", "logrite.filename": filename, "logrite.testing": testing})
    import socket

    port = 12312  # Reserve a port for your service.
    sock = socket.socket()  # Create a socket object
    logger.error("send_file(filename=%s,testing=%s): sock → %s", filename, testing, sock, extra={"event.action": "send_file", "logrite.filename": filename, "logrite.testing": testing})
    host = socket.gethostname()  # Get local machine name
    logger.error("send_file(filename=%s,testing=%s): host → %s", filename, testing, host, extra={"event.action": "send_file", "logrite.filename": filename, "logrite.testing": testing})
    sock.bind((host, port))  # Bind to the port
    sock.listen(5)  # Now wait for client connection.

    print("Server listening....")

    while True:
        conn, addr = sock.accept()  # Establish connection with client.
        print(f"Got connection from {addr}")
        data = conn.recv(1024)
        logger.error("send_file(filename=%s,testing=%s): data → %s", filename, testing, data, extra={"event.action": "send_file", "logrite.filename": filename, "logrite.testing": testing})
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
    logger.warning("<<< Exiting send_file(filename=%s,testing=%s)", filename, testing, extra={"event.action": "send_file", "logrite.filename": filename, "logrite.testing": testing})


if __name__ == "__main__":
    send_file()
