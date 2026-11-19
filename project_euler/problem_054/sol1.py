"""
Problem: https://projecteuler.net/problem=54

In the card game poker, a hand consists of five cards and are ranked,
from lowest to highest, in the following way:

High Card: Highest value card.
One Pair: Two cards of the same value.
Two Pairs: Two different pairs.
Three of a Kind: Three cards of the same value.
Straight: All cards are consecutive values.
Flush: All cards of the same suit.
Full House: Three of a kind and a pair.
Four of a Kind: Four cards of the same value.
Straight Flush: All cards are consecutive values of same suit.
Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.

The cards are valued in the order:
2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.

If two players have the same ranked hands then the rank made up of the highest
value wins; for example, a pair of eights beats a pair of fives.
But if two ranks tie, for example, both players have a pair of queens, then highest
cards in each hand are compared; if the highest cards tie then the next highest
cards are compared, and so on.

The file, poker.txt, contains one-thousand random hands dealt to two players.
Each line of the file contains ten cards (separated by a single space): the
first five are Player 1's cards and the last five are Player 2's cards.
You can assume that all hands are valid (no invalid characters or repeated cards),
each player's hand is in no specific order, and in each hand there is a clear winner.

How many hands does Player 1 win?

Resources used:
https://en.wikipedia.org/wiki/Texas_hold_%27em
https://en.wikipedia.org/wiki/List_of_poker_hands

Similar problem on codewars:
https://www.codewars.com/kata/ranking-poker-hands
https://www.codewars.com/kata/sortable-poker-hands
"""

from __future__ import annotations

import os
import logging
logger = logging.getLogger(__name__)


class PokerHand:
    """Create an object representing a Poker Hand based on an input of a
    string which represents the best 5-card combination from the player's hand
    and board cards.

    Attributes: (read-only)
        hand: a string representing the hand consisting of five cards

    Methods:
        compare_with(opponent): takes in player's hand (self) and
            opponent's hand (opponent) and compares both hands according to
            the rules of Texas Hold'em.
            Returns one of 3 strings (Win, Loss, Tie) based on whether
            player's hand is better than the opponent's hand.

        hand_name(): Returns a string made up of two parts: hand name
            and high card.

    Supported operators:
        Rich comparison operators: <, >, <=, >=, ==, !=

    Supported built-in methods and functions:
        list.sort(), sorted()
    """

    _HAND_NAME = (
        "High card",
        "One pair",
        "Two pairs",
        "Three of a kind",
        "Straight",
        "Flush",
        "Full house",
        "Four of a kind",
        "Straight flush",
        "Royal flush",
    )

    _CARD_NAME = (
        "",  # placeholder as tuples are zero-indexed
        "One",
        "Two",
        "Three",
        "Four",
        "Five",
        "Six",
        "Seven",
        "Eight",
        "Nine",
        "Ten",
        "Jack",
        "Queen",
        "King",
        "Ace",
    )

    def __init__(self, hand: str) -> None:
        """
        Initialize hand.
        Hand should of type str and should contain only five cards each
        separated by a space.

        The cards should be of the following format:
        [card value][card suit]

        The first character is the value of the card:
        2, 3, 4, 5, 6, 7, 8, 9, T(en), J(ack), Q(ueen), K(ing), A(ce)

        The second character represents the suit:
        S(pades), H(earts), D(iamonds), C(lubs)

        For example: "6S 4C KC AS TH"
        """
        logger.error(">>> Entering __init__(hand=%s)", hand, extra={"event.action": "__init__", "logrite.hand": hand})
        if not isinstance(hand, str):
            msg = f"Hand should be of type 'str': {hand!r}"
            logger.error("__init__(hand=%s): msg → %s", hand, msg, extra={"event.action": "__init__", "logrite.hand": hand})
            raise TypeError(msg)
        # split removes duplicate whitespaces so no need of strip
        if len(hand.split(" ")) != 5:
            msg = f"Hand should contain only 5 cards: {hand!r}"
            raise ValueError(msg)
        self._hand = hand
        logger.debug("__init__(self=%s,hand=%s): self._hand → %s", self, hand, self._hand, extra={"event.action": "__init__", "logrite.hand": hand})
        self._first_pair = 0
        logger.debug("__init__(self=%s,hand=%s): self._first_pair → %s", self, hand, self._first_pair, extra={"event.action": "__init__", "logrite.hand": hand})
        self._second_pair = 0
        logger.debug("__init__(self=%s,hand=%s): self._second_pair → %s", self, hand, self._second_pair, extra={"event.action": "__init__", "logrite.hand": hand})
        self._card_values, self._card_suit = self._internal_state()
        logger.warning("<<< Exiting __init__(hand=%s)", hand, extra={"event.action": "__init__", "logrite.hand": hand})
        self._hand_type = self._get_hand_type()
        logger.error("__init__(hand=%s): self._hand_type → %s", hand, self._hand_type, extra={"event.action": "__init__", "logrite.hand": hand})
        self._high_card = self._card_values[0]
        logger.debug("__init__(self=%s,hand=%s): self._high_card → %s", self, hand, self._high_card, extra={"event.action": "__init__", "logrite.hand": hand})

    @property
    def hand(self):
        """Returns the self hand"""
        logger.error(">>> Entering hand()", extra={"event.action": "hand"})
        logger.warning("<<< Exiting hand()", extra={"event.action": "hand"})
        return self._hand

    def compare_with(self, other: PokerHand) -> str:
        """
        Determines the outcome of comparing self hand with other hand.
        Returns the output as 'Win', 'Loss', 'Tie' according to the rules of
        Texas Hold'em.

        Here are some examples:
        >>> player = PokerHand("2H 3H 4H 5H 6H")  # Stright flush
        >>> opponent = PokerHand("KS AS TS QS JS")  # Royal flush
        >>> player.compare_with(opponent)
        'Loss'

        >>> player = PokerHand("2S AH 2H AS AC")  # Full house
        >>> opponent = PokerHand("2H 3H 5H 6H 7H")  # Flush
        >>> player.compare_with(opponent)
        'Win'

        >>> player = PokerHand("2S AH 4H 5S 6C")  # High card
        >>> opponent = PokerHand("AD 4C 5H 6H 2C")  # High card
        >>> player.compare_with(opponent)
        'Tie'
        """
        logger.error(">>> Entering compare_with(other=%s)", other, extra={"event.action": "compare_with", "logrite.other": other})
        # Breaking the tie works on the following order of precedence:
        # 1. First pair (default 0)
        # 2. Second pair (default 0)
        # 3. Compare all cards in reverse order because they are sorted.

        # First pair and second pair will only be a non-zero value if the card
        # type is either from the following:
        # 21: Four of a kind
        # 20: Full house
        # 17: Three of a kind
        # 16: Two pairs
        # 15: One pair
        if self._hand_type > other._hand_type:
            return "Win"
        elif self._hand_type < other._hand_type:
            return "Loss"
        elif self._first_pair == other._first_pair:
            if self._second_pair == other._second_pair:
                return self._compare_cards(other)
            else:
                return "Win" if self._second_pair > other._second_pair else "Loss"
        logger.warning("<<< Exiting compare_with(other=%s)", other, extra={"event.action": "compare_with", "logrite.other": other})
        return "Win" if self._first_pair > other._first_pair else "Loss"

    # This function is not part of the problem, I did it just for fun
    def hand_name(self) -> str:
        """
        Return the name of the hand in the following format:
        'hand name, high card'

        Here are some examples:
        >>> PokerHand("KS AS TS QS JS").hand_name()
        'Royal flush'

        >>> PokerHand("2D 6D 3D 4D 5D").hand_name()
        'Straight flush, Six-high'

        >>> PokerHand("JC 6H JS JD JH").hand_name()
        'Four of a kind, Jacks'

        >>> PokerHand("3D 2H 3H 2C 2D").hand_name()
        'Full house, Twos over Threes'

        >>> PokerHand("2H 4D 3C AS 5S").hand_name()  # Low ace
        'Straight, Five-high'

        Source: https://en.wikipedia.org/wiki/List_of_poker_hands
        """
        logger.error(">>> Entering hand_name()", extra={"event.action": "hand_name"})
        name = PokerHand._HAND_NAME[self._hand_type - 14]
        logger.error("hand_name(): name → %s", name, extra={"event.action": "hand_name"})
        high = PokerHand._CARD_NAME[self._high_card]
        pair1 = PokerHand._CARD_NAME[self._first_pair]
        pair2 = PokerHand._CARD_NAME[self._second_pair]
        if self._hand_type in [22, 19, 18]:
            return name + f", {high}-high"
        elif self._hand_type in [21, 17, 15]:
            return name + f", {pair1}s"
        elif self._hand_type in [20, 16]:
            join = "over" if self._hand_type == 20 else "and"
            logger.error("hand_name(): join → %s", join, extra={"event.action": "hand_name"})
            return name + f", {pair1}s {join} {pair2}s"
        elif self._hand_type == 23:
            return name
        else:
            logger.warning("<<< Exiting hand_name()", extra={"event.action": "hand_name"})
            return name + f", {high}"

    def _compare_cards(self, other: PokerHand) -> str:
        logger.error(">>> Entering _compare_cards(other=%s)", other, extra={"event.action": "_compare_cards", "logrite.other": other})
        # Enumerate gives us the index as well as the element of a list
        for index, card_value in enumerate(self._card_values):
            if card_value != other._card_values[index]:
                return "Win" if card_value > other._card_values[index] else "Loss"
        logger.warning("<<< Exiting _compare_cards(other=%s)", other, extra={"event.action": "_compare_cards", "logrite.other": other})
        return "Tie"

    def _get_hand_type(self) -> int:
        logger.error(">>> Entering _get_hand_type()", extra={"event.action": "_get_hand_type"})
        # Number representing the type of hand internally:
        # 23: Royal flush
        # 22: Straight flush
        # 21: Four of a kind
        # 20: Full house
        # 19: Flush
        # 18: Straight
        # 17: Three of a kind
        # 16: Two pairs
        # 15: One pair
        # 14: High card
        if self._is_flush():
            if self._is_five_high_straight() or self._is_straight():
                return 23 if sum(self._card_values) == 60 else 22
            return 19
        elif self._is_five_high_straight() or self._is_straight():
            return 18
        logger.warning("<<< Exiting _get_hand_type()", extra={"event.action": "_get_hand_type"})
        return 14 + self._is_same_kind()

    def _is_flush(self) -> bool:
        logger.error(">>> Entering _is_flush()", extra={"event.action": "_is_flush"})
        logger.warning("<<< Exiting _is_flush()", extra={"event.action": "_is_flush"})
        return len(self._card_suit) == 1

    def _is_five_high_straight(self) -> bool:
        logger.error(">>> Entering _is_five_high_straight()", extra={"event.action": "_is_five_high_straight"})
        # If a card is a five high straight (low ace) change the location of
        # ace from the start of the list to the end. Check whether the first
        # element is ace or not. (Don't want to change again)
        # Five high straight (low ace): AH 2H 3S 4C 5D
        # Why use sorted here? One call to this function will mutate the list to
        # [5, 4, 3, 2, 14] and so for subsequent calls (which will be rare) we
        # need to compare the sorted version.
        # Refer test_multiple_calls_five_high_straight in test_poker_hand.py
        if sorted(self._card_values) == [2, 3, 4, 5, 14]:
            if self._card_values[0] == 14:
                # Remember, our list is sorted in reverse order
                ace_card = self._card_values.pop(0)
                logger.error("_is_five_high_straight(): ace_card → %s", ace_card, extra={"event.action": "_is_five_high_straight"})
                self._card_values.append(ace_card)
            return True
        logger.warning("<<< Exiting _is_five_high_straight()", extra={"event.action": "_is_five_high_straight"})
        return False

    def _is_straight(self) -> bool:
        logger.error(">>> Entering _is_straight()", extra={"event.action": "_is_straight"})
        for i in range(4):
            if self._card_values[i] - self._card_values[i + 1] != 1:
                return False
        logger.warning("<<< Exiting _is_straight()", extra={"event.action": "_is_straight"})
        return True

    def _is_same_kind(self) -> int:
        logger.error(">>> Entering _is_same_kind()", extra={"event.action": "_is_same_kind"})
        # Kind Values for internal use:
        # 7: Four of a kind
        # 6: Full house
        # 3: Three of a kind
        # 2: Two pairs
        # 1: One pair
        # 0: False
        kind = val1 = val2 = 0
        for i in range(4):
            # Compare two cards at a time, if they are same increase 'kind',
            # add the value of the card to val1, if it is repeating again we
            # will add 2 to 'kind' as there are now 3 cards with same value.
            # If we get card of different value than val1, we will do the same
            # thing with val2
            if self._card_values[i] == self._card_values[i + 1]:
                if not val1:
                    val1 = self._card_values[i]
                    kind += 1
                elif val1 == self._card_values[i]:
                    kind += 2
                elif not val2:
                    val2 = self._card_values[i]
                    kind += 1
                elif val2 == self._card_values[i]:
                    kind += 2
        # For consistency in hand type (look at note in _get_hand_type function)
        kind = kind + 2 if kind in [4, 5] else kind
        # first meaning first pair to compare in 'compare_with'
        first = max(val1, val2)
        logger.error("_is_same_kind(): first → %s", first, extra={"event.action": "_is_same_kind"})
        second = min(val1, val2)
        logger.error("_is_same_kind(): second → %s", second, extra={"event.action": "_is_same_kind"})
        # If it's full house (three count pair + two count pair), make sure
        # first pair is three count and if not then switch them both.
        if kind == 6 and self._card_values.count(first) != 3:
            first, second = second, first
        self._first_pair = first
        logger.debug("_is_same_kind(self=%s): self._first_pair → %s", self, self._first_pair, extra={"event.action": "_is_same_kind"})
        self._second_pair = second
        logger.debug("_is_same_kind(self=%s): self._second_pair → %s", self, self._second_pair, extra={"event.action": "_is_same_kind"})
        logger.warning("<<< Exiting _is_same_kind()", extra={"event.action": "_is_same_kind"})
        return kind

    def _internal_state(self) -> tuple[list[int], set[str]]:
        logger.error(">>> Entering _internal_state()", extra={"event.action": "_internal_state"})
        # Internal representation of hand as a list of card values and
        # a set of card suit
        trans: dict = {"T": "10", "J": "11", "Q": "12", "K": "13", "A": "14"}
        logger.error("_internal_state(): trans → %s", trans, extra={"event.action": "_internal_state"})
        new_hand = self._hand.translate(str.maketrans(trans)).split()
        logger.error("_internal_state(): new_hand → %s", new_hand, extra={"event.action": "_internal_state"})
        card_values = [int(card[:-1]) for card in new_hand]
        logger.error("_internal_state(): card_values → %s", card_values, extra={"event.action": "_internal_state"})
        card_suit = {card[-1] for card in new_hand}
        logger.warning("<<< Exiting _internal_state()", extra={"event.action": "_internal_state"})
        return sorted(card_values, reverse=True), card_suit

    def __repr__(self):
        logger.error(">>> Entering __repr__()", extra={"event.action": "__repr__"})
        logger.warning("<<< Exiting __repr__()", extra={"event.action": "__repr__"})
        return f'{self.__class__}("{self._hand}")'

    def __str__(self):
        logger.error(">>> Entering __str__()", extra={"event.action": "__str__"})
        logger.warning("<<< Exiting __str__()", extra={"event.action": "__str__"})
        return self._hand

    # Rich comparison operators (used in list.sort() and sorted() builtin functions)
    # Note that this is not part of the problem but another extra feature where
    # if you have a list of PokerHand objects, you can sort them just through
    # the builtin functions.
    def __eq__(self, other):
        logger.error(">>> Entering __eq__(other=%s)", other, extra={"event.action": "__eq__", "logrite.other": other})
        if isinstance(other, PokerHand):
            return self.compare_with(other) == "Tie"
        logger.warning("<<< Exiting __eq__(other=%s)", other, extra={"event.action": "__eq__", "logrite.other": other})
        return NotImplemented

    def __lt__(self, other):
        logger.error(">>> Entering __lt__(other=%s)", other, extra={"event.action": "__lt__", "logrite.other": other})
        if isinstance(other, PokerHand):
            return self.compare_with(other) == "Loss"
        logger.warning("<<< Exiting __lt__(other=%s)", other, extra={"event.action": "__lt__", "logrite.other": other})
        return NotImplemented

    def __le__(self, other):
        logger.error(">>> Entering __le__(other=%s)", other, extra={"event.action": "__le__", "logrite.other": other})
        if isinstance(other, PokerHand):
            return self < other or self == other
        logger.warning("<<< Exiting __le__(other=%s)", other, extra={"event.action": "__le__", "logrite.other": other})
        return NotImplemented

    def __gt__(self, other):
        logger.error(">>> Entering __gt__(other=%s)", other, extra={"event.action": "__gt__", "logrite.other": other})
        if isinstance(other, PokerHand):
            return not self < other and self != other
        logger.warning("<<< Exiting __gt__(other=%s)", other, extra={"event.action": "__gt__", "logrite.other": other})
        return NotImplemented

    def __ge__(self, other):
        logger.error(">>> Entering __ge__(other=%s)", other, extra={"event.action": "__ge__", "logrite.other": other})
        if isinstance(other, PokerHand):
            return not self < other
        logger.warning("<<< Exiting __ge__(other=%s)", other, extra={"event.action": "__ge__", "logrite.other": other})
        return NotImplemented

    def __hash__(self):
        logger.error(">>> Entering __hash__()", extra={"event.action": "__hash__"})
        logger.warning("<<< Exiting __hash__()", extra={"event.action": "__hash__"})
        return object.__hash__(self)


def solution() -> int:
    logger.error(">>> Entering solution()", extra={"event.action": "solution"})
    # Solution for problem number 54 from Project Euler
    # Input from poker_hands.txt file
    answer = 0
    script_dir = os.path.abspath(os.path.dirname(__file__))
    logger.error("solution(): script_dir → %s", script_dir, extra={"event.action": "solution"})
    poker_hands = os.path.join(script_dir, "poker_hands.txt")
    logger.error("solution(): poker_hands → %s", poker_hands, extra={"event.action": "solution"})
    with open(poker_hands) as file_hand:
        for line in file_hand:
            player_hand = line[:14].strip()
            logger.error("solution(): player_hand → %s", player_hand, extra={"event.action": "solution"})
            opponent_hand = line[15:].strip()
            logger.error("solution(): opponent_hand → %s", opponent_hand, extra={"event.action": "solution"})
            player, opponent = PokerHand(player_hand), PokerHand(opponent_hand)
            output = player.compare_with(opponent)
            logger.error("solution(): output → %s", output, extra={"event.action": "solution"})
            if output == "Win":
                answer += 1
    logger.warning("<<< Exiting solution()", extra={"event.action": "solution"})
    return answer


if __name__ == "__main__":
    solution()
