import os
import json
import sys

from sympy import use

def GET_Enc_Table(name:str) -> dict:
    data = {}
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "CipherTable.json")) as file:
        data = json.load(file)

    return data[name]

def MAKE_Enc_Table() -> None:
    pheonix_3d_matrix_sbox = {}
    pheonix_3d_matrix_v1 = {}

    max_G = 10
    max_SG = 10
    max_C = 10

    done_keys = []
    done_values = []
    import random

    req = max_G*max_SG*max_C

    while req > 0:
        key = f"{random.randint(1, max_G)} {random.randint(1, max_SG)} {random.randint(1, max_C)}"
        if key in done_keys:
            continue
        else:
            value = f"{random.randint(1, max_G)} {random.randint(1, max_SG)} {random.randint(1, max_C)}"
            if value == key:
                continue
            elif value in done_values:
                continue
            else:
                done_keys.append(key)
                done_values.append(value)
                pheonix_3d_matrix_v1[key] = value

        req -= 1

    #Clear Space
    done_values = []
    done_keys = []

    used_values = set()

    for code_point in range(0x10FFFF):
        unicode_char = chr(code_point)

        # Find a random Unicode character that hasn't been used yet
        while True:
            random_char = chr(random.randint(0x0000, 0x10FFFF))
            if not random_char in used_values and random_char != unicode_char:
                break

        pheonix_3d_matrix_sbox[unicode_char] = random_char
        used_values.add(random_char)

    used_values = set()

    pheonix_3d_matrix_sbox = {k: v for k, v in pheonix_3d_matrix_sbox.items() if v}

    table = {
        "pheonix_3d_matrix_v1": pheonix_3d_matrix_v1,
        "pheonix_3d_matrix_sbox": pheonix_3d_matrix_sbox
    }

    pheonix_3d_matrix_sbox = {}
    pheonix_3d_matrix_v1 = {}

    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "CipherTable.json"), "w") as file:
        json.dump(table, file)
        file.close()

    table = {}

def MakeDEFMAPS() -> None:
    ENCMAPS_DATA = {
        "PSntx_H1": {
            "a": "e",
            "b": "@",
            "c": "%",
            "d": "!",
            "e": "&",
            "f": "b",
            "g": "/",
            "h": "g",
            "i": "d",
            "j": "^",
            "k": "1",
            "l": "6",
            "m": "7",
            "n": "~",
            "o": ")",
            "p": "9",
            "q": "(",
            "r": "*",
            "s": "`",
            "t": "V",
            "u": "P",
            "v": "E",
            "w": "'",
            "x": "<",
            "y": ">",
            "z": ","
        },
        "pheonix_utx": {
                "a": "!",
                "b": "#",
                "c": "%",
                "d": "&",
                "e": "(",
                "f": "@",
                "g": "$",
                "h": "^",
                "i": "*",
                "j": ")",
                "k": "-",
                "l": "=",
                "m": "_",
                "n": "+",
                "o": "{",
                "p": "]",
                "q": "[",
                "r": "}",
                "s": "|",
                "t": ":",
                "u": "\"",
                "v": ";",
                "w": "'",
                "x": "<",
                "y": ".",
                "z": ",",
                "1": "D",
                "2": "J",
                "3": "G",
                "4": "P",
                "5": "A",
                "6": "b",
                "7": "B",
                "8": "F",
                "9": "X",
                "0": "Z",
                ".": "/",
                ",": "?",
                "?": "1",
                "|": "2",
                ":": "3",
                ";": "4",
                "/": "5",
                "\"": "6",
                "'": "7",
                "<": "8",
                ">": "9",
                "&": "0",
                " ": "~",
                "@": "`"
        },

        "hype_space": {
            "A": "+", "B": "-", "C": "@", "D": "*", "E": "(", "F": ")", "G": "\"", "H": "\"", "I": "/", "J": "\\", "K": ".", "L": ",", "M": "~",
            "N": "4", "O": "3", "P": "2", "Q": "1", "R": "0", "S": "9", "T": "8", "U": "7", "V": "6", "W": "5", "X": "^", "Y": "A", "Z": "B",
            "a": "C", "b": "D", "c": "E", "d": "K", "e": "J", "f": "L", "g": "N", "h": "I", "i": "Q", "j": "S", "k": "R", "l": "U", "m": "T",
            "n": "Y", "o": "X", "p": "W", "q": "V", "r": "Z", "s": "F", "t": "G", "u": "H", "v": "M", "w": "O", "x": "P", "y": "a", "z": "b",
            "+": "c", "-": "d", "@": "e", "*": "f", "(": "g", ")": "h", "'": "i", "\"": "j", "/": "k", "\\": "l", ".": "m", ",": "n", "&": "`",
            "#": "$", "$": "&", "%": "!", "!": "%", "{": "}", "}": "{", ":": ";", ";": ":", "<": "?", "?": "<", ">": " ", "[": "]", "]": "[",
            "|": "#", " ": "o", "1": "p", "2": "q", "3": "r", "4": "s", "5": "t", "6": "u", "7": "v", "8": "w", "9": "x", "0": "y", "~": "z",
            "`": "_", "_": "=", "=": "|", "^": ">"
        },

        "hype_space_bin": {"A": "00101011", "B": "00101101", "C": "01000000", "D": "00101010", "E": "00101000", "F": "00101001", "G": "00100111", "H": "00100010", "I": "00101111", "J": "01011100", "K": "00101110", "L": "00101100", "M": "01111110", "N": "00110100", "O": "00110011", "P": "00110010", "Q": "00110001", "R": "00110000", "S": "00111001", "T": "00111000", "U": "00110111", "V": "00110110", "W": "00110101", "X": "01011110", "Y": "01000001", "Z": "01000010", "a": "01000011", "b": "01000100", "c": "01000101", "d": "01001011", "e": "01001010", "f": "01001100", "g": "01001110", "h": "01001001", "i": "01010001", "j": "01010011", "k": "01010010", "l": "01010101", "m": "01010100", "n": "01011001", "o": "01011000", "p": "01010111", "q": "01010110", "r": "01011010", "s": "01000110", "t": "01000111", "u": "01001000", "v": "01001101", "w": "01001111", "x": "01010000", "y": "01100001", "z": "01100010", "+": "01100011", "-": "01100100", "@": "01100101", "*": "01100110", "(": "01100111", ")": "01101000", "'": "01101001", "\"": "01101010", "/": "01101011", "\\": "01101100", ".": "01101101", ",": "01101110", "&": "01100000", "#": "00100100", "$": "00100110", "%": "00100001", "!": "00100101", "{": "01111101", "}": "01111011", ":": "00111011", ";": "00111010", "<": "00111111", "?": "00111100", ">": "00100000", "[": "01011101", "]": "01011011", "|": "00100011", " ": "01101111", "1": "01110000", "2": "01110001", "3": "01110010", "4": "01110011", "5": "01110100", "6": "01110101", "7": "01110110", "8": "01110111", "9": "01111000", "0": "01111001", "~": "01111010", "`": "01011111", "_": "00111101", "=": "01111100", "^": "00111110"}
    }
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "pheonixapp", "files", "Mapper", "DEFAULT_MAPS.json"), "w") as file:
        json.dump(ENCMAPS_DATA, file)