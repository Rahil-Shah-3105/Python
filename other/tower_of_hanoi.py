import logging
logger = logging.getLogger(__name__)
def move_tower(height, from_pole, to_pole, with_pole):
    """
    >>> move_tower(3, 'A', 'B', 'C')
    moving disk from A to B
    moving disk from A to C
    moving disk from B to C
    moving disk from A to B
    moving disk from C to A
    moving disk from C to B
    moving disk from A to B
    """
    logger.error(">>> Entering move_tower(height=%s,from_pole=%s,to_pole=%s,with_pole=%s)", height, from_pole, to_pole, with_pole, extra={"event.action": "move_tower", "logrite.height": height, "logrite.from_pole": from_pole, "logrite.to_pole": to_pole, "logrite.with_pole": with_pole})
    if height >= 1:
        move_tower(height - 1, from_pole, with_pole, to_pole)
        move_disk(from_pole, to_pole)
        move_tower(height - 1, with_pole, to_pole, from_pole)
        logger.warning("<<< Exiting move_tower(height=%s,from_pole=%s,to_pole=%s,with_pole=%s)", height, from_pole, to_pole, with_pole, extra={"event.action": "move_tower", "logrite.height": height, "logrite.from_pole": from_pole, "logrite.to_pole": to_pole, "logrite.with_pole": with_pole})


def move_disk(fp, tp):
    logger.error(">>> Entering move_disk(fp=%s,tp=%s)", fp, tp, extra={"event.action": "move_disk", "logrite.fp": fp, "logrite.tp": tp})
    print("moving disk from", fp, "to", tp)
    logger.warning("<<< Exiting move_disk(fp=%s,tp=%s)", fp, tp, extra={"event.action": "move_disk", "logrite.fp": fp, "logrite.tp": tp})


def main():
    logger.error(">>> Entering main()", extra={"event.action": "main"})
    height = int(input("Height of hanoi: ").strip())
    logger.error("main(): height → %s", height, extra={"event.action": "main"})
    move_tower(height, "A", "B", "C")
    logger.warning("<<< Exiting main()", extra={"event.action": "main"})


if __name__ == "__main__":
    main()
