import os
import sys
from typing import *
import base64
import json

from PheonixAppAPI.pheonixapp.files import (HashDecoderT)

if __name__ == "__main__":
    sys.path.append(os.path.dirname(__file__))

    os.chdir(os.path.dirname(__file__))

class BIN():
    """
    A class to handle binary operations, encoding, and decoding for various formats and encodings.

    Attributes:
    ----------
    path : str
        The path to the binary file.
    format : str
        The format of the binary data.
    encoding : str
        The encoding used for the data.
    encode : bool
        Whether to encode the data.
    content : str
        The content to be encoded/decoded.
    content_dict : dict
        The dictionary content to be encoded/decoded.
    use_base64 : bool
        Whether to use base64 encoding.
    use_pheonixApp_encoder : bool
        Whether to use PheonixApp encoder.
    """

    def __init__(self, path: str = "./aol_var-dict.aolvd", format: str = "vardict-v0.001JSON", encoding: str = "utf-16", encode: bool = False, content: str = "", content_dict: dict = {}, use_base64: bool = False, use_pheonixApp_encoder: bool = True, compressed: bool = False, hyper_compressed: bool = False) -> None:
        """
        Initialize the BIN class with the provided parameters.

        Parameters:
        ----------
        path : str
            The path to the binary file.
        format : str
            The format of the binary data.
        encoding : str
            The encoding used for the data.
        encode : bool
            Whether to encode the data.
        content : str
            The content to be encoded/decoded.
        content_dict : dict
            The dictionary content to be encoded/decoded.
        use_base64 : bool
            Whether to use base64 encoding.
        use_pheonixApp_encoder : bool
            Whether to use PheonixApp encoder.
        compressed : bool
            Whether to use compressed encoding.
        hyper_compressed : bool
            Wether to use hyper-compressed encoding.
        """
        self.path = path
        if not os.path.exists(self.path):
            pass

        self.format: str = format
        self.encoding: str = encoding
        self.encode: bool = encode
        self.content: str = content
        self.content_dict: dict = content_dict
        self.use_base64: bool = use_base64
        self.use_pheonixapp_encoder: bool = use_pheonixApp_encoder
        self.compressed = compressed
        self.hyper_compressed  = hyper_compressed

        if hyper_compressed:
            self.compressed = False

        if use_pheonixApp_encoder:
            self.use_base64 = False
        elif not use_pheonixApp_encoder and not use_base64:
            self.use_pheonixapp_encoder = True

    def bin_to_str(self, data: Union[str, int, dict]) -> str:
        """
        Convert binary data to a string.

        Parameters:
        ----------
        data : Union[str, int, dict]
            The binary data to be converted.

        Returns:
        -------
        str
            The resulting string.
        """
        data = str(data)
        binary_values = data.split()
        ascii_characters = [chr(int(bv, 2)) for bv in binary_values]
        return ''.join(ascii_characters)

    def str_to_bytes(self, data: Union[str, int, dict], encoding: str = "utf-16") -> bytes:
        """
        Convert a string to bytes using the specified encoding.

        Parameters:
        ----------
        data : Union[str, int, dict]
            The string data to be converted.
        encoding : str
            The encoding to be used.

        Returns:
        -------
        bytes
            The resulting bytes.
        """
        return bytes(str(data), encoding)

    def bytes_to_str(self, data: bytes, encoding: str = "utf-16") -> str:
        """
        Convert bytes to a string using the specified encoding.

        Parameters:
        ----------
        data : bytes
            The bytes to be converted.
        encoding : str
            The encoding to be used.

        Returns:
        -------
        str
            The resulting string.
        """
        return data.decode(encoding)

    def to_binINT(self, data_dict: dict = {}, data_str: str = "", useString: bool = True) -> int:
        """
        Convert a string or dictionary to a binary integer representation.

        Parameters:
        ----------
        data_dict : dict
            The dictionary to be converted.
        data_str : str
            The string to be converted.
        useString : bool
            Whether to use the string for conversion.

        Returns:
        -------
        int
            The resulting binary integer.
        """
        l, m = [], []

        dict_str: str = ""

        if useString:
            for i in data_str:
                l.append(ord(i))

            for i in l:
                m.append(int(bin(i)[2:]))

            return m
        else:
            dict_str = str(data_dict)

            for i in dict_str:
                l.append(ord(i))

            for i in l:
                m.append(int(bin(i)[2:]))

            return m

    def str_to_bin(self, data: str) -> str:
        """
        Convert a string to its binary representation.

        Parameters:
        ----------
        data : str
            The string to be converted.

        Returns:
        -------
        str
            The resulting binary string.
        """
        return ' '.join(format(ord(char), 'b') for char in data)

    def get_str(self) -> str:
        """Get the content of the file"""
        data = ""

        with open(self.path, "rb") as file:
            file.seek(0)
            data = file.read()
            file.close()

        data_ = data
        data = self.bytes_to_str(data, "utf-16")

        if self.use_pheonixapp_encoder:
            if not self.compressed and not self.hyper_compressed:
                data = HashDecoderT.Decode(self.bin_to_str(data), "Hype_Space_BIN", "Community").run()
            elif self.compressed:
                data = HashDecoderT.Decode(data, "Hype_Space_BIN", "Community").run()
            else:
                data = HashDecoderT.Decode(data, "Hype_Space", "Community").run()
        else:
            if not self.compressed or self.hyper_compressed:
                data = self.bin_to_str(self.bytes_to_str(base64.a85decode(data_), "utf-8"))
            else:
                data = self.bytes_to_str(base64.a85decode(data_), "utf-8")

        return data

    def get_dict(self) -> dict:
        data = self.get_str()
        data = json.loads(data)

        return data

    def push_str(self) -> None:
        """
        Encode and write a string to the binary file.
        """
        data = ""
        if self.use_pheonixapp_encoder:
            if not self.hyper_compressed:
                data = HashDecoderT.Encode(self.content, "Hype_Space_BIN", "Community").run()
            else:
                data = HashDecoderT.Encode(self.content, "Hype_Space", "Community").run()

            if not self.compressed and not self.hyper_compressed:
                data = self.str_to_bytes(self.str_to_bin(data), "utf-16")
            else:
                data = self.str_to_bytes(data, "utf-16")
        else:
            if not self.compressed and self.hyper_compressed:
                data = base64.a85encode(self.str_to_bytes(self.str_to_bin(self.content), "utf-8"))
            else:
                data  = base64.a85encode(self.str_to_bytes(self.content, "utf-8"))

        with open(self.path, "wb") as file:
            file.write(data)

    def push_dict(self) -> None:
        """
        Encode and write a dictionary to the binary file.
        """
        data = ""
        dict_ = str(self.content_dict)
        if self.use_pheonixapp_Encode:
            if not self.hyper_compressed:
                data = HashDecoderT.Encode(dict_, "Hype_Space_BIN", "Community").run()
            else:
                data = HashDecoderT.Encode(dict_, "Hype_Space", "Community").run()
            if not self.compressed and not self.hyper_compressed:
                data = self.str_to_bytes(self.str_to_bin(data), "utf-16")
            else:
                data = self.str_to_bytes(data, "utf-16")
        else:
            if not self.compressed and not self.hyper_compressed:
                data = base64.a85encode(self.str_to_bytes(self.str_to_bin(dict_), "utf-8"))
            else:
                data  = base64.a85decode(self.str_to_bytes(dict_, "utf-8"))

        with open(self.path, "wb") as file:
            file.write(data)

    def PEMU(self) -> str:
        """This will encode a given string using PEMU(Pheonix Encoding Method User).

        Returns:
            str: The encoded data.
        """

        data = HashDecoderT.Encode(self.content, "Hype_Space_BIN", "Community").run()
        data = self.str_to_bin(data)
        return data

    def PCEMU(self) -> str:
        """This will encode a given string using PCEMU(Pheonix Compressed Encoding Method User).

        Returns:
            str: The encoded data.
        """

        data = HashDecoderT.Encode(self.content, "Hype_Space_BIN", "Community").run()
        return data

    def PHCEMU(self) -> str:
        """This will encode a given string using PHCEMU(Pheonix Hyper-Compressed Encoding Method User).

        Returns:
            str: The encoded data.
        """

        data = HashDecoderT.Encode(self.content, "Hype_Space", "Community").run()
        return data

    def PDMU(self) -> str:
        """This will decode a given string using PDMU(Pheonix Decoding Method User).

        Returns:
            str: The decoded data.
        """

        data = self.bin_to_str(data)
        data = HashDecoderT.Decode(self.content, "Hype_Space_BIN").run()
        return data

    def PCDMU(self) -> str:
        """This will decode a given string using PCDMU(Pheonix Compressed Decoding Method User).

        Returns:
            str: The decoded data.
        """

        data = HashDecoderT.Decode(self.content, "Hype_Space_BIN").run()
        return data

    def PHCDMU(self) -> str:
        """This will decode a given string using PHCDMU(Pheonix Hyper-Compressed Decoding Method User).

        Returns:
            str: The decoded data.
        """

        data = HashDecoderT.Decode(self.content, "Hype_Space").run()
        return data