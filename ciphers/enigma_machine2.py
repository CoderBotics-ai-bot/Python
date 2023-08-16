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
    The only difference with real-world enigma is that I allowed string input.
    All characters are converted to uppercase. (non-letter symbol are ignored)
    How it works:
    (for every letter in the message)

    - Input letter goes into the plugboard.
    If it is connected to another one, switch it.

    - Letter goes through 3 rotors.
    Each rotor can be represented as 2 sets of symbol, where one is shuffled.
    Each symbol from the first set has corresponding symbol in
    the second set and vice versa.

    example:
    | ABCDEFGHIJKLMNOPQRSTUVWXYZ | e.g. F=D and D=F
    | VKLEPDBGRNWTFCJOHQAMUZYIXS |

    - Symbol then goes through reflector (static rotor).
    There it is switched with paired symbol
    The reflector can be represented as2 sets, each with half of the alphanet.
    There are usually 10 pairs of letters.

    Example:
    | ABCDEFGHIJKLM | e.g. E is paired to X
    | ZYXWVUTSRQPON | so when E goes in X goes out and vice versa

    - Letter then goes through the rotors again

    - If the letter is connected to plugboard, it is switched.

    - Return the letter

    >>> enigma('Hello World!', (1, 2, 1), plugb='pictures')
    'KORYH JUHHI!'
    >>> enigma('KORYH, juhhi!', (1, 2, 1), plugb='pictures')
    'HELLO, WORLD!'
    >>> enigma('hello world!', (1, 1, 1), plugb='pictures')
    'FPNCZ QWOBU!'
    >>> enigma('FPNCZ QWOBU', (1, 1, 1), plugb='pictures')
    'HELLO WORLD'


    :param text: input message
    :param rotor_position: tuple with 3 values in range 1..26
    :param rotor_selection: tuple with 3 rotors ()
    :param plugb: string containing plugboard configuration (default '')
    :return: en/decrypted string
    """

    text = text.upper()
    rotor_position, rotor_selection, plugboard = _validator(
        rotor_position, rotor_selection, plugb.upper()
    )

    rotorpos1, rotorpos2, rotorpos3 = rotor_position
    rotor1, rotor2, rotor3 = rotor_selection
    rotorpos1 -= 1
    rotorpos2 -= 1
    rotorpos3 -= 1

    result = []

    # encryption/decryption process --------------------------
    for symbol in text:
        if symbol in abc:
            # 1st plugboard --------------------------
            if symbol in plugboard:
                symbol = plugboard[symbol]

            # rotor ra --------------------------
            index = abc.index(symbol) + rotorpos1
            symbol = rotor1[index % len(abc)]

            # rotor rb --------------------------
            index = abc.index(symbol) + rotorpos2
            symbol = rotor2[index % len(abc)]

            # rotor rc --------------------------
            index = abc.index(symbol) + rotorpos3
            symbol = rotor3[index % len(abc)]

            # reflector --------------------------
            # this is the reason you don't need another machine to decipher

            symbol = reflector[symbol]

            # 2nd rotors
            symbol = abc[rotor3.index(symbol) - rotorpos3]
            symbol = abc[rotor2.index(symbol) - rotorpos2]
            symbol = abc[rotor1.index(symbol) - rotorpos1]

            # 2nd plugboard
            if symbol in plugboard:
                symbol = plugboard[symbol]

            # moves/resets rotor positions
            rotorpos1 += 1
            if rotorpos1 >= len(abc):
                rotorpos1 = 0
                rotorpos2 += 1
            if rotorpos2 >= len(abc):
                rotorpos2 = 0
                rotorpos3 += 1
            if rotorpos3 >= len(abc):
                rotorpos3 = 0

        # else:
        #    pass
        #    Error could be also raised
        #    raise ValueError(
        #       'Invalid symbol('+repr(symbol)+')')
        result.append(symbol)

    return "".join(result)


if __name__ == "__main__":
    message = "This is my Python script that emulates the Enigma machine from WWII."
    rotor_pos = (1, 1, 1)
    pb = "pictures"
    rotor_sel = (rotor2, rotor4, rotor8)
    en = enigma(message, rotor_pos, rotor_sel, pb)

    print("Encrypted message:", en)
    print("Decrypted message:", enigma(en, rotor_pos, rotor_sel, pb))
