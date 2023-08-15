LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def main() -> None:
    message = input("Enter message: ")
    key = input("Enter key [alphanumeric]: ")
    mode = input("Encrypt/Decrypt [e/d]: ")

    if mode.lower().startswith("e"):
        mode = "encrypt"
        translated = encrypt_message(key, message)
    elif mode.lower().startswith("d"):
        mode = "decrypt"
        translated = decrypt_message(key, message)

    print(f"\n{mode.title()}ed message:")
    print(translated)


def encrypt_message(key: str, message: str) -> str:
    """
    >>> encrypt_message('HDarji', 'This is Harshil Darji from Dharmaj.')
    'Akij ra Odrjqqs Gaisq muod Mphumrs.'
    """
    return translate_message(key, message, "encrypt")


def decrypt_message(key: str, message: str) -> str:
    """
    >>> decrypt_message('HDarji', 'Akij ra Odrjqqs Gaisq muod Mphumrs.')
    'This is Harshil Darji from Dharmaj.'
    """
    return translate_message(key, message, "decrypt")


def translate_message(key: str, message: str, mode: str) -> str:
    check_mode_valid(mode)

    translated = []
    key_index = 0
    key = key.upper()

    for symbol in message:
        num = LETTERS.find(symbol.upper())
        if num != -1:
            num = get_translated_num(num, LETTERS.find(key[key_index]), mode)

            translated.append(
                LETTERS[num] if symbol.isupper() else LETTERS[num].lower()
            )

            key_index = get_updated_key_index(key_index, key)
        else:
            translated.append(symbol)

    return "".join(translated)


if __name__ == "__main__":
    main()

def get_translated_num(num: int, num_key: int, mode: str) -> int:
    """Returns the translated number based on operation mode.

    Args:
        num (int): The ordinal value of the character.
        num_key (int): The ordinal value of the corresponding character in the key.
        mode (str): The mode of operation, either 'encrypt' or 'decrypt'.

    Returns:
        int: The translated numeral value.
    """
    num = num + num_key if mode == "encrypt" else num - num_key
    return num % len(LETTERS)


def get_updated_key_index(key_index: int, key: str) -> int:
    """Returns the updated key index.

    Args:
        key_index (int): The current key index.
        key (str): The key string used for the Caesar cipher.

    Returns:
        int: The updated key index.
    """
    key_index += 1
    return key_index if key_index != len(key) else 0
