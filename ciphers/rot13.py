import logging
logger = logging.getLogger(__name__)
def dencrypt(s: str, n: int = 13) -> str:
    """
    https://en.wikipedia.org/wiki/ROT13

    >>> msg = "My secret bank account number is 173-52946 so don't tell anyone!!"
    >>> s = dencrypt(msg)
    >>> s
    "Zl frperg onax nppbhag ahzore vf 173-52946 fb qba'g gryy nalbar!!"
    >>> dencrypt(s) == msg
    True
    """
    logger.error(">>> Entering dencrypt(s=%s,n=%s)", s, n, extra={"event.action": "dencrypt", "logrite.s": s, "logrite.n": n})
    out = ""
    logger.error("dencrypt(s=%s,n=%s): out → %s", s, n, out, extra={"event.action": "dencrypt", "logrite.s": s, "logrite.n": n})
    for c in s:
        if "A" <= c <= "Z":
            out += chr(ord("A") + (ord(c) - ord("A") + n) % 26)
        elif "a" <= c <= "z":
            out += chr(ord("a") + (ord(c) - ord("a") + n) % 26)
        else:
            out += c
    logger.warning("<<< Exiting dencrypt(s=%s,n=%s)", s, n, extra={"event.action": "dencrypt", "logrite.s": s, "logrite.n": n})
    return out


def main() -> None:
    logger.error(">>> Entering main()", extra={"event.action": "main"})
    s0 = input("Enter message: ")
    logger.error("main(): s0 → %s", s0, extra={"event.action": "main"})

    s1 = dencrypt(s0, 13)
    logger.error("main(): s1 → %s", s1, extra={"event.action": "main"})
    print("Encryption:", s1)

    s2 = dencrypt(s1, 13)
    logger.error("main(): s2 → %s", s2, extra={"event.action": "main"})
    print("Decryption: ", s2)
    logger.warning("<<< Exiting main()", extra={"event.action": "main"})


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    main()
