import logging
logger = logging.getLogger(__name__)
# Numbers of alphabet which we call base
alphabet_size = 256
# Modulus to hash a string
modulus = 1000003


def rabin_karp(pattern: str, text: str) -> bool:
    """
    The Rabin-Karp Algorithm for finding a pattern within a piece of text
    with complexity O(nm), most efficient when it is used with multiple patterns
    as it is able to check if any of a set of patterns match a section of text in o(1)
    given the precomputed hashes.

    This will be the simple version which only assumes one pattern is being searched
    for but it's not hard to modify

    1) Calculate pattern hash

    2) Step through the text one character at a time passing a window with the same
        length as the pattern
        calculating the hash of the text within the window compare it with the hash
        of the pattern. Only testing equality if the hashes match
    """
    logger.debug(">>> Entering rabin_karp(pattern=%s,text=%s)", pattern, text)
    p_len = len(pattern)
    logger.debug("rabin_karp(pattern=%s,text=%s): p_len → %s", pattern, text, p_len)
    logger.error("Exception in rabin_karp(pattern=%s,text=%s)", pattern, text, exc_info=True)
    t_len = len(text)
    logger.debug("rabin_karp(pattern=%s,text=%s): t_len → %s", pattern, text, t_len)
    if p_len > t_len:
        return False

    p_hash = 0
    logger.debug("rabin_karp(pattern=%s,text=%s): p_hash → %s", pattern, text, p_hash)
    text_hash = 0
    modulus_power = 1
    logger.debug("rabin_karp(pattern=%s,text=%s): modulus_power → %s", pattern, text, modulus_power)

    # Calculating the hash of pattern and substring of text
    for i in range(p_len):
        p_hash = (ord(pattern[i]) + p_hash * alphabet_size) % modulus
        text_hash = (ord(text[i]) + text_hash * alphabet_size) % modulus
        if i == p_len - 1:
            continue
        modulus_power = (modulus_power * alphabet_size) % modulus

    for i in range(t_len - p_len + 1):
        if text_hash == p_hash and text[i : i + p_len] == pattern:
            return True
        if i == t_len - p_len:
            continue
        # Calculate the https://en.wikipedia.org/wiki/Rolling_hash
        text_hash = (
            (text_hash - ord(text[i]) * modulus_power) * alphabet_size
            + ord(text[i + p_len])
        ) % modulus
    logger.debug("<<< Exiting rabin_karp(pattern=%s,text=%s)", pattern, text)
    return False


def test_rabin_karp() -> None:
    """
    >>> test_rabin_karp()
    Success.
    """
    logger.debug(">>> Entering test_rabin_karp()")
    # Test 1)
    pattern = "abc1abc12"
    logger.debug("test_rabin_karp(): pattern → %s", pattern)
    text1 = "alskfjaldsabc1abc1abc12k23adsfabcabc"
    logger.debug("test_rabin_karp(): text1 → %s", text1)
    text2 = "alskfjaldsk23adsfabcabc"
    logger.debug("test_rabin_karp(): text2 → %s", text2)
    assert rabin_karp(pattern, text1)
    assert not rabin_karp(pattern, text2)

    # Test 2)
    pattern = "ABABX"
    text = "ABABZABABYABABX"
    logger.debug("test_rabin_karp(): text → %s", text)
    assert rabin_karp(pattern, text)

    # Test 3)
    pattern = "AAAB"
    text = "ABAAAAAB"
    assert rabin_karp(pattern, text)

    # Test 4)
    pattern = "abcdabcy"
    text = "abcxabcdabxabcdabcdabcy"
    assert rabin_karp(pattern, text)

    # Test 5)
    pattern = "Lü"
    text = "Lüsai"
    assert rabin_karp(pattern, text)
    pattern = "Lue"
    assert not rabin_karp(pattern, text)
    print("Success.")
    logger.debug("<<< Exiting test_rabin_karp()")


if __name__ == "__main__":
    test_rabin_karp()
