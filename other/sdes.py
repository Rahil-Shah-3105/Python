import logging
logger = logging.getLogger(__name__)
def apply_table(inp, table):
    """
    >>> apply_table("0123456789", list(range(10)))
    '9012345678'
    >>> apply_table("0123456789", list(range(9, -1, -1)))
    '8765432109'
    """
    logger.error(">>> Entering apply_table(inp=%s,table=%s)", inp, table, extra={"event.action": "apply_table", "logrite.inp": inp, "logrite.table": table})
    res = ""
    logger.error("apply_table(inp=%s,table=%s): res → %s", inp, table, res, extra={"event.action": "apply_table", "logrite.inp": inp, "logrite.table": table})
    for i in table:
        res += inp[i - 1]
    logger.warning("<<< Exiting apply_table(inp=%s,table=%s)", inp, table, extra={"event.action": "apply_table", "logrite.inp": inp, "logrite.table": table})
    return res


def left_shift(data):
    """
    >>> left_shift("0123456789")
    '1234567890'
    """
    logger.error(">>> Entering left_shift(data=%s)", data, extra={"event.action": "left_shift"})
    logger.warning("<<< Exiting left_shift(data=%s)", data, extra={"event.action": "left_shift"})
    return data[1:] + data[0]


def xor(a, b):
    """
    >>> xor("01010101", "00001111")
    '01011010'
    """
    logger.error(">>> Entering xor(a=%s,b=%s)", a, b, extra={"event.action": "xor", "logrite.a": a, "logrite.b": b})
    res = ""
    logger.error("xor(a=%s,b=%s): res → %s", a, b, res, extra={"event.action": "xor", "logrite.a": a, "logrite.b": b})
    for i in range(len(a)):
        if a[i] == b[i]:
            res += "0"
        else:
            res += "1"
    logger.warning("<<< Exiting xor(a=%s,b=%s)", a, b, extra={"event.action": "xor", "logrite.a": a, "logrite.b": b})
    return res


def apply_sbox(s, data):
    logger.error(">>> Entering apply_sbox(s=%s,data=%s)", s, data, extra={"event.action": "apply_sbox", "logrite.s": s})
    row = int("0b" + data[0] + data[-1], 2)
    logger.error("apply_sbox(s=%s,data=%s): row → %s", s, data, row, extra={"event.action": "apply_sbox", "logrite.s": s})
    col = int("0b" + data[1:3], 2)
    logger.error("apply_sbox(s=%s,data=%s): col → %s", s, data, col, extra={"event.action": "apply_sbox", "logrite.s": s})
    logger.warning("<<< Exiting apply_sbox(s=%s,data=%s)", s, data, extra={"event.action": "apply_sbox", "logrite.s": s})
    return bin(s[row][col])[2:]


def function(expansion, s0, s1, key, message):
    logger.error(">>> Entering function(expansion=%s,s0=%s,s1=%s,key=%s,message=%s)", expansion, s0, s1, key, message, extra={"event.action": "function", "logrite.expansion": expansion, "logrite.s0": s0, "logrite.s1": s1, "logrite.key": key, "logrite.message": message})
    left = message[:4]
    right = message[4:]
    temp = apply_table(right, expansion)
    temp = xor(temp, key)
    left_bin_str = apply_sbox(s0, temp[:4])
    right_bin_str = apply_sbox(s1, temp[4:])
    left_bin_str = "0" * (2 - len(left_bin_str)) + left_bin_str
    logger.error("function(expansion=%s,s0=%s,s1=%s,key=%s,message=%s): left_bin_str → %s", expansion, s0, s1, key, message, left_bin_str, extra={"event.action": "function", "logrite.expansion": expansion, "logrite.s0": s0, "logrite.s1": s1, "logrite.key": key, "logrite.message": message})
    right_bin_str = "0" * (2 - len(right_bin_str)) + right_bin_str
    logger.error("function(expansion=%s,s0=%s,s1=%s,key=%s,message=%s): right_bin_str → %s", expansion, s0, s1, key, message, right_bin_str, extra={"event.action": "function", "logrite.expansion": expansion, "logrite.s0": s0, "logrite.s1": s1, "logrite.key": key, "logrite.message": message})
    temp = apply_table(left_bin_str + right_bin_str, p4_table)
    temp = xor(left, temp)
    logger.warning("<<< Exiting function(expansion=%s,s0=%s,s1=%s,key=%s,message=%s)", expansion, s0, s1, key, message, extra={"event.action": "function", "logrite.expansion": expansion, "logrite.s0": s0, "logrite.s1": s1, "logrite.key": key, "logrite.message": message})
    return temp + right


if __name__ == "__main__":
    key = input("Enter 10 bit key: ")
    message = input("Enter 8 bit message: ")

    p8_table = [6, 3, 7, 4, 8, 5, 10, 9]
    p10_table = [3, 5, 2, 7, 4, 10, 1, 9, 8, 6]
    p4_table = [2, 4, 3, 1]
    IP = [2, 6, 3, 1, 4, 8, 5, 7]
    IP_inv = [4, 1, 3, 5, 7, 2, 8, 6]
    expansion = [4, 1, 2, 3, 2, 3, 4, 1]
    s0 = [[1, 0, 3, 2], [3, 2, 1, 0], [0, 2, 1, 3], [3, 1, 3, 2]]
    s1 = [[0, 1, 2, 3], [2, 0, 1, 3], [3, 0, 1, 0], [2, 1, 0, 3]]

    # key generation
    temp = apply_table(key, p10_table)
    left = temp[:5]
    right = temp[5:]
    left = left_shift(left)
    right = left_shift(right)
    key1 = apply_table(left + right, p8_table)
    left = left_shift(left)
    right = left_shift(right)
    left = left_shift(left)
    right = left_shift(right)
    key2 = apply_table(left + right, p8_table)

    # encryption
    temp = apply_table(message, IP)
    temp = function(expansion, s0, s1, key1, temp)
    temp = temp[4:] + temp[:4]
    temp = function(expansion, s0, s1, key2, temp)
    CT = apply_table(temp, IP_inv)
    print("Cipher text is:", CT)

    # decryption
    temp = apply_table(CT, IP)
    temp = function(expansion, s0, s1, key2, temp)
    temp = temp[4:] + temp[:4]
    temp = function(expansion, s0, s1, key1, temp)
    PT = apply_table(temp, IP_inv)
    print("Plain text after decypting is:", PT)
