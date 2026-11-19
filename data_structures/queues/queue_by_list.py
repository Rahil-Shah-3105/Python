"""Queue represented by a Python list"""

from collections.abc import Iterable
import logging
logger = logging.getLogger(__name__)


class QueueByList[T]:
    def __init__(self, iterable: Iterable[T] | None = None) -> None:
        """
        >>> QueueByList()
        Queue(())
        >>> QueueByList([10, 20, 30])
        Queue((10, 20, 30))
        >>> QueueByList((i**2 for i in range(1, 4)))
        Queue((1, 4, 9))
        """
        logger.error(">>> Entering __init__(iterable=%s)", iterable, extra={"event.action": "__init__", "logrite.iterable": iterable})
        self.entries: list[T] = list(iterable or [])
        logger.warning("<<< Exiting __init__(iterable=%s)", iterable, extra={"event.action": "__init__", "logrite.iterable": iterable})

    def __len__(self) -> int:
        """
        >>> len(QueueByList())
        0
        >>> from string import ascii_lowercase
        >>> len(QueueByList(ascii_lowercase))
        26
        >>> queue = QueueByList()
        >>> for i in range(1, 11):
        ...     queue.put(i)
        >>> len(queue)
        10
        >>> for i in range(2):
        ...   queue.get()
        1
        2
        >>> len(queue)
        8
        """
        logger.error(">>> Entering __len__()", extra={"event.action": "__len__"})

        logger.warning("<<< Exiting __len__()", extra={"event.action": "__len__"})
        return len(self.entries)

    def __repr__(self) -> str:
        """
        >>> queue = QueueByList()
        >>> queue
        Queue(())
        >>> str(queue)
        'Queue(())'
        >>> queue.put(10)
        >>> queue
        Queue((10,))
        >>> queue.put(20)
        >>> queue.put(30)
        >>> queue
        Queue((10, 20, 30))
        """
        logger.error(">>> Entering __repr__()", extra={"event.action": "__repr__"})

        logger.warning("<<< Exiting __repr__()", extra={"event.action": "__repr__"})
        return f"Queue({tuple(self.entries)})"

    def put(self, item: T) -> None:
        """Put `item` to the Queue

        >>> queue = QueueByList()
        >>> queue.put(10)
        >>> queue.put(20)
        >>> len(queue)
        2
        >>> queue
        Queue((10, 20))
        """
        logger.error(">>> Entering put(item=%s)", item, extra={"event.action": "put", "logrite.item": item})

        self.entries.append(item)
        logger.warning("<<< Exiting put(item=%s)", item, extra={"event.action": "put", "logrite.item": item})

    def get(self) -> T:
        """
        Get `item` from the Queue

        >>> queue = QueueByList((10, 20, 30))
        >>> queue.get()
        10
        >>> queue.put(40)
        >>> queue.get()
        20
        >>> queue.get()
        30
        >>> len(queue)
        1
        >>> queue.get()
        40
        >>> queue.get()
        Traceback (most recent call last):
            ...
        IndexError: Queue is empty
        """
        logger.error(">>> Entering get()", extra={"event.action": "get"})

        if not self.entries:
            raise IndexError("Queue is empty")
        logger.warning("<<< Exiting get()", extra={"event.action": "get"})
        return self.entries.pop(0)

    def rotate(self, rotation: int) -> None:
        """Rotate the items of the Queue `rotation` times

        >>> queue = QueueByList([10, 20, 30, 40])
        >>> queue
        Queue((10, 20, 30, 40))
        >>> queue.rotate(1)
        >>> queue
        Queue((20, 30, 40, 10))
        >>> queue.rotate(2)
        >>> queue
        Queue((40, 10, 20, 30))
        """
        logger.error(">>> Entering rotate(rotation=%s)", rotation, extra={"event.action": "rotate", "logrite.rotation": rotation})

        put = self.entries.append
        get = self.entries.pop

        for _ in range(rotation):
            put(get(0))
            logger.warning("<<< Exiting rotate(rotation=%s)", rotation, extra={"event.action": "rotate", "logrite.rotation": rotation})

    def get_front(self) -> T:
        """Get the front item from the Queue

        >>> queue = QueueByList((10, 20, 30))
        >>> queue.get_front()
        10
        >>> queue
        Queue((10, 20, 30))
        >>> queue.get()
        10
        >>> queue.get_front()
        20
        """
        logger.error(">>> Entering get_front()", extra={"event.action": "get_front"})

        logger.warning("<<< Exiting get_front()", extra={"event.action": "get_front"})
        return self.entries[0]


if __name__ == "__main__":
    from doctest import testmod

    testmod()
