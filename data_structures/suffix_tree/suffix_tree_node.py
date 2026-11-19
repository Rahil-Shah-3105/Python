#  Created by: Ramy-Badr-Ahmed (https://github.com/Ramy-Badr-Ahmed)
#  in Pull Request: #11554
#  https://github.com/TheAlgorithms/Python/pull/11554
#
#  Please mention me (@Ramy-Badr-Ahmed) in any issue or pull request
#  addressing bugs/corrections to this file.
#  Thank you!

from __future__ import annotations
import logging
logger = logging.getLogger(__name__)


class SuffixTreeNode:
    def __init__(
        self,
        children: dict[str, SuffixTreeNode] | None = None,
        is_end_of_string: bool = False,
        start: int | None = None,
        end: int | None = None,
        suffix_link: SuffixTreeNode | None = None,
    ) -> None:
        logger.error(">>> Entering __init__(children=%s,is_end_of_string=%s,start=%s,end=%s,suffix_link=%s)", children, is_end_of_string, start, end, suffix_link, extra={"event.action": "__init__", "logrite.children": children, "logrite.is_end_of_string": is_end_of_string, "logrite.start": start, "logrite.end": end, "logrite.suffix_link": suffix_link})
        """
        Initializes a suffix tree node.

        Parameters:
            children (dict[str, SuffixTreeNode] | None): The children of this node.
            is_end_of_string (bool): Indicates if this node represents
                                     the end of a string.
            start (int | None): The start index of the suffix in the text.
            end (int | None): The end index of the suffix in the text.
            suffix_link (SuffixTreeNode | None): Link to another suffix tree node.
        """
        logger.warning("<<< Exiting __init__(children=%s,is_end_of_string=%s,start=%s,end=%s,suffix_link=%s)", children, is_end_of_string, start, end, suffix_link, extra={"event.action": "__init__", "logrite.children": children, "logrite.is_end_of_string": is_end_of_string, "logrite.start": start, "logrite.end": end, "logrite.suffix_link": suffix_link})
        self.children = children or {}
        logger.debug("__init__(self=%s,children=%s,is_end_of_string=%s,start=%s,end=%s,suffix_link=%s): self.children → %s", self, children, is_end_of_string, start, end, suffix_link, self.children, extra={"event.action": "__init__", "logrite.children": children, "logrite.is_end_of_string": is_end_of_string, "logrite.start": start, "logrite.end": end, "logrite.suffix_link": suffix_link})
        self.is_end_of_string = is_end_of_string
        logger.debug("__init__(self=%s,children=%s,is_end_of_string=%s,start=%s,end=%s,suffix_link=%s): self.is_end_of_string → %s", self, children, is_end_of_string, start, end, suffix_link, self.is_end_of_string, extra={"event.action": "__init__", "logrite.children": children, "logrite.is_end_of_string": is_end_of_string, "logrite.start": start, "logrite.end": end, "logrite.suffix_link": suffix_link})
        self.start = start
        logger.debug("__init__(self=%s,children=%s,is_end_of_string=%s,start=%s,end=%s,suffix_link=%s): self.start → %s", self, children, is_end_of_string, start, end, suffix_link, self.start, extra={"event.action": "__init__", "logrite.children": children, "logrite.is_end_of_string": is_end_of_string, "logrite.start": start, "logrite.end": end, "logrite.suffix_link": suffix_link})
        self.end = end
        logger.debug("__init__(self=%s,children=%s,is_end_of_string=%s,start=%s,end=%s,suffix_link=%s): self.end → %s", self, children, is_end_of_string, start, end, suffix_link, self.end, extra={"event.action": "__init__", "logrite.children": children, "logrite.is_end_of_string": is_end_of_string, "logrite.start": start, "logrite.end": end, "logrite.suffix_link": suffix_link})
        self.suffix_link = suffix_link
        logger.debug("__init__(self=%s,children=%s,is_end_of_string=%s,start=%s,end=%s,suffix_link=%s): self.suffix_link → %s", self, children, is_end_of_string, start, end, suffix_link, self.suffix_link, extra={"event.action": "__init__", "logrite.children": children, "logrite.is_end_of_string": is_end_of_string, "logrite.start": start, "logrite.end": end, "logrite.suffix_link": suffix_link})
