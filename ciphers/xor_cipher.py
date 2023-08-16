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
        input: 'content' of type string and 'key' of type int
        output: encrypted string 'content' as a list of chars
        if key not passed the method uses the key by the constructor.
        otherwise key = 1
        """

        # precondition
        assert isinstance(key, int) and isinstance(content, str)

        key = key or self.__key or 1

        # make sure key is an appropriate size
        key %= 255

        return [chr(ord(ch) ^ key) for ch in content]

    def decrypt(self, content: str, key: int) -> list[str]:
        """
        Decrypt a given string content using XOR Cipher with a given key.

        The decryption process involves taking each character from the input string, converting
        it to its ASCII value, and then performing a bitwise XOR operation on it with the given key.

        The key is first checked to make sure it's of appropriate size - modulo 255 operation is performed.
        If no key is provided during decryption, it defaults to the key stored in the instance variable '__key'
        during object creation. If '__key' is also not set, it defaults to 1.

        Args:
            content (str): The content to be decrypted.
            key (int): The decryption key.

        Returns:
            list[str]: The decrypted content as a list of characters.

        Raises:
            AssertionError: If the key is not an integer or if the content is not a list.
        """
        assert isinstance(key, int) and isinstance(content, list)

        key = key or self.__key or 1
        key %= 255

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
