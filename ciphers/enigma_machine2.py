"""
Wikipedia: https://en.wikipedia.org/wiki/Enigma_machine
Video explanation: https://youtu.be/QwQVMqfoB2E
Also check out Numberphile's and Computerphile's videos on this topic

This module contains function 'enigma' which emulates
the famous Enigma machine from WWII.
Module includes:
- enigma function
- showcase of function usage
- 9 randomly generated rotors
- reflector (aka static rotor)
- original alphabet

Created by TrapinchO
"""
from __future__ import annotations

RotorPositionT = tuple[int, int, int]
RotorSelectionT = tuple[str, str, str]


# used alphabet --------------------------
# from string.ascii_uppercase
abc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# -------------------------- default selection --------------------------
# rotors --------------------------
rotor1 = "EGZWVONAHDCLFQMSIPJBYUKXTR"
rotor2 = "FOBHMDKEXQNRAULPGSJVTYICZW"
rotor3 = "ZJXESIUQLHAVRMDOYGTNFWPBKC"
# reflector --------------------------
reflector = {
    "A": "N",
    "N": "A",
    "B": "O",
    "O": "B",
    "C": "P",
    "P": "C",
    "D": "Q",
    "Q": "D",
    "E": "R",
    "R": "E",
    "F": "S",
    "S": "F",
    "G": "T",
    "T": "G",
    "H": "U",
    "U": "H",
    "I": "V",
    "V": "I",
    "J": "W",
    "W": "J",
    "K": "X",
    "X": "K",
    "L": "Y",
    "Y": "L",
    "M": "Z",
    "Z": "M",
}

# -------------------------- extra rotors --------------------------
rotor4 = "RMDJXFUWGISLHVTCQNKYPBEZOA"
rotor5 = "SGLCPQWZHKXAREONTFBVIYJUDM"
rotor6 = "HVSICLTYKQUBXDWAJZOMFGPREN"
rotor7 = "RZWQHFMVDBKICJLNTUXAGYPSOE"
rotor8 = "LFKIJODBEGAMQPXVUHYSTCZRWN"
rotor9 = "KOAEGVDHXPQZMLFTYWJNBRCIUS"


def _validator(
    rotpos: RotorPositionT, rotsel: RotorSelectionT, pb: str
) -> tuple[RotorPositionT, RotorSelectionT, dict[str, str]]:
    """
    Checks if the values can be used for the 'enigma' function

    >>> _validator((1,1,1), (rotor1, rotor2, rotor3), 'POLAND')
    ((1, 1, 1), ('EGZWVONAHDCLFQMSIPJBYUKXTR', 'FOBHMDKEXQNRAULPGSJVTYICZW', \
'ZJXESIUQLHAVRMDOYGTNFWPBKC'), \
{'P': 'O', 'O': 'P', 'L': 'A', 'A': 'L', 'N': 'D', 'D': 'N'})

    :param rotpos: rotor_positon
    :param rotsel: rotor_selection
    :param pb: plugb -> validated and transformed
    :return: (rotpos, rotsel, pb)
    """
    # Checks if there are 3 unique rotors

    if (unique_rotsel := len(set(rotsel))) < 3:
        msg = f"Please use 3 unique rotors (not {unique_rotsel})"
        raise Exception(msg)

    # Checks if rotor positions are valid
    rotorpos1, rotorpos2, rotorpos3 = rotpos
    if not 0 < rotorpos1 <= len(abc):
        msg = f"First rotor position is not within range of 1..26 ({rotorpos1}"
        raise ValueError(msg)
    if not 0 < rotorpos2 <= len(abc):
        msg = f"Second rotor position is not within range of 1..26 ({rotorpos2})"
        raise ValueError(msg)
    if not 0 < rotorpos3 <= len(abc):
        msg = f"Third rotor position is not within range of 1..26 ({rotorpos3})"
        raise ValueError(msg)

    # Validates string and returns dict
    pbdict = _plugboard(pb)

    return rotpos, rotsel, pbdict

def _plugboard(pbstring: str) -> dict[str, str]:
    """
    Creates a dictionary mapping for the Enigma machine setting designed to scramble the input in a
    particular manner.

    More details can be found on: https://en.wikipedia.org/wiki/Enigma_machine#Plugboard

    Args:
        pbstring (str): A string input containing pairs of uppercase alphabets. Each pair is expected to be
                        unique and characters can be separated by spaces.

    Returns:
        dict: A dictionary mapping of the input string in the form of key-value pairs. Each pair is
              swapped and mapped to each other.

    Raises:
        TypeError: If the input `pbstring` is not of type string.
        Exception: If the length of the input `pbstring` is not even or it contains characters not in native
                   language alphabet set (only English uppercase alphabets allowed).
        Exception: In case of duplicate alphabets in the input `pbstring`.

    Examples:
        >>> _plugboard('PICTURES')
        {'P': 'I', 'I': 'P', 'C': 'T', 'T': 'C', 'U': 'R', 'R': 'U', 'E': 'S', 'S': 'E'}
        >>> _plugboard('POLAND')
        {'P': 'O', 'O': 'P', 'L': 'A', 'A': 'L', 'N': 'D', 'D': 'N'}
    """
    if not isinstance(pbstring, str):
        raise TypeError(f"Plugboard setting isn't type string ({type(pbstring)})")
    elif len(pbstring) % 2 != 0:
        raise Exception(f"Odd number of symbols ({len(pbstring)})")
    elif pbstring == "":
        return {}

    pbstring.replace(" ", "")
    tmppbl = set()
    for i in pbstring:
        if i not in abc:
            raise Exception(f"'{i}' not in list of symbols")
        elif i in tmppbl:
            raise Exception(f"Duplicate symbol ({i})")
        else:
            tmppbl.add(i)
    del tmppbl

    pb = {}
    for j in range(0, len(pbstring) - 1, 2):
        pb[pbstring[j]] = pbstring[j + 1]
        pb[pbstring[j + 1]] = pbstring[j]

    return pb

def enigma(
    text: str,
    rotor_position: RotorPositionT,
    rotor_selection: RotorSelectionT = (rotor1, rotor2, rotor3),
    plugb: str = "",
) -> str:
    """
    Encrypts or decrypts a given text using Enigma machine algorithm.

    This function is almost similar as real-world Enigma machine. This function accepted
    a given string and converted all characters to uppercase. Non-letter symbols are ignored.

    How it works:
    For each letter in the message:

    1. Input letter goes into the plugboard, if it is connected to another one, it switches.

    2. Letter goes through 3 rotors. Each rotor can be represented as 2 sets of symbol,
       where one is shuffled.

    3. Symbol then goes through reflector (static rotor). There it is switched with paired symbol

    4. Letter then goes through the rotors again.

    5. If the letter is connected to plugboard, it is switched.

    6. Return the letter

    Args:
        text (str): Input message in string format. The message that needs to be encrypted or decrypted
        rotor_position (RotorPositionT): A tuple with 3 values each in range 1..26 representing positions
                                         of selected rotors.
        rotor_selection (RotorSelectionT, optional): A tuple with 3 rotors. The selected rotors to be used
                                     for the encryption or decryption operation.
                                     Default to (rotor1, rotor2, rotor3).
        plugb (str, optional): String containing plugboard configuration,
                                    default is empty string.

    Returns:
        str: The encrypted or decrypted output as a single string.

    Examples:
        >>> enigma('Hello World!', (1, 2, 1), plugb='pictures')
        'KORYH JUHHI!'
        >>> enigma('KORYH, juhhi!', (1, 2, 1), plugb='pictures')
        'HELLO, WORLD!'
        >>> enigma('hello world!', (1, 1, 1), plugb='pictures')
        'FPNCZ QWOBU!'
        >>> enigma('FPNCZ QWOBU', (1, 1, 1), plugb='pictures')
        'HELLO WORLD'
    """


if __name__ == "__main__":
    message = "This is my Python script that emulates the Enigma machine from WWII."
    rotor_pos = (1, 1, 1)
    pb = "pictures"
    rotor_sel = (rotor2, rotor4, rotor8)
    en = enigma(message, rotor_pos, rotor_sel, pb)

    print("Encrypted message:", en)
    print("Decrypted message:", enigma(en, rotor_pos, rotor_sel, pb))
