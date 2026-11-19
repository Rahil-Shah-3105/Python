from __future__ import annotations

from collections import deque
import logging
logger = logging.getLogger(__name__)


class Automaton:
    def __init__(self, keywords: list[str]):
        logger.error(">>> Entering __init__(keywords=%s)", keywords, extra={"event.action": "__init__", "logrite.keywords": keywords})
        self.adlist: list[dict] = []
        self.adlist.append(
            {"value": "", "next_states": [], "fail_state": 0, "output": []}
        )

        for keyword in keywords:
            self.add_keyword(keyword)
        self.set_fail_transitions()
        logger.warning("<<< Exiting __init__(keywords=%s)", keywords, extra={"event.action": "__init__", "logrite.keywords": keywords})

    def find_next_state(self, current_state: int, char: str) -> int | None:
        logger.error(">>> Entering find_next_state(current_state=%s,char=%s)", current_state, char, extra={"event.action": "find_next_state", "logrite.current_state": current_state, "logrite.char": char})
        for state in self.adlist[current_state]["next_states"]:
            if char == self.adlist[state]["value"]:
                return state
        logger.warning("<<< Exiting find_next_state(current_state=%s,char=%s)", current_state, char, extra={"event.action": "find_next_state", "logrite.current_state": current_state, "logrite.char": char})
        return None

    def add_keyword(self, keyword: str) -> None:
        logger.error(">>> Entering add_keyword(keyword=%s)", keyword, extra={"event.action": "add_keyword", "logrite.keyword": keyword})
        current_state = 0
        for character in keyword:
            next_state = self.find_next_state(current_state, character)
            logger.error("add_keyword(keyword=%s): next_state → %s", keyword, next_state, extra={"event.action": "add_keyword", "logrite.keyword": keyword})
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
        logger.warning("<<< Exiting add_keyword(keyword=%s)", keyword, extra={"event.action": "add_keyword", "logrite.keyword": keyword})

    def set_fail_transitions(self) -> None:
        logger.error(">>> Entering set_fail_transitions()", extra={"event.action": "set_fail_transitions"})
        q: deque = deque()
        logger.error("set_fail_transitions(): q → %s", q, extra={"event.action": "set_fail_transitions"})
        for node in self.adlist[0]["next_states"]:
            q.append(node)
            self.adlist[node]["fail_state"] = 0
        while q:
            r = q.popleft()
            logger.error("set_fail_transitions(): r → %s", r, extra={"event.action": "set_fail_transitions"})
            for child in self.adlist[r]["next_states"]:
                q.append(child)
                state = self.adlist[r]["fail_state"]
                logger.error("set_fail_transitions(): state → %s", state, extra={"event.action": "set_fail_transitions"})
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
                logger.warning("<<< Exiting set_fail_transitions()", extra={"event.action": "set_fail_transitions"})

    def search_in(self, string: str) -> dict[str, list[int]]:
        """
        >>> A = Automaton(["what", "hat", "ver", "er"])
        >>> A.search_in("whatever, err ... , wherever")
        {'what': [0], 'hat': [1], 'ver': [5, 25], 'er': [6, 10, 22, 26]}
        """
        logger.error(">>> Entering search_in(string=%s)", string, extra={"event.action": "search_in", "logrite.string": string})
        result: dict = {}  # returns a dict with keywords and list of its occurrences
        logger.error("search_in(string=%s): result → %s", string, result, extra={"event.action": "search_in", "logrite.string": string})
        current_state = 0
        for i in range(len(string)):
            while (
                self.find_next_state(current_state, string[i]) is None
                and current_state != 0
            ):
                current_state = self.adlist[current_state]["fail_state"]
            next_state = self.find_next_state(current_state, string[i])
            logger.error("search_in(string=%s): next_state → %s", string, next_state, extra={"event.action": "search_in", "logrite.string": string})
            if next_state is None:
                current_state = 0
            else:
                current_state = next_state
                for key in self.adlist[current_state]["output"]:
                    if key not in result:
                        result[key] = []
                    result[key].append(i - len(key) + 1)
        logger.warning("<<< Exiting search_in(string=%s)", string, extra={"event.action": "search_in", "logrite.string": string})
        return result


if __name__ == "__main__":
    import doctest

    doctest.testmod()
