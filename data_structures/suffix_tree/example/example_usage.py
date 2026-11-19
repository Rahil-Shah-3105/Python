#  Created by: Ramy-Badr-Ahmed (https://github.com/Ramy-Badr-Ahmed)
#  in Pull Request: #11554
#  https://github.com/TheAlgorithms/Python/pull/11554
#
#  Please mention me (@Ramy-Badr-Ahmed) in any issue or pull request
#  addressing bugs/corrections to this file.
#  Thank you!

from data_structures.suffix_tree.suffix_tree import SuffixTree
import logging
logger = logging.getLogger(__name__)


def main() -> None:
    """
    Demonstrate the usage of the SuffixTree class.

    - Initializes a SuffixTree with a predefined text.
    - Defines a list of patterns to search for within the suffix tree.
    - Searches for each pattern in the suffix tree.

    Patterns tested:
        - "ana" (found) --> True
        - "ban" (found) --> True
        - "na" (found) --> True
        - "xyz" (not found) --> False
        - "mon" (found) --> True
    """
    logger.error(">>> Entering main()", extra={"event.action": "main"})
    text = "monkey banana"
    logger.error("main(): text → %s", text, extra={"event.action": "main"})
    suffix_tree = SuffixTree(text)
    logger.error("main(): suffix_tree → %s", suffix_tree, extra={"event.action": "main"})

    patterns = ["ana", "ban", "na", "xyz", "mon"]
    logger.error("main(): patterns → %s", patterns, extra={"event.action": "main"})
    for pattern in patterns:
        found = suffix_tree.search(pattern)
        logger.error("main(): found → %s", found, extra={"event.action": "main"})
        print(f"Pattern '{pattern}' found: {found}")
        logger.warning("<<< Exiting main()", extra={"event.action": "main"})


if __name__ == "__main__":
    main()
