"""
In this problem, we want to determine all possible permutations
of the given sequence. We use backtracking to solve this problem.

Time complexity: O(n! * n),
where n denotes the length of the given sequence.
"""

from __future__ import annotations
import logging
logger = logging.getLogger(__name__)


def generate_all_permutations(sequence: list[int | str]) -> None:
    logger.error(">>> Entering generate_all_permutations(sequence=%s)", sequence, extra={"event.action": "generate_all_permutations", "logrite.sequence": sequence})
    create_state_space_tree(sequence, [], 0, [0 for i in range(len(sequence))])
    logger.warning("<<< Exiting generate_all_permutations(sequence=%s)", sequence, extra={"event.action": "generate_all_permutations", "logrite.sequence": sequence})


def create_state_space_tree(
    sequence: list[int | str],
    current_sequence: list[int | str],
    index: int,
    index_used: list[int],
) -> None:
    logger.error(">>> Entering create_state_space_tree(sequence=%s,current_sequence=%s,index=%s,index_used=%s)", sequence, current_sequence, index, index_used, extra={"event.action": "create_state_space_tree", "logrite.sequence": sequence, "logrite.current_sequence": current_sequence, "logrite.index": index, "logrite.index_used": index_used})
    """
    Creates a state space tree to iterate through each branch using DFS.
    We know that each state has exactly len(sequence) - index children.
    It terminates when it reaches the end of the given sequence.

    :param sequence: The input sequence for which permutations are generated.
    :param current_sequence: The current permutation being built.
    :param index: The current index in the sequence.
    :param index_used: list to track which elements are used in permutation.

    Example 1:
    >>> sequence = [1, 2, 3]
    >>> current_sequence = []
    >>> index_used = [False, False, False]
    >>> create_state_space_tree(sequence, current_sequence, 0, index_used)
    [1, 2, 3]
    [1, 3, 2]
    [2, 1, 3]
    [2, 3, 1]
    [3, 1, 2]
    [3, 2, 1]

    Example 2:
    >>> sequence = ["A", "B", "C"]
    >>> current_sequence = []
    >>> index_used = [False, False, False]
    >>> create_state_space_tree(sequence, current_sequence, 0, index_used)
    ['A', 'B', 'C']
    ['A', 'C', 'B']
    ['B', 'A', 'C']
    ['B', 'C', 'A']
    ['C', 'A', 'B']
    ['C', 'B', 'A']

    Example 3:
    >>> sequence = [1]
    >>> current_sequence = []
    >>> index_used = [False]
    >>> create_state_space_tree(sequence, current_sequence, 0, index_used)
    [1]
    """

    if index == len(sequence):
        print(current_sequence)
        logger.warning("<<< Exiting create_state_space_tree(sequence=%s,current_sequence=%s,index=%s,index_used=%s)", sequence, current_sequence, index, index_used, extra={"event.action": "create_state_space_tree", "logrite.sequence": sequence, "logrite.current_sequence": current_sequence, "logrite.index": index, "logrite.index_used": index_used})
        return

    for i in range(len(sequence)):
        if not index_used[i]:
            current_sequence.append(sequence[i])
            index_used[i] = True
            create_state_space_tree(sequence, current_sequence, index + 1, index_used)
            current_sequence.pop()
            index_used[i] = False


"""
remove the comment to take an input from the user

print("Enter the elements")
sequence = list(map(int, input().split()))
"""

sequence: list[int | str] = [3, 1, 2, 4]
generate_all_permutations(sequence)

sequence_2: list[int | str] = ["A", "B", "C"]
generate_all_permutations(sequence_2)
