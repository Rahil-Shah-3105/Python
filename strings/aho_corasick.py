from __future__ import annotations

from collections import deque
import logging
logger = logging.getLogger(__name__)


class Automaton:
    def __init__(self, keywords: list[str]):
        logger.debug(">>> Entering __init__(keywords=%s)", keywords)
        self.adlist: list[dict] = []
        self.adlist.append(
            {"value": "", "next_states": [], "fail_state": 0, "output": []}
        )

        for keyword in keywords:
            self.add_keyword(keyword)
        self.set_fail_transitions()
        logger.debug("<<< Exiting __init__(keywords=%s)", keywords)

    def find_next_state(self, current_state: int, char: str) -> int | None:
        logger.debug(">>> Entering find_next_state(current_state=%s,char=%s)", current_state, char)
        for state in self.adlist[current_state]["next_states"]:
            if char == self.adlist[state]["value"]:
                return state
        logger.debug("<<< Exiting find_next_state(current_state=%s,char=%s)", current_state, char)
        return None

    def add_keyword(self, keyword: str) -> None:
        logger.debug(">>> Entering add_keyword(keyword=%s)", keyword)
        logger.debug("add_keyword(keyword=%s): next_state → %s", keyword, next_state)
        logger.debug("add_keyword(self=%s,keyword=%s): next_state → %s", self, keyword, next_state)
        current_state = 0
        logger.debug("add_keyword(self=%s,keyword=%s): current_state → %s", self, keyword, current_state)
        for character in keyword:
            next_state = self.find_next_state(current_state, character)
            if next_state is None:
                self.adlist.append(
                    {
                        "value": character,
                        "next_states": [],
                        "fail_state": 0,
                        "output": [],
                    }
                )
                self.adlist[current_state]["next_states"].append(len(self.adlist) - 1)
                current_state = len(self.adlist) - 1
            else:
                current_state = next_state
        self.adlist[current_state]["output"].append(keyword)
        logger.debug("<<< Exiting add_keyword(keyword=%s)", keyword)

    def set_fail_transitions(self) -> None:
        logger.debug(">>> Entering set_fail_transitions()")
        logger.debug("set_fail_transitions(): q → %s", q)
        q: deque = deque()
        for node in self.adlist[0]["next_states"]:
            q.append(node)
            self.adlist[node]["fail_state"] = 0
        while q:
            r = q.popleft()
            logger.debug("set_fail_transitions(): r → %s", r)
            for child in self.adlist[r]["next_states"]:
                q.append(child)
                state = self.adlist[r]["fail_state"]
                logger.debug("set_fail_transitions(self=%s): state → %s", self, state)
                logger.debug("set_fail_transitions(): state → %s", state)
                while (
                    self.find_next_state(state, self.adlist[child]["value"]) is None
                    and state != 0
                ):
                    state = self.adlist[state]["fail_state"]
                self.adlist[child]["fail_state"] = self.find_next_state(
                    state, self.adlist[child]["value"]
                )
                if self.adlist[child]["fail_state"] is None:
                    self.adlist[child]["fail_state"] = 0
                self.adlist[child]["output"] = (
                    self.adlist[child]["output"]
                    + self.adlist[self.adlist[child]["fail_state"]]["output"]
                )
                logger.debug("<<< Exiting set_fail_transitions()")

    def search_in(self, string: str) -> dict[str, list[int]]:
        """
        >>> A = Automaton(["what", "hat", "ver", "er"])
        >>> A.search_in("whatever, err ... , wherever")
        {'what': [0], 'hat': [1], 'ver': [5, 25], 'er': [6, 10, 22, 26]}
        """
        result: dict = {}  # returns a dict with keywords and list of its occurrences
        current_state = 0
        for i in range(len(string)):
            while (
                self.find_next_state(current_state, string[i]) is None
                and current_state != 0
            ):
                current_state = self.adlist[current_state]["fail_state"]
            next_state = self.find_next_state(current_state, string[i])
            if next_state is None:
                current_state = 0
            else:
                current_state = next_state
                for key in self.adlist[current_state]["output"]:
                    if key not in result:
                        result[key] = []
                    result[key].append(i - len(key) + 1)
        return result


if __name__ == "__main__":
    import doctest

    doctest.testmod()
