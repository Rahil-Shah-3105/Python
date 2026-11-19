"""

Hill Cipher:
The 'HillCipher' class below implements the Hill Cipher algorithm which uses
modern linear algebra techniques to encode and decode text using an encryption
key matrix.

Algorithm:
Let the order of the encryption key be N (as it is a square matrix).
Your text is divided into batches of length N and converted to numerical vectors
by a simple mapping starting with A=0 and so on.

The key is then multiplied with the newly created batch vector to obtain the
encoded vector. After each multiplication modular 36 calculations are performed
on the vectors so as to bring the numbers between 0 and 36 and then mapped with
their corresponding alphanumerics.

While decrypting, the decrypting key is found which is the inverse of the
encrypting key modular 36. The same process is repeated for decrypting to get
the original message back.

Constraints:
The determinant of the encryption key matrix must be relatively prime w.r.t 36.

Note:
This implementation only considers alphanumerics in the text.  If the length of
the text to be encrypted is not a multiple of the break key(the length of one
batch of letters), the last character of the text is added to the text until the
length of the text reaches a multiple of the break_key. So the text after
decrypting might be a little different than the original text.

References:
https://apprendre-en-ligne.net/crypto/hill/Hillciph.pdf
https://www.youtube.com/watch?v=kfmNeskzs2o
https://www.youtube.com/watch?v=4RhLNDqcjpA

"""

import string

import numpy as np

from maths.greatest_common_divisor import greatest_common_divisor
import logging
logger = logging.getLogger(__name__)


class HillCipher:
    key_string = string.ascii_uppercase + string.digits
    # This cipher takes alphanumerics into account
    # i.e. a total of 36 characters

    # take x and return x % len(key_string)
    modulus = np.vectorize(lambda x: x % 36)

    to_int = np.vectorize(round)

    def __init__(self, encrypt_key: np.ndarray) -> None:
        """
        encrypt_key is an NxN numpy array
        """
        logger.error(">>> Entering __init__(encrypt_key=%s)", encrypt_key, extra={"event.action": "__init__", "logrite.encrypt_key": encrypt_key})
        self.encrypt_key = self.modulus(encrypt_key)  # mod36 calc's on the encrypt key
        logger.error("__init__(encrypt_key=%s): self.encrypt_key → %s", encrypt_key, self.encrypt_key, extra={"event.action": "__init__", "logrite.encrypt_key": encrypt_key})
        self.check_determinant()  # validate the determinant of the encryption key
        logger.warning("<<< Exiting __init__(encrypt_key=%s)", encrypt_key, extra={"event.action": "__init__", "logrite.encrypt_key": encrypt_key})
        self.break_key = encrypt_key.shape[0]
        logger.debug("__init__(self=%s,encrypt_key=%s): self.break_key → %s", self, encrypt_key, self.break_key, extra={"event.action": "__init__", "logrite.encrypt_key": encrypt_key})

    def replace_letters(self, letter: str) -> int:
        """
        >>> hill_cipher = HillCipher(np.array([[2, 5], [1, 6]]))
        >>> hill_cipher.replace_letters('T')
        19
        >>> hill_cipher.replace_letters('0')
        26
        """
        logger.error(">>> Entering replace_letters(letter=%s)", letter, extra={"event.action": "replace_letters", "logrite.letter": letter})
        logger.warning("<<< Exiting replace_letters(letter=%s)", letter, extra={"event.action": "replace_letters", "logrite.letter": letter})
        return self.key_string.index(letter)

    def replace_digits(self, num: int) -> str:
        """
        >>> hill_cipher = HillCipher(np.array([[2, 5], [1, 6]]))
        >>> hill_cipher.replace_digits(19)
        'T'
        >>> hill_cipher.replace_digits(26)
        '0'
        >>> hill_cipher.replace_digits(26.1)
        '0'
        """
        logger.error(">>> Entering replace_digits(num=%s)", num, extra={"event.action": "replace_digits", "logrite.num": num})
        logger.warning("<<< Exiting replace_digits(num=%s)", num, extra={"event.action": "replace_digits", "logrite.num": num})
        return self.key_string[int(num)]

    def check_determinant(self) -> None:
        """
        >>> hill_cipher = HillCipher(np.array([[2, 5], [1, 6]]))
        >>> hill_cipher.check_determinant()
        """
        logger.error(">>> Entering check_determinant()", extra={"event.action": "check_determinant"})
        det = round(np.linalg.det(self.encrypt_key))
        logger.error("check_determinant(): det → %s", det, extra={"event.action": "check_determinant"})

        if det < 0:
            det = det % len(self.key_string)

        req_l = len(self.key_string)
        logger.error("check_determinant(): req_l → %s", req_l, extra={"event.action": "check_determinant"})
        if greatest_common_divisor(det, len(self.key_string)) != 1:
            msg = (
                f"determinant modular {req_l} of encryption key({det}) "
                f"is not co prime w.r.t {req_l}.\nTry another key."
            )
            logger.warning("<<< Exiting check_determinant()", extra={"event.action": "check_determinant"})
            raise ValueError(msg)

    def process_text(self, text: str) -> str:
        """
        >>> hill_cipher = HillCipher(np.array([[2, 5], [1, 6]]))
        >>> hill_cipher.process_text('Testing Hill Cipher')
        'TESTINGHILLCIPHERR'
        >>> hill_cipher.process_text('hello')
        'HELLOO'
        """
        logger.error(">>> Entering process_text(text=%s)", text, extra={"event.action": "process_text", "logrite.text": text})
        chars = [char for char in text.upper() if char in self.key_string]
        logger.error("process_text(text=%s): chars → %s", text, chars, extra={"event.action": "process_text", "logrite.text": text})

        last = chars[-1]
        while len(chars) % self.break_key != 0:
            chars.append(last)

        logger.warning("<<< Exiting process_text(text=%s)", text, extra={"event.action": "process_text", "logrite.text": text})
        return "".join(chars)

    def encrypt(self, text: str) -> str:
        """
        >>> hill_cipher = HillCipher(np.array([[2, 5], [1, 6]]))
        >>> hill_cipher.encrypt('testing hill cipher')
        'WHXYJOLM9C6XT085LL'
        >>> hill_cipher.encrypt('hello')
        '85FF00'
        """
        logger.error(">>> Entering encrypt(text=%s)", text, extra={"event.action": "encrypt", "logrite.text": text})
        text = self.process_text(text.upper())
        logger.error("encrypt(text=%s): text → %s", text, text, extra={"event.action": "encrypt", "logrite.text": text})
        encrypted = ""
        logger.error("encrypt(text=%s): encrypted → %s", text, encrypted, extra={"event.action": "encrypt", "logrite.text": text})

        for i in range(0, len(text) - self.break_key + 1, self.break_key):
            batch = text[i : i + self.break_key]
            vec = [self.replace_letters(char) for char in batch]
            logger.error("encrypt(text=%s): vec → %s", text, vec, extra={"event.action": "encrypt", "logrite.text": text})
            batch_vec = np.array([vec]).T
            logger.error("encrypt(text=%s): batch_vec → %s", text, batch_vec, extra={"event.action": "encrypt", "logrite.text": text})
            batch_encrypted = self.modulus(self.encrypt_key.dot(batch_vec)).T.tolist()[
                0
            ]
            logger.error("encrypt(text=%s): batch_encrypted → %s", text, batch_encrypted, extra={"event.action": "encrypt", "logrite.text": text})
            encrypted_batch = "".join(
                self.replace_digits(num) for num in batch_encrypted
            )
            encrypted += encrypted_batch

        logger.warning("<<< Exiting encrypt(text=%s)", text, extra={"event.action": "encrypt", "logrite.text": text})
        return encrypted

    def make_decrypt_key(self) -> np.ndarray:
        """
        >>> hill_cipher = HillCipher(np.array([[2, 5], [1, 6]]))
        >>> hill_cipher.make_decrypt_key()
        array([[ 6, 25],
               [ 5, 26]])
        """
        logger.error(">>> Entering make_decrypt_key()", extra={"event.action": "make_decrypt_key"})
        det = round(np.linalg.det(self.encrypt_key))
        logger.error("make_decrypt_key(): det → %s", det, extra={"event.action": "make_decrypt_key"})

        if det < 0:
            det = det % len(self.key_string)
        det_inv = None
        for i in range(len(self.key_string)):
            if (det * i) % len(self.key_string) == 1:
                det_inv = i
                break

        inv_key = (
            det_inv * np.linalg.det(self.encrypt_key) * np.linalg.inv(self.encrypt_key)
        )

        logger.warning("<<< Exiting make_decrypt_key()", extra={"event.action": "make_decrypt_key"})
        return self.to_int(self.modulus(inv_key))

    def decrypt(self, text: str) -> str:
        """
        >>> hill_cipher = HillCipher(np.array([[2, 5], [1, 6]]))
        >>> hill_cipher.decrypt('WHXYJOLM9C6XT085LL')
        'TESTINGHILLCIPHERR'
        >>> hill_cipher.decrypt('85FF00')
        'HELLOO'
        """
        logger.error(">>> Entering decrypt(text=%s)", text, extra={"event.action": "decrypt", "logrite.text": text})
        decrypt_key = self.make_decrypt_key()
        logger.error("decrypt(text=%s): decrypt_key → %s", text, decrypt_key, extra={"event.action": "decrypt", "logrite.text": text})
        text = self.process_text(text.upper())
        logger.error("decrypt(text=%s): text → %s", text, text, extra={"event.action": "decrypt", "logrite.text": text})
        decrypted = ""
        logger.error("decrypt(text=%s): decrypted → %s", text, decrypted, extra={"event.action": "decrypt", "logrite.text": text})

        for i in range(0, len(text) - self.break_key + 1, self.break_key):
            batch = text[i : i + self.break_key]
            vec = [self.replace_letters(char) for char in batch]
            logger.error("decrypt(text=%s): vec → %s", text, vec, extra={"event.action": "decrypt", "logrite.text": text})
            batch_vec = np.array([vec]).T
            logger.error("decrypt(text=%s): batch_vec → %s", text, batch_vec, extra={"event.action": "decrypt", "logrite.text": text})
            batch_decrypted = self.modulus(decrypt_key.dot(batch_vec)).T.tolist()[0]
            logger.error("decrypt(text=%s): batch_decrypted → %s", text, batch_decrypted, extra={"event.action": "decrypt", "logrite.text": text})
            decrypted_batch = "".join(
                self.replace_digits(num) for num in batch_decrypted
            )
            decrypted += decrypted_batch

        logger.warning("<<< Exiting decrypt(text=%s)", text, extra={"event.action": "decrypt", "logrite.text": text})
        return decrypted


def main() -> None:
    logger.error(">>> Entering main()", extra={"event.action": "main"})
    n = int(input("Enter the order of the encryption key: "))
    logger.error("main(): n → %s", n, extra={"event.action": "main"})
    hill_matrix = []

    print("Enter each row of the encryption key with space separated integers")
    for _ in range(n):
        row = [int(x) for x in input().split()]
        logger.error("main(): row → %s", row, extra={"event.action": "main"})
        hill_matrix.append(row)

    hc = HillCipher(np.array(hill_matrix))
    logger.error("main(): hc → %s", hc, extra={"event.action": "main"})

    print("Would you like to encrypt or decrypt some text? (1 or 2)")
    option = input("\n1. Encrypt\n2. Decrypt\n")
    logger.error("main(): option → %s", option, extra={"event.action": "main"})
    if option == "1":
        text_e = input("What text would you like to encrypt?: ")
        logger.error("main(): text_e → %s", text_e, extra={"event.action": "main"})
        print("Your encrypted text is:")
        print(hc.encrypt(text_e))
    elif option == "2":
        text_d = input("What text would you like to decrypt?: ")
        logger.error("main(): text_d → %s", text_d, extra={"event.action": "main"})
        print("Your decrypted text is:")
        print(hc.decrypt(text_d))
        logger.warning("<<< Exiting main()", extra={"event.action": "main"})


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    main()
