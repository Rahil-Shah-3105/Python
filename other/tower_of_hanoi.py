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
    logger.debug(">>> Entering move_tower(height=%s,from_pole=%s,to_pole=%s,with_pole=%s)", height, from_pole, to_pole, with_pole)
    if height >= 1:
        move_tower(height - 1, from_pole, with_pole, to_pole)
        move_disk(from_pole, to_pole)
        move_tower(height - 1, with_pole, to_pole, from_pole)
        logger.debug("<<< Exiting move_tower(height=%s,from_pole=%s,to_pole=%s,with_pole=%s)", height, from_pole, to_pole, with_pole)


def move_disk(fp, tp):
    logger.debug(">>> Entering move_disk(fp=%s,tp=%s)", fp, tp)
    print("moving disk from", fp, "to", tp)
    logger.debug("<<< Exiting move_disk(fp=%s,tp=%s)", fp, tp)


def main():
    logger.debug(">>> Entering main()")
    height = int(input("Height of hanoi: ").strip())
    logger.debug("main(): height → %s", height)
    move_tower(height, "A", "B", "C")
    logger.debug("<<< Exiting main()")


if __name__ == "__main__":
    main()
