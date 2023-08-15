"""
        author: Christian Bender
        date: 21.12.2017
        class: XORCipher

        This class implements the XOR-cipher algorithm and provides
        some useful methods for encrypting and decrypting strings and
        files.

        Overview about methods

        - encrypt : list of char
        - decrypt : list of char
        - encrypt_string : str
        - decrypt_string : str
        - encrypt_file : boolean
        - decrypt_file : boolean
"""
from __future__ import annotations








class XORCipher:
    def __init__(self, key: int = 0):
        """
        simple constructor that receives a key or uses
        default key = 0
        """

        # private field
        self.__key = key

    def encrypt(self, content: str, key: int) -> list[str]:
        """
        Encrypts the given string content with the XOR operation using the provided key.

        The key is first modulo 255 to ensure it's an appropriate size.
        For each character in the given content string,
        it calculates the XOR of the ASCII value of the character and the key,
        and converts the result back into a character.
        If key is not provided, it uses the key available in the constructor,
        and if that isn't available too, it defaults to 1.

        Args:
            content (str): The string contents to encrypt.
            key (int): The integer key to use for XOR encryption.

        Returns:
            list[str]: The encrypted content represented as a list of characters.

        Raises:
            AssertionError: If key isn't an int or content isn't a str.
        """
        # precondition
        assert isinstance(key, int) and isinstance(content, str)

        key = self.normalize_key(key)

        return self.apply_xor_operation(content, key)

    def decrypt(self, content: str, key: int) -> list[str]:
        """
        Decrypts a string of characters using XOR cipher.

        Args:
        content (str): The string to be decrypted.
        key (int): The key used for decryption; defaults to class key or 1.

        Returns:
        list[str]: A list of characters representing the decrypted string.
        """
        # Preconditions
        assert isinstance(key, int) and isinstance(content, str)

        key = self._get_valid_key(key)

        return [chr(ord(ch) ^ key) for ch in content]

    def normalize_key(self, key: int) -> int:
        """Ensures that key is within the acceptable range."""
        return (key or self.__key or 1) % 255

    def _get_valid_key(self, key: int) -> int:
        """Ensures the supplied key is non-zero and less than 255."""
        default_key = self.__key if hasattr(self, "__key") else 1
        return key or default_key % 255

    def apply_xor_operation(self, content: str, key: int) -> list[str]:
        """Applies XOR operation to the content using the key."""
        return [chr(ord(ch) ^ key) for ch in content]

    def encrypt_string(self, content: str, key: int = 0) -> str:
        """
        input: 'content' of type string and 'key' of type int
        output: encrypted string 'content'
        if key not passed the method uses the key by the constructor.
        otherwise key = 1
        """

        # precondition
        assert isinstance(key, int) and isinstance(content, str)

        key = key or self.__key or 1

        # make sure key can be any size
        while key > 255:
            key -= 255

        # This will be returned
        ans = ""

        for ch in content:
            ans += chr(ord(ch) ^ key)

        return ans

    def decrypt_string(self, content: str, key: int = 0) -> str:
        """
        input: 'content' of type string and 'key' of type int
        output: decrypted string 'content'
        if key not passed the method uses the key by the constructor.
        otherwise key = 1
        """

        # precondition
        assert isinstance(key, int) and isinstance(content, str)

        key = key or self.__key or 1

        # make sure key can be any size
        while key > 255:
            key -= 255

        # This will be returned
        ans = ""

        for ch in content:
            ans += chr(ord(ch) ^ key)

        return ans

    def encrypt_file(self, file: str, key: int = 0) -> bool:
        """
        input: filename (str) and a key (int)
        output: returns true if encrypt process was
        successful otherwise false
        if key not passed the method uses the key by the constructor.
        otherwise key = 1
        """

        # precondition
        assert isinstance(file, str) and isinstance(key, int)

        try:
            with open(file) as fin, open("encrypt.out", "w+") as fout:
                # actual encrypt-process
                for line in fin:
                    fout.write(self.encrypt_string(line, key))

        except OSError:
            return False

        return True

    def decrypt_file(self, file: str, key: int) -> bool:
        """
        input: filename (str) and a key (int)
        output: returns true if decrypt process was
        successful otherwise false
        if key not passed the method uses the key by the constructor.
        otherwise key = 1
        """

        # precondition
        assert isinstance(file, str) and isinstance(key, int)

        try:
            with open(file) as fin, open("decrypt.out", "w+") as fout:
                # actual encrypt-process
                for line in fin:
                    fout.write(self.decrypt_string(line, key))

        except OSError:
            return False

        return True


# Tests
# crypt = XORCipher()
# key = 67

# # test encrypt
# print(crypt.encrypt("hallo welt",key))
# # test decrypt
# print(crypt.decrypt(crypt.encrypt("hallo welt",key), key))

# # test encrypt_string
# print(crypt.encrypt_string("hallo welt",key))

# # test decrypt_string
# print(crypt.decrypt_string(crypt.encrypt_string("hallo welt",key),key))

# if (crypt.encrypt_file("test.txt",key)):
#       print("encrypt successful")
# else:
#       print("encrypt unsuccessful")

# if (crypt.decrypt_file("encrypt.out",key)):
#       print("decrypt successful")
# else:
#       print("decrypt unsuccessful")
