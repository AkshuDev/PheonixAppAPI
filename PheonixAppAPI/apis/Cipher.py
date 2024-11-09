import os
import sys

from typing import *

import cryptography
import Crypto
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

from numpy import mgrid
from sympy import nextprime, isprime
import random

from PheonixAppAPI.Scripts.post_install import Encrypt_Maps

class PTDMEDMU():
    """This class stands for Pheonix Three Dimensional Matrix Encrypt/Decrypt Method User. This method encrypts each character 4 times placing it on one of the cells from one of the 6 grids. This is a hard to crack method.
    NOTE: The available bytes for encryption are anywhere from 1 to 900.
    
    NOTE: Doesn't include Decrypt yet. [Under Development]"""
    def __init__(self) -> None:
        """This class stands for Pheonix Three Dimensional Encrypt/Decrypt Method User. This method encrypts each character 4 times placing it on one of the cells from one of the 6 grids. This is a hard to crack method.
        NOTE: The available bytes for encryption are anywhere from 1 to 900."""
        from PheonixAppAPI.apis.Modules.Pre.PheonixCipherTools.LIB import CipherTools
        self.Pheonix_3D_Matrix_Table = CipherTools.pheonix_3d_matrix_v1
        self.Pheonix_3D_Matrix_SBOX = CipherTools.pheonix_3d_matrix_sbox
        self.enc_times_round = 0

    @staticmethod
    def new(key:Union[str, int, bytes], use_sys_info:bool=False, value:Union[str, bytes, int]="") -> tuple[str, str]:
        """This function allows you to use the encrypt and decrypt methods.
        Args:
            key(Union[str, int, bytes]): The key to be used.
            use_sys_info(bool, optional): This defines wether to set/append the key with the sys-info of the computer. This is helpful when you want only a specific computer to decode the message. Defaults to False.
            value(Union[str, bytes, int], optional): This defines to value to be encrypted or decrypted. Defaults to ''.

        Returns:
            tuple[str, str]: The first value is the key and the second value is the output value. NOTE: Please use the output value as it is modified to match the len of the key."""

        if isinstance(key, int) or isinstance(key, str):
            key = str(key)
        elif isinstance(key, bytes):
            key = key.decode()

        if isinstance(value, int) or isinstance(value, str):
            value = str(value)
        elif isinstance(value, bytes):
            value = value.decode()

        import hashlib
        if use_sys_info:
            import platform
            import uuid

            system_info = platform.uname()
            mac_address = uuid.getnode()

            key = f"{key}-{system_info.system}-{system_info.node}-{system_info.release}-{system_info.version}-{mac_address}"

            # Hash the identifier to get a consistent length output
            key = hashlib.sha256(key.encode()).hexdigest()
        else:
            key = hashlib.sha256(key.encode()).hexdigest()

        if len(key) > len(value):
            key = key[:len(value)]
        elif len(key) < len(value):
            subLen = len(value) - len(key)
            left = subLen
            import secrets
            while left > 0:
                key += str(secrets.randbelow(9-1 + 1) + 1)
                left -= 1

        return key, value

    def adjust_ascii(self, val, pos_list):
        """Adjust ASCII value as per the given rules."""
        digit = int(val)
        result = []
        og_result = []
        digit = int(digit)
        if digit in [1, 2, 3]:
            result = digit
            og_result = digit
        else:
            og_result = digit
            # Round digit to random value
            if pos_list == []:
                digit = "1 1 1"
            else:
                last_pos =  pos_list[len(pos_list) - 1]
                last_grid, last_subgrid, last_cell = map(int, last_pos.split(" "))
                if last_grid != 10:
                    digit = str(last_grid + 1) + " 1 1"
                elif last_subgrid != 10:
                    digit = "10 " + str(last_subgrid + 1) + " 1"
                elif last_cell != 10:
                    digit = "10 10 " + str(last_cell + 1)
                else:
                    raise Exception("Invalid position. Can only happend due to altering of encryption code or invalid value size")
            result = digit
        return str(result), str(og_result)

    def process_ascii(self, ascii_val, pos, pos_list, getpos):
        """Process ASCII value with additional checks and modifications."""
        og = []

        if getpos:
            pos, og = self.adjust_ascii(ascii_val, pos_list)

        # Ensure ASCII processing is unique for each position
        processed_ascii, og = self.adjust_ascii(ascii_val, pos_list)
        if pos in pos_list:
            # Apply some modification if the position is repeated
            ascii_val = (ascii_val + 1) % 256
            processed_ascii, og = self.adjust_ascii(ascii_val, pos_list)

        return processed_ascii, og

    def encrypt(self, key:Union[str, int, bytes], value:Union[str, int, bytes]) -> bytes:
        """This method encrypts the given value. NOTE: Please use the output value provided from the new method.

        Args:
            key (Union[str, int, bytes]): The key to use.
            value (Union[str, int, bytes]): The value to encrypt.

        Returns:
            bytes: The output encryption.
        """

        import struct

        if isinstance(key, int) or isinstance(key, str):
            key = str(key)
        elif isinstance(key, bytes):
            key = key.decode()

        if isinstance(value, int) or isinstance(value, str):
            value = str(value)
        elif isinstance(value, bytes):
            value = value.decode()

        key = key.encode()
        value = value.encode()

        str_value = value.decode()

        code_points = [ord(char) for char in str_value]
        modified_code_points = [(code_point * 2 + 3) % 256 for code_point in code_points]
        modified_text = ''.join(chr(code_point) for code_point in modified_code_points)

        # Padding or truncation to match original length
        if len(modified_text) < len(value):
            modified_text += " " * (len(value) - len(modified_text))
        else:
            modified_text = modified_text[:len(value)].encode()

        result = bytes(a ^ b for a, b in zip(key, modified_text))

        enc_chars = []
        pos_list = []

        for i, byte in enumerate(result):
            char = chr(byte)
            enc = char.encode("utf-8")
            ascii_ = ord(char)

            p_ascii, og_pos = self.process_ascii(ascii_, "", pos_list, True)

            pos_list.append(p_ascii)
            enc_chars.append(enc)

        final_result = []
        final_chars = []
        char_be = []
        current = 0
        for char, pos in zip(enc_chars, pos_list):
            i = 2
            char = char.decode()
            grid, subgrid, cell = map(int, pos.split(' '))
            mGrid, mSubgrid, mCell = self.Pheonix_3D_Matrix_Table[f'{grid} {subgrid} {cell}'].split()
            subs_char = self.Pheonix_3D_Matrix_SBOX[char].encode()
            subs_char = bytes(a ^ b for a, b in zip(key, subs_char))
            while i > 0:
                mGrid, mSubgrid, mCell = self.Pheonix_3D_Matrix_Table[f'{mGrid} {mSubgrid} {mCell}'].split()
                subs_char = self.Pheonix_3D_Matrix_SBOX[subs_char.decode()].encode()
                subs_char = bytes(a ^ b for a, b in zip(key, subs_char))
                i -= 1
            final_chars.append(subs_char)
            final_result.append(f"{mGrid, mSubgrid, mCell}")
            current += 1

        for i, v in enumerate(final_chars):
            final_chars[i] = v.decode()

        encrypted_data = ''.join(final_chars)

        return encrypted_data

class PMEDMU():
    """This class stands for Pheonix Mathematical Encrypt/Decrypt Method User. This method uses large primes for doing encryption and decryption. It normally uses the MAC address of a computer but more keys can be added to it.
    """
    def __init__(self) -> None:
        """This class stands for Pheonix Mathematical Encrypt/Decrypt Method User. This method uses large primes for doing encryption and decryption. It normally uses the MAC address of a computer but more keys can be added to it.
        """
        pass

    def generate_large_prime(self, bits:int) -> int:
        """Generate a large prime number with the specified bit size.

        Args:
            bits (int): The bit size

        Returns:
            int: The output
        """
        prime = random.getrandbits(bits)
        while not isprime(prime):
            prime = random.getrandbits(bits)
        return prime

    def new(self, bits:int) -> int:
        """Generate a pair of large primes for encryption and decryption.

        Args:
            bits (int): The bit size.

        Returns:
            int: The output
        """
        p = self.generate_large_prime(bits)
        q = self.generate_large_prime(bits)
        return p, q

    def encrypt(self, message: Union[str, int, bytes], p: int, q: int) -> bytes:
        """Encrypt a message using large primes p and q.

        Args:
            message (Union[str, int, bytes]): The message to encrypt.
            p (int): Large prime 1.
            q (int): Large prime 2.

        Raises:
            ValueError: If the message is too long for the given primes.

        Returns:
            bytes: The output encrypted message
        """
        if isinstance(message, int):
            message = str(message)
        elif isinstance(message, bytes):
            message  = message.decode()

        # Convert message to numerical form
        message_bytes = message.encode('utf-8')
        message_num = int.from_bytes(message_bytes, 'big')

        # Ensure message_num fits within the modulus
        if message_num >= q:
            raise ValueError("Message is too long for the given prime.")

        # Encryption: (message ^ p) % q
        encrypted_num = (message_num + p) % q

        return str(encrypted_num).encode("utf-16")


    def decrypt(self, encrypted_bytes: bytes, p: int, q: int) -> str:
        """Decrypt a message using large primes p and q.

        Args:
            encrypted_bytes (int): The encrypted data in bytes (utf-16).
            p (int): Large prime 1.
            q (int): Large prime 2.

        Returns:
            str: The output.
        """
        try:
            # Convert the encrypted data to integer
            encrypted_num = encrypted_bytes.decode("utf-16")

            encrypted_num = int(encrypted_num)

            # Decryption: (encrypted_num ^ p) % q
            decrypted_num = (encrypted_num - p) % q

            # Convert numerical form back to bytes
            message_bytes = decrypted_num.to_bytes((decrypted_num.bit_length() + 7) // 8, "big")

            # Decode bytes to string
            message = message_bytes.decode()

            return message
        except UnicodeDecodeError:
            raise Exception("This message can't be decoded using the specified primes.")

class PTSEDM():
    """This class is used to encrypt or decrypt data using Pheonix Two Step Encrypt/Decrypt Method (PTSEDM). It normally uses the MAC address of a computer but more keys can be added to it.
    """
    def __init__(self) -> None:
        """This class is used to encrypt or decrypt data using Pheonix Two Step Encrypt/Decrypt Method (PTSEDM). It normally uses the MAC address of a computer but more keys can be added to it.
        """
        pass

    def get_machine_identifier(self, key=str(nextprime(256)), data="") -> bytes:
        """This function returns a unique identifier that is different in all machines (MAC)

        Args:
            key(str, optional): The key that will be used while encrypting and decrypting the data. The key and the computer should be same or else a error might occur. Defaults to str(nextprime(256)).
            data(Any, optional): The data here will be used to make a proper key bigger than the data.

        Returns:
            bytes: The output."""

        import platform
        import hashlib
        import uuid
        system_info = platform.uname()
        mac_address = uuid.getnode()

        if isinstance(data, bytes):
            data = str(data).replace("b'", '').replace("'", '')
        elif isinstance(data, int):
            data = str(data)

        # if data != "":
        #     fulllen = len(str(mac_address))+len(key)
        #     msglen = len(data)

        #     if fulllen < msglen:
        #         reqLen = msglen - fulllen
        #         while reqLen > -1:
        #             reqLen -= 1
        #             key = key + str(random.randint(0, 9))

        # Combine system and network information
        identifier = f"{system_info.system}-{system_info.node}-{system_info.release}-{system_info.version}-{mac_address}-{key}"

        # Hash the identifier to get a consistent length output
        hashed_identifier = hashlib.sha256(identifier.encode()).digest()

        combined_key = hashed_identifier.upper()[::-1]
        output = (combined_key * ((len(data) // len(combined_key)) + 1))[:len(data)]

        return output

    def encrypt(self, data: Union[str, int, bytes], flag:str="", key=str(nextprime(256))) -> Union[str, bytes]:
        """
        Encrypt data using a machine-specific identifier.

        Args:
            data (bytes): The data to encrypt.
            flag (str, optional): Flags to encrypt/decrypt. Available Are ->
                1. decrypt: Means instead of rerunning the program and getting wrong data some decodes are made to the data so that rerunning the program will just result in the orignal data.
            key(str, optional): The key that will be used to encrypt the data. Even if the key is right the computer should be having the correct mac address to decrypt. Defaults to str(nextprime(256)).
        Returns:
            bytes: The encrypted data.
        """
        machine_identifier = self.get_machine_identifier(key=key, data=data)

        if not flag == "decrypt":
            if isinstance(data, int):
                data = str(data)
            elif isinstance(data, bytes):
                data = data.decode()
        else:
            decrypted_data = bytes(a ^ b for a, b in zip(data, machine_identifier))

            value = decrypted_data.decode("utf-8")
            return value

        data = data.encode("utf-8")

        encrypted_data = bytes(a ^ b for a, b in zip(data, machine_identifier))

        return encrypted_data

    def decrypt(self, encrypted_data: bytes, key:str=str(nextprime(256))) -> str:
        """
        Decrypt data using a machine-specific identifier.

        Args:
            encrypted_data (bytes): The data to decrypt.
            key(str, optional): The key that will be used to decrypt the data. Even if the key is right the computer should be having the correct mac address to decrypt. Defaults to str(nextprime(256)).
        Returns:
            str: The decrypted data.
        """
        try:
            return self.encrypt(encrypted_data, "decrypt", key)
        except UnicodeDecodeError:
            raise Exception("This encrypted data can't be decoded!")

class _AES_():
    """This class uses PyCryptodome for providing with tested security encryptions. This class uses AES (Advanced Encryption System).
    """
    def __init_(self) -> None:
        """This class uses PyCryptodome for providing with tested security encryptions. This class uses AES (Advanced Encryption System).
        """
        pass

    def Encrypt(self, data:Union[ByteString, bytes, bytearray], key:Union[ByteString, bytearray, bytes], mode=AES.MODE_CBC):
        """This function allows to encrypt data using AES.

        Args:
            data (Union[ByteString, bytes, bytearray]): The data for encryption.
            key (Union[ByteString, bytearray, bytes]): The key that will be used for encryption.
            mode (Any, optional): This defines the mode used for encrypting data. It should be set only using either the _AES_.modes.(mode) or AES.(mode). Defaults to AES.MODE_CBC

        Returns:
            Any: The encrypted data.
        """
        cipher = AES.new(key, mode)

        ciphertext = cipher.encrypt(data)

        return ciphertext

    def Decrypt(self, data, key:Union[ByteString, bytearray, bytes], mode=AES.MODE_CBC) -> str:
        """This function allows to decrypt data using AES.

        Args:
            data (Union[str, int]): The data for decryption.
            key (Union[ByteString, bytearray, bytes]): The key that was used for encryption.
            mode (Any, optional): This defines the mode that used for encrypting data. It should be set only using either the _AES_MODES.(mode) or AES.(mode). Defaults to AES.MODE_CBC

        Returns:
            str: The decrypted data.
        """
        cipher = AES.new(key, mode)

        text = cipher.decrypt(data)

        return text

class _AES_MODES:
    MODE_CBC = AES.MODE_CBC
    MODE_CCM = AES.MODE_CCM
    MODE_CFB = AES.MODE_CFB
    MODE_CTR = AES.MODE_CTR
    MODE_EAX = AES.MODE_EAX
    MODE_ECB = AES.MODE_ECB
    MODE_GCM = AES.MODE_GCM
    MODE_OCB = AES.MODE_OCB
    MODE_OPENPGP = AES.MODE_OPENPGP
    MODE_SIV = AES.MODE_SIV
    MODE_OFB = AES.MODE_OFB
