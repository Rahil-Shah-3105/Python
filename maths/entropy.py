#!/usr/bin/env python3

"""
Implementation of entropy of information
https://en.wikipedia.org/wiki/Entropy_(information_theory)
"""

from __future__ import annotations

import math
from collections import Counter
from string import ascii_lowercase
import logging
logger = logging.getLogger(__name__)


def calculate_prob(text: str) -> None:
    """
    This method takes path and two dict as argument
    and than calculates entropy of them.
    :param dict:
    :param dict:
    :return: Prints
    1) Entropy of information based on 1 alphabet
    2) Entropy of information based on couples of 2 alphabet
    3) print Entropy of H(X n|Xn-1)

    Text from random books. Also, random quotes.
    >>> text = ("Behind Winston's back the voice "
    ...         "from the telescreen was still "
    ...         "babbling and the overfulfilment")
    >>> calculate_prob(text)
    4.0
    6.0
    2.0

    >>> text = ("The Ministry of Truth—Minitrue, in Newspeak [Newspeak was the official"
    ...         "face in elegant lettering, the three")
    >>> calculate_prob(text)
    4.0
    5.0
    1.0
    >>> text = ("Had repulsive dashwoods suspicion sincerity but advantage now him. "
    ...         "Remark easily garret nor nay.  Civil those mrs enjoy shy fat merry. "
    ...         "You greatest jointure saw horrible. He private he on be imagine "
    ...         "suppose. Fertile beloved evident through no service elderly is. Blind "
    ...         "there if every no so at. Own neglected you preferred way sincerity "
    ...         "delivered his attempted. To of message cottage windows do besides "
    ...         "against uncivil.  Delightful unreserved impossible few estimating "
    ...         "men favourable see entreaties. She propriety immediate was improving. "
    ...         "He or entrance humoured likewise moderate. Much nor game son say "
    ...         "feel. Fat make met can must form into gate. Me we offending prevailed "
    ...         "discovery.")
    >>> calculate_prob(text)
    4.0
    7.0
    3.0
    """
    logger.debug(">>> Entering calculate_prob(text=%s)", text)
    single_char_strings, two_char_strings = analyze_text(text)
    my_alphas = list(" " + ascii_lowercase)
    logger.debug("calculate_prob(text=%s): my_alphas → %s", text, my_alphas)
    # what is our total sum of probabilities.
    all_sum = sum(single_char_strings.values())
    logger.debug("calculate_prob(text=%s): all_sum → %s", text, all_sum)

    # one length string
    my_fir_sum = 0
    logger.debug("calculate_prob(text=%s): my_fir_sum → %s", text, my_fir_sum)
    # for each alpha we go in our dict and if it is in it we calculate entropy
    for ch in my_alphas:
        if ch in single_char_strings:
            my_str = single_char_strings[ch]
            logger.debug("calculate_prob(text=%s): my_str → %s", text, my_str)
            prob = my_str / all_sum
            logger.debug("calculate_prob(text=%s): prob → %s", text, prob)
            my_fir_sum += prob * math.log2(prob)  # entropy formula.

    # print entropy
    print(f"{round(-1 * my_fir_sum):.1f}")

    # two len string
    all_sum = sum(two_char_strings.values())
    my_sec_sum = 0
    logger.debug("calculate_prob(text=%s): my_sec_sum → %s", text, my_sec_sum)
    # for each alpha (two in size) calculate entropy.
    for ch0 in my_alphas:
        for ch1 in my_alphas:
            sequence = ch0 + ch1
            logger.debug("calculate_prob(text=%s): sequence → %s", text, sequence)
            if sequence in two_char_strings:
                my_str = two_char_strings[sequence]
                prob = int(my_str) / all_sum
                my_sec_sum += prob * math.log2(prob)

    # print second entropy
    print(f"{round(-1 * my_sec_sum):.1f}")

    # print the difference between them
    print(f"{round((-1 * my_sec_sum) - (-1 * my_fir_sum)):.1f}")
    logger.debug("<<< Exiting calculate_prob(text=%s)", text)


def analyze_text(text: str) -> tuple[dict, dict]:
    """
    Convert text input into two dicts of counts.
    The first dictionary stores the frequency of single character strings.
    The second dictionary stores the frequency of two character strings.
    """
    logger.debug(">>> Entering analyze_text(text=%s)", text)
    single_char_strings = Counter()  # type: ignore[var-annotated]
    logger.debug("analyze_text(text=%s): single_char_strings → %s", text, single_char_strings)
    two_char_strings = Counter()  # type: ignore[var-annotated]
    logger.debug("analyze_text(text=%s): two_char_strings → %s", text, two_char_strings)
    single_char_strings[text[-1]] += 1

    # first case when we have space at start.
    two_char_strings[" " + text[0]] += 1
    for i in range(len(text) - 1):
        single_char_strings[text[i]] += 1
        two_char_strings[text[i : i + 2]] += 1
    logger.debug("<<< Exiting analyze_text(text=%s)", text)
    return single_char_strings, two_char_strings


def main():
    logger.debug(">>> Entering main()")
    import doctest

    doctest.testmod()
    logger.debug("<<< Exiting main()")
    # text = (
    #     "Had repulsive dashwoods suspicion sincerity but advantage now him. Remark "
    #     "easily garret nor nay. Civil those mrs enjoy shy fat merry. You greatest "
    #     "jointure saw horrible. He private he on be imagine suppose. Fertile "
    #     "beloved evident through no service elderly is. Blind there if every no so "
    #     "at. Own neglected you preferred way sincerity delivered his attempted. To "
    #     "of message cottage windows do besides against uncivil.  Delightful "
    #     "unreserved impossible few estimating men favourable see entreaties. She "
    #     "propriety immediate was improving. He or entrance humoured likewise "
    #     "moderate. Much nor game son say feel. Fat make met can must form into "
    #     "gate. Me we offending prevailed discovery. "
    # )

    # calculate_prob(text)


if __name__ == "__main__":
    main()
