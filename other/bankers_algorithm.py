# A Python implementation of the Banker's Algorithm in Operating Systems using
# Processes and Resources
# {
# "Author: "Biney Kingsley (bluedistro@github.io), bineykingsley36@gmail.com",
# "Date": 28-10-2018
# }
"""
The Banker's algorithm is a resource allocation and deadlock avoidance algorithm
developed by Edsger Dijkstra that tests for safety by simulating the allocation of
predetermined maximum possible amounts of all resources, and then makes a "s-state"
check to test for possible deadlock conditions for all other pending activities,
before deciding whether allocation should be allowed to continue.

| [Source] Wikipedia
| [Credit] Rosetta Code C implementation helped very much.
| (https://rosettacode.org/wiki/Banker%27s_algorithm)
"""

from __future__ import annotations

import numpy as np
import logging
logger = logging.getLogger(__name__)

test_claim_vector = [8, 5, 9, 7]
test_allocated_res_table = [
    [2, 0, 1, 1],
    [0, 1, 2, 1],
    [4, 0, 0, 3],
    [0, 2, 1, 0],
    [1, 0, 3, 0],
]
test_maximum_claim_table = [
    [3, 2, 1, 4],
    [0, 2, 5, 2],
    [5, 1, 0, 5],
    [1, 5, 3, 0],
    [3, 0, 3, 3],
]


class BankersAlgorithm:
    def __init__(
        self,
        claim_vector: list[int],
        allocated_resources_table: list[list[int]],
        maximum_claim_table: list[list[int]],
    ) -> None:
        logger.error(">>> Entering __init__(claim_vector=%s,allocated_resources_table=%s,maximum_claim_table=%s)", claim_vector, allocated_resources_table, maximum_claim_table, extra={"event.action": "__init__", "logrite.claim_vector": claim_vector, "logrite.allocated_resources_table": allocated_resources_table, "logrite.maximum_claim_table": maximum_claim_table})
        """
        :param claim_vector: A nxn/nxm list depicting the amount of each resources
         (eg. memory, interface, semaphores, etc.) available.
        :param allocated_resources_table: A nxn/nxm list depicting the amount of each
         resource each process is currently holding
        :param maximum_claim_table: A nxn/nxm list depicting how much of each resource
         the system currently has available
        """
        logger.warning("<<< Exiting __init__(claim_vector=%s,allocated_resources_table=%s,maximum_claim_table=%s)", claim_vector, allocated_resources_table, maximum_claim_table, extra={"event.action": "__init__", "logrite.claim_vector": claim_vector, "logrite.allocated_resources_table": allocated_resources_table, "logrite.maximum_claim_table": maximum_claim_table})
        self.__claim_vector = claim_vector
        logger.debug("__init__(self=%s,claim_vector=%s,allocated_resources_table=%s,maximum_claim_table=%s): self.__claim_vector → %s", self, claim_vector, allocated_resources_table, maximum_claim_table, self.__claim_vector, extra={"event.action": "__init__", "logrite.claim_vector": claim_vector, "logrite.allocated_resources_table": allocated_resources_table, "logrite.maximum_claim_table": maximum_claim_table})
        self.__allocated_resources_table = allocated_resources_table
        logger.debug("__init__(self=%s,claim_vector=%s,allocated_resources_table=%s,maximum_claim_table=%s): self.__allocated_resources_table → %s", self, claim_vector, allocated_resources_table, maximum_claim_table, self.__allocated_resources_table, extra={"event.action": "__init__", "logrite.claim_vector": claim_vector, "logrite.allocated_resources_table": allocated_resources_table, "logrite.maximum_claim_table": maximum_claim_table})
        self.__maximum_claim_table = maximum_claim_table
        logger.debug("__init__(self=%s,claim_vector=%s,allocated_resources_table=%s,maximum_claim_table=%s): self.__maximum_claim_table → %s", self, claim_vector, allocated_resources_table, maximum_claim_table, self.__maximum_claim_table, extra={"event.action": "__init__", "logrite.claim_vector": claim_vector, "logrite.allocated_resources_table": allocated_resources_table, "logrite.maximum_claim_table": maximum_claim_table})

    def __processes_resource_summation(self) -> list[int]:
        """
        Check for allocated resources in line with each resource in the claim vector
        """
        logger.error(">>> Entering __processes_resource_summation()", extra={"event.action": "__processes_resource_summation"})
        logger.warning("<<< Exiting __processes_resource_summation()", extra={"event.action": "__processes_resource_summation"})
        return [
            sum(p_item[i] for p_item in self.__allocated_resources_table)
            for i in range(len(self.__allocated_resources_table[0]))
        ]

    def __available_resources(self) -> list[int]:
        """
        Check for available resources in line with each resource in the claim vector
        """
        logger.error(">>> Entering __available_resources()", extra={"event.action": "__available_resources"})
        logger.warning("<<< Exiting __available_resources()", extra={"event.action": "__available_resources"})
        return np.array(self.__claim_vector) - np.array(
            self.__processes_resource_summation()
        )

    def __need(self) -> list[list[int]]:
        """
        Implement safety checker that calculates the needs by ensuring that
        ``max_claim[i][j] - alloc_table[i][j] <= avail[j]``
        """
        logger.error(">>> Entering __need()", extra={"event.action": "__need"})
        logger.warning("<<< Exiting __need()", extra={"event.action": "__need"})
        return [
            list(np.array(self.__maximum_claim_table[i]) - np.array(allocated_resource))
            for i, allocated_resource in enumerate(self.__allocated_resources_table)
        ]

    def __need_index_manager(self) -> dict[int, list[int]]:
        """
        This function builds an index control dictionary to track original ids/indices
        of processes when altered during execution of method "main"

            :Return: {0: [a: int, b: int], 1: [c: int, d: int]}

        >>> index_control = BankersAlgorithm(
        ...     test_claim_vector, test_allocated_res_table, test_maximum_claim_table
        ... )._BankersAlgorithm__need_index_manager()
        >>> {key: [int(x) for x in value] for key, value
        ...     in index_control.items()}  # doctest: +NORMALIZE_WHITESPACE
        {0: [1, 2, 0, 3], 1: [0, 1, 3, 1], 2: [1, 1, 0, 2], 3: [1, 3, 2, 0],
         4: [2, 0, 0, 3]}
        """
        logger.error(">>> Entering __need_index_manager()", extra={"event.action": "__need_index_manager"})
        logger.warning("<<< Exiting __need_index_manager()", extra={"event.action": "__need_index_manager"})
        return {self.__need().index(i): i for i in self.__need()}

    def main(self, **kwargs) -> None:
        """
        Utilize various methods in this class to simulate the Banker's algorithm
            :Return: None

        >>> BankersAlgorithm(test_claim_vector, test_allocated_res_table,
        ...    test_maximum_claim_table).main(describe=True)
                 Allocated Resource Table
        P1       2        0        1        1
        <BLANKLINE>
        P2       0        1        2        1
        <BLANKLINE>
        P3       4        0        0        3
        <BLANKLINE>
        P4       0        2        1        0
        <BLANKLINE>
        P5       1        0        3        0
        <BLANKLINE>
                 System Resource Table
        P1       3        2        1        4
        <BLANKLINE>
        P2       0        2        5        2
        <BLANKLINE>
        P3       5        1        0        5
        <BLANKLINE>
        P4       1        5        3        0
        <BLANKLINE>
        P5       3        0        3        3
        <BLANKLINE>
        Current Usage by Active Processes: 8 5 9 7
        Initial Available Resources:       1 2 2 2
        __________________________________________________
        <BLANKLINE>
        Process 3 is executing.
        Updated available resource stack for processes: 5 2 2 5
        The process is in a safe state.
        <BLANKLINE>
        Process 1 is executing.
        Updated available resource stack for processes: 7 2 3 6
        The process is in a safe state.
        <BLANKLINE>
        Process 2 is executing.
        Updated available resource stack for processes: 7 3 5 7
        The process is in a safe state.
        <BLANKLINE>
        Process 4 is executing.
        Updated available resource stack for processes: 7 5 6 7
        The process is in a safe state.
        <BLANKLINE>
        Process 5 is executing.
        Updated available resource stack for processes: 8 5 9 7
        The process is in a safe state.
        <BLANKLINE>
        """
        logger.error(">>> Entering main()", extra={"event.action": "main"})
        need_list = self.__need()
        logger.error("main(): need_list → %s", need_list, extra={"event.action": "main"})
        alloc_resources_table = self.__allocated_resources_table
        available_resources = self.__available_resources()
        logger.error("main(): available_resources → %s", available_resources, extra={"event.action": "main"})
        need_index_manager = self.__need_index_manager()
        logger.error("main(): need_index_manager → %s", need_index_manager, extra={"event.action": "main"})
        for kw, val in kwargs.items():
            if kw and val is True:
                self.__pretty_data()
        print("_" * 50 + "\n")
        while need_list:
            safe = False
            for each_need in need_list:
                execution = True
                for index, need in enumerate(each_need):
                    if need > available_resources[index]:
                        execution = False
                        break
                if execution:
                    safe = True
                    # get the original index of the process from ind_ctrl db
                    for original_need_index, need_clone in need_index_manager.items():
                        if each_need == need_clone:
                            process_number = original_need_index
                    print(f"Process {process_number + 1} is executing.")
                    # remove the process run from stack
                    need_list.remove(each_need)
                    # update available/freed resources stack
                    available_resources = np.array(available_resources) + np.array(
                        alloc_resources_table[process_number]
                    )
                    print(
                        "Updated available resource stack for processes: "
                        + " ".join([str(x) for x in available_resources])
                    )
                    break
            if safe:
                print("The process is in a safe state.\n")
            else:
                print("System in unsafe state. Aborting...\n")
                logger.warning("<<< Exiting main()", extra={"event.action": "main"})
                break

    def __pretty_data(self):
        """
        Properly align display of the algorithm's solution
        """
        logger.error(">>> Entering __pretty_data()", extra={"event.action": "__pretty_data"})
        print(" " * 9 + "Allocated Resource Table")
        for item in self.__allocated_resources_table:
            print(
                f"P{self.__allocated_resources_table.index(item) + 1}"
                + " ".join(f"{it:>8}" for it in item)
                + "\n"
            )
        print(" " * 9 + "System Resource Table")
        for item in self.__maximum_claim_table:
            print(
                f"P{self.__maximum_claim_table.index(item) + 1}"
                + " ".join(f"{it:>8}" for it in item)
                + "\n"
            )
        print(
            "Current Usage by Active Processes: "
            + " ".join(str(x) for x in self.__claim_vector)
        )
        print(
            "Initial Available Resources:       "
            + " ".join(str(x) for x in self.__available_resources())
        )
        logger.warning("<<< Exiting __pretty_data()", extra={"event.action": "__pretty_data"})


if __name__ == "__main__":
    import doctest

    doctest.testmod()
