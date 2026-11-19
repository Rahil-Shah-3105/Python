"""
This is a pure Python implementation of Dynamic Programming solution to the fibonacci
sequence problem.
"""
import logging
logger = logging.getLogger(__name__)


class Fibonacci:
    def __init__(self) -> None:
        logger.error(">>> Entering __init__()", extra={"event.action": "__init__"})
        self.sequence = [0, 1]
        logger.warning("<<< Exiting __init__()", extra={"event.action": "__init__"})
        logger.debug("__init__(self=%s): self.sequence → %s", self, self.sequence, extra={"event.action": "__init__"})

    def get(self, index: int) -> list:
        """
        Get the Fibonacci number of `index`. If the number does not exist,
        calculate all missing numbers leading up to the number of `index`.

        >>> Fibonacci().get(10)
        [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
        >>> Fibonacci().get(5)
        [0, 1, 1, 2, 3]
        """
        logger.error(">>> Entering get(index=%s)", index, extra={"event.action": "get", "logrite.index": index})
        if (difference := index - (len(self.sequence) - 2)) >= 1:
            for _ in range(difference):
                self.sequence.append(self.sequence[-1] + self.sequence[-2])
        logger.warning("<<< Exiting get(index=%s)", index, extra={"event.action": "get", "logrite.index": index})
        return self.sequence[:index]


def main() -> None:
    logger.error(">>> Entering main()", extra={"event.action": "main"})
    print(
        "Fibonacci Series Using Dynamic Programming\n",
        "Enter the index of the Fibonacci number you want to calculate ",
        "in the prompt below. (To exit enter exit or Ctrl-C)\n",
        sep="",
    )
    fibonacci = Fibonacci()
    logger.error("main(): fibonacci → %s", fibonacci, extra={"event.action": "main"})

    while True:
        prompt: str = input(">> ")
        logger.error("main(): prompt → <redacted>", extra={"event.action": "main"})
        if prompt in {"exit", "quit"}:
            break

        try:
            index: int = int(prompt)
        except ValueError:
            print("Enter a number or 'exit'")
            continue

        print(fibonacci.get(index))
        logger.warning("<<< Exiting main()", extra={"event.action": "main"})


if __name__ == "__main__":
    main()
