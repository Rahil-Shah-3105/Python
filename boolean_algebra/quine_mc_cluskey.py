from __future__ import annotations

from collections.abc import Sequence
from typing import Literal
import logging
logger = logging.getLogger(__name__)


def compare_string(string1: str, string2: str) -> str | Literal[False]:
    """
    >>> compare_string('0010','0110')
    '0_10'

    >>> compare_string('0110','1101')
    False
    """
    logger.debug(">>> Entering compare_string(string1=%s,string2=%s)", string1, string2)
    list1 = list(string1)
    logger.debug("compare_string(string1=%s,string2=%s): list1 → %s", string1, string2, list1)
    list2 = list(string2)
    logger.debug("compare_string(string1=%s,string2=%s): list2 → %s", string1, string2, list2)
    count = 0
    logger.debug("compare_string(string1=%s,string2=%s): count → %s", string1, string2, count)
    for i in range(len(list1)):
        if list1[i] != list2[i]:
            count += 1
            list1[i] = "_"
    if count > 1:
        return False
    else:
        logger.debug("<<< Exiting compare_string(string1=%s,string2=%s)", string1, string2)
        return "".join(list1)


def check(binary: list[str]) -> list[str]:
    """
    >>> check(['0.00.01.5'])
    ['0.00.01.5']
    """
    logger.debug(">>> Entering check(binary=%s)", binary)
    pi = []
    while True:
        check1 = ["$"] * len(binary)
        logger.debug("check(binary=%s): check1 → %s", binary, check1)
        temp = []
        for i in range(len(binary)):
            for j in range(i + 1, len(binary)):
                k = compare_string(binary[i], binary[j])
                if k is False:
                    check1[i] = "*"
                    check1[j] = "*"
                    temp.append("X")
        for i in range(len(binary)):
            if check1[i] == "$":
                pi.append(binary[i])
        if len(temp) == 0:
            logger.debug("<<< Exiting check(binary=%s)", binary)
            return pi
        binary = list(set(temp))


def decimal_to_binary(no_of_variable: int, minterms: Sequence[float]) -> list[str]:
    """
    >>> decimal_to_binary(3,[1.5])
    ['0.00.01.5']
    """
    logger.debug(">>> Entering decimal_to_binary(no_of_variable=%s,minterms=%s)", no_of_variable, minterms)
    temp = []
    for minterm in minterms:
        string = ""
        logger.debug("decimal_to_binary(no_of_variable=%s,minterms=%s): string → %s", no_of_variable, minterms, string)
        for _ in range(no_of_variable):
            string = str(minterm % 2) + string
            minterm //= 2
        temp.append(string)
    logger.debug("<<< Exiting decimal_to_binary(no_of_variable=%s,minterms=%s)", no_of_variable, minterms)
    return temp


def is_for_table(string1: str, string2: str, count: int) -> bool:
    """
    >>> is_for_table('__1','011',2)
    True

    >>> is_for_table('01_','001',1)
    False
    """
    logger.debug(">>> Entering is_for_table(string1=%s,string2=%s,count=%s)", string1, string2, count)
    list1 = list(string1)
    logger.debug("is_for_table(string1=%s,string2=%s,count=%s): list1 → %s", string1, string2, count, list1)
    list2 = list(string2)
    logger.debug("is_for_table(string1=%s,string2=%s,count=%s): list2 → %s", string1, string2, count, list2)
    count_n = sum(item1 != item2 for item1, item2 in zip(list1, list2))
    logger.debug("is_for_table(string1=%s,string2=%s,count=%s): count_n → %s", string1, string2, count, count_n)
    logger.debug("<<< Exiting is_for_table(string1=%s,string2=%s,count=%s)", string1, string2, count)
    return count_n == count


def selection(chart: list[list[int]], prime_implicants: list[str]) -> list[str]:
    """
    >>> selection([[1]],['0.00.01.5'])
    ['0.00.01.5']

    >>> selection([[1]],['0.00.01.5'])
    ['0.00.01.5']
    """
    logger.debug(">>> Entering selection(chart=%s,prime_implicants=%s)", chart, prime_implicants)
    temp = []
    select = [0] * len(chart)
    logger.debug("selection(chart=%s,prime_implicants=%s): select → %s", chart, prime_implicants, select)
    for i in range(len(chart[0])):
        count = sum(row[i] == 1 for row in chart)
        logger.debug("selection(chart=%s,prime_implicants=%s): count → %s", chart, prime_implicants, count)
        if count == 1:
            rem = max(j for j, row in enumerate(chart) if row[i] == 1)
            select[rem] = 1
    for i, item in enumerate(select):
        if item != 1:
            continue
        for j in range(len(chart[0])):
            if chart[i][j] != 1:
                continue
            for row in chart:
                row[j] = 0
        temp.append(prime_implicants[i])
    while True:
        counts = [chart[i].count(1) for i in range(len(chart))]
        logger.debug("selection(chart=%s,prime_implicants=%s): counts → %s", chart, prime_implicants, counts)
        max_n = max(counts)
        logger.debug("selection(chart=%s,prime_implicants=%s): max_n → %s", chart, prime_implicants, max_n)
        rem = counts.index(max_n)
        logger.debug("selection(chart=%s,prime_implicants=%s): rem → %s", chart, prime_implicants, rem)

        if max_n == 0:
            logger.debug("<<< Exiting selection(chart=%s,prime_implicants=%s)", chart, prime_implicants)
            return temp

        temp.append(prime_implicants[rem])

        for j in range(len(chart[0])):
            if chart[rem][j] != 1:
                continue
            for i in range(len(chart)):
                chart[i][j] = 0


def prime_implicant_chart(
    prime_implicants: list[str], binary: list[str]
) -> list[list[int]]:
    """
    >>> prime_implicant_chart(['0.00.01.5'],['0.00.01.5'])
    [[1]]
    """
    chart = [[0 for x in range(len(binary))] for x in range(len(prime_implicants))]
    for i in range(len(prime_implicants)):
        count = prime_implicants[i].count("_")
        for j in range(len(binary)):
            if is_for_table(prime_implicants[i], binary[j], count):
                chart[i][j] = 1

    return chart


def main() -> None:
    logger.debug(">>> Entering main()")
    no_of_variable = int(input("Enter the no. of variables\n"))
    logger.debug("main(): no_of_variable → %s", no_of_variable)
    minterms = [
        float(x)
        for x in input(
            "Enter the decimal representation of Minterms 'Spaces Separated'\n"
        ).split()
    ]
    binary = decimal_to_binary(no_of_variable, minterms)
    logger.debug("main(): minterms → %s", minterms)
    logger.debug("main(): binary → %s", binary)

    prime_implicants = check(binary)
    print("Prime Implicants are:")
    logger.debug("main(): prime_implicants → %s", prime_implicants)
    print(prime_implicants)
    chart = prime_implicant_chart(prime_implicants, binary)
    logger.debug("main(): chart → %s", chart)

    essential_prime_implicants = selection(chart, prime_implicants)
    logger.debug("main(): essential_prime_implicants → %s", essential_prime_implicants)
    print("Essential Prime Implicants are:")
    print(essential_prime_implicants)
    logger.debug("<<< Exiting main()")


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    main()
