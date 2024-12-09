from typing import *

import os
import sys

PHardwareITK = len(sys.path) - 1
PHardwareITK_P = os.path.join(os.path.dirname(__file__), "..", "..")

class Color:
    """Color Class for defining color.
    """
    def __init__(self, color:str="white", alpha:int=255) -> None:
        """Init of color class.

        Args:
            color (str, optional): The color, leave and chose a function if, want to use RGB. Defaults to "white".
        """
        self.color_names_rgb:dict[str, tuple[int, int, int]] = {
            "red": (255, 0, 0),
            "green": (0, 255, 0),
            "blue": (0, 0, 255),
            "yellow": (255, 255, 0),
            "cyan": (0, 255, 255),
            "magenta": (255, 0, 255),
            "black": (0, 0, 0),
            "white": (255, 255, 255),
            "gray": (169, 169, 169),
            "grey": (169, 169, 169),
            "silver": (192, 192, 192),
            "maroon": (128, 0, 0),
            "olive": (128, 128, 0),
            "lime": (0, 255, 0),
            "aqua": (0, 255, 255),
            "fuchsia": (255, 0, 255),
            "teal": (0, 128, 128),
            "navy": (0, 0, 128),
            "purple": (128, 0, 128),
            "pink": (255, 192, 203),
            "brown": (139, 69, 19),
            "beige": (245, 245, 220),
            "chocolate": (210, 105, 30),
            "coral": (255, 127, 80),
            "indigo": (75, 0, 130),
            "lavender": (230, 230, 250),
            "violet": (238, 130, 238),
            "peach": (255, 218, 185),
            "gold": (255, 215, 0),
            "plum": (221, 160, 221),
            "orchid": (218, 112, 214),
            "crimson": (220, 20, 60),
            "chartreuse": (127, 255, 0),
            "tomato": (255, 99, 71),
            "salmon": (250, 128, 114),
            "seashell": (255, 245, 238),
            "blush": (222, 93, 131),
            "wheat": (245, 222, 179),
            "khaki": (240, 230, 140),
            "mint": (189, 252, 201),
            "forest": (34, 139, 34),
            "lemon": (255, 247, 0),
            "pearl": (234, 234, 234),
            "periwinkle": (204, 204, 255),
            "sand": (194, 178, 128),
            "emerald": (80, 200, 120),
            "russet": (128, 70, 27),
            "scarlet": (255, 36, 0),
            "charcoal": (54, 69, 79),
            "rose": (255, 99, 123),
            "tangerine": (255, 129, 0),
            "bordeaux": (127, 0, 24)
        }

        self.hex_codes_rgb:dict[str, tuple[int, int, int]] = {
            "#ff0000": (255, 0, 0),
            "#00ff00": (0, 255, 0),
            "#0000ff": (0, 0, 255),
            "#ffff00": (255, 255, 0),
            "#00ffff": (0, 255, 255),
            "#ff00ff": (255, 0, 255),
            "#000000": (0, 0, 0),
            "#ffffff": (255, 255, 255),
            "#a9a9a9": (169, 169, 169),
            "#c0c0c0": (192, 192, 192),
            "#800000": (128, 0, 0),
            "#808000": (128, 128, 0),
            "#00ff00": (0, 255, 0),
            "#00ffff": (0, 255, 255),
            "#ff00ff": (255, 0, 255),
            "#008080": (0, 128, 128),
            "#000080": (0, 0, 128),
            "#800080": (128, 0, 128),
            "#ffc0cb": (255, 192, 203),
            "#8b4513": (139, 69, 19),
            "#f5f5dc": (245, 245, 220),
            "#d2691e": (210, 105, 30),
            "#ff7f50": (255, 127, 80),
            "#4b0082": (75, 0, 130),
            "#e6e6fa": (230, 230, 250),
            "#ee82ee": (238, 130, 238),
            "#ffdab9": (255, 218, 185),
            "#ffd700": (255, 215, 0),
            "#dda0dd": (221, 160, 221),
            "#da70d6": (218, 112, 214),
            "#dc143c": (220, 20, 60),
            "#7fff00": (127, 255, 0),
            "#ff6347": (255, 99, 71),
            "#fa8072": (250, 128, 114),
            "#fff5ee": (255, 245, 238),
            "#de5d83": (222, 93, 131),
            "#f5deb3": (245, 222, 179),
            "#f0e68c": (240, 230, 140),
            "#bdfcc9": (189, 252, 201),
            "#228b22": (34, 139, 34),
            "#fff700": (255, 247, 0),
            "#eaeaea": (234, 234, 234),
            "#ccccff": (204, 204, 255),
            "#c2b280": (194, 178, 128),
            "#50c878": (80, 200, 120),
            "#80461b": (128, 70, 27),
            "#ff2400": (255, 36, 0),
            "#36454f": (54, 69, 79),
            "#ff637d": (255, 99, 123),
            "#ff8100": (255, 129, 0),
            "#7f0029": (127, 0, 41)
        }

        self.color_names_hex:dict[str, str] = {
            "red": "#ff0000",
            "green": "#00ff00",
            "blue": "#0000ff",
            "yellow": "#ffff00",
            "cyan": "#00ffff",
            "magenta": "#ff00ff",
            "black": "#000000",
            "white": "#ffffff",
            "gray": "#a9a9a9",
            "grey": "#a9a9a9",
            "silver": "#c0c0c0",
            "maroon": "#800000",
            "olive": "#808000",
            "lime": "#00ff00",
            "aqua": "#00ffff",
            "fuchsia": "#ff00ff",
            "teal": "#008080",
            "navy": "#000080",
            "purple": "#800080",
            "pink": "#ffc0cb",
            "brown": "#8b4513",
            "beige": "#f5f5dc",
            "chocolate": "#d2691e",
            "coral": "#ff7f50",
            "indigo": "#4b0082",
            "lavender": "#e6e6fa",
            "violet": "#ee82ee",
            "peach": "#ffdab9",
            "gold": "#ffd700",
            "plum": "#dda0dd",
            "orchid": "#da70d6",
            "crimson": "#dc143c",
            "chartreuse": "#7fff00",
            "tomato": "#ff6347",
            "salmon": "#fa8072",
            "seashell": "#fff5ee",
            "blush": "#de5d83",
            "wheat": "#f5deb3",
            "khaki": "#f0e68c",
            "mint": "#bdfcc9",
            "forest": "#228b22",
            "lemon": "#fff700",
            "pearl": "#eaeaea",
            "periwinkle": "#ccccff",
            "sand": "#c2b280",
            "emerald": "#50c878",
            "russet": "#80461b",
            "scarlet": "#ff2400",
            "charcoal": "#36454f",
            "rose": "#ff637d",
            "tangerine": "#ff8100",
            "bordeaux": "#7f0029"
        }

        self.color = self.ColorToRGB(color.lower())
        self.alpha = alpha

    def RGB(self, r:int, g:int, b:int) -> tuple:
        """Sets the color to the specified RGB values

        Args:
            r (int): Red.
            g (int): Green.
            b (int): Blue.

        Returns:
            tuple: Just a copy of the entered data in the form of a tuple.
        """
        self.color = (r, g, b)
        return (r, g, b)

    def ColorToRGB(self, color:str) -> tuple:
        """Converts the specified color into its specified RGB values IF IT IS PRESENT IN THE DICTIONARY.

        Args:
            color (str): The color name.

        Returns:
            tuple: The RGB values.
        """
        if not color.lower() in self.color_names_rgb.keys():
            return None

        return self.color_names_rgb[color.lower()]

    def HexToRGB(self, hex_code:str) -> tuple:
        """Converts Hex code to RGB values IF IT IS PRESENT IN THE DICTIONARY.

        Args:
            hex_code (str): The hexadecimal code.

        Returns:
            tuple: The RGB values.
        """
        if not hex_code.lower() in self.hex_codes_rgb.keys():
            return None

        return self.hex_codes_rgb[hex_code.lower()]

    def ColorToHex(self, color:str) -> tuple:
        """Converts a color name to a hexadecimal code IF IT IS PRESENT IN THE DICTIONARY.

        Args:
            color (str): The color name.

        Returns:
            tuple: The Hexadecimal value.
        """
        if not color.lower() in self.color_names_hex.keys():
            return None

        return self.color_names_hex[color.lower()]

    def to_rgb_code(self):
        """Converts the RGB tuple to an ANSI escape code."""
        return f"\033[38;2;{self.color[0]};{self.color[1]};{self.color[2]}m"

    def to_background_code(self):
        """Converts the RGB tuple to an ANSI background escape code."""
        return f"\033[48;2;{self.color[0]};{self.color[1]};{self.color[2]}m"

class PHeader:
    """Generates a PHardware Header.

    Args:
        version (int, optional): The version of the program/File. Defaults to 1.
        flags (int, optional): The flags.. Defaults to 0.
        magicCode (Union[str, bytes], optional): The magic code in ASCII or string. Defaults to "PHardwareITK".
    """
    def __init__(self, version:int=1, flags:int=0, magicCode:Union[str, bytes]="PHardwareITK") -> None:
        """Initialize the PHeader.

        Args:
            version (int, optional): The version of the program/File. Defaults to 1.
            flags (int, optional): The flags.. Defaults to 0.
            magicCode (Union[str, bytes], optional): The magic code in ASCII or string. Defaults to "PHardwareITK".
        """
        self.version = version
        self.flags = flags
        self.magicCode = magicCode
        self.checksum = None

        if isinstance(magicCode, str):
            self.magicCode = magicCode.encode('ascii')
            magicCode = magicCode.encode('ascii')
        elif isinstance(magicCode, bytes):
            try:
                magicCode.decode('ascii')
            except UnicodeDecodeError:
                return None

    def calculateChecksum(self, Header:bytes) -> str:
        """Calculate checksum of Header.

        Args:
            Header (bytes): The header.

        Returns:
            str: The checksum.
        """
        import hashlib
        return hashlib.sha256(Header).hexdigest()

    def Pack(self) -> Any:
        """Packs the specified data into a single PHeader.


        The structure includes:


        - Magic number (4 bytes)

        - Version (4 bytes)

        - Flags (4 bytes)

        - Placeholder for checksum (32 bytes as hexadecimal string)


        Returns:
            Any: The header.
        """
        import struct

        headerData = struct.pack('>4sIB', self.magicCode, self.version, self.flags)

        checkSum = self.calculateChecksum(headerData)

        return headerData + bytes.fromhex(checkSum)

    def UnPack(self, data:str) -> Any:
        """Upacks the binary header into header fields.
        """
        import struct
        header = data[:-64]
        checksum = data[-64:]

        magic, version, flags = struct.unpack('>4sIB', header)

        self.magic = magic
        self.version = version
        self.flags = flags
        self.checksum = checksum.decode()

        # Validate checksum
        expected_checksum = self.calculateChecksum(header)
        if self.checksum != expected_checksum:
            raise ValueError(f"Checksum mismatch: expected {expected_checksum}, but got {self.checksum}")

        return self

    def WriteToFile(self, filename):
        """
        Write the packed header data to a binary file.
        """
        header_data = self.Pack()
        with open(filename, 'wb') as f:
            f.write(header_data)

    def ReadFromFile(self, filename):
        """
        Read the header from a binary file and unpack the fields.
        """
        if not os.path.exists(filename):
            raise FileNotFoundError(f"{filename} does not exist.")

        with open(filename, 'rb') as f:
            data = f.read()

        return self.UnPack(data)

class PBin:
    """
    PBin (PHardware Binary) is a custom binary serialization format designed to serialize various data types into a
    compact binary representation. The format includes strings, integers, floats, and custom flags.

    Attributes:
        data (bytes): The binary data representing the serialized object.
    """
    def __init__(self, header:Optional[PHeader]) -> None:
        """
        Initializes the PBin object with an empty data field.
        """
        self.data:bytes = b""

        self.header:PHeader = header if header else PHeader()

    def Serialize(self, data:Union[str, bytes, int, dict, float, list, bool], CB_flag:Optional[bool]=None) -> bytes:
        """
        Serializes a string, integer, float, and a custom flag into a binary format.

        Args:
            data (Union[str, bytes (UTF-8), int, dict (CONVERTED TO STR), float, list, bool]): The data to serialize, in UTF-8 format.
            CB_flag (Optional[bool], optional): A flag indicating whether a custom byte follows. Defaults to None

        Returns:
            bytes: The serialized binary data.
        """
        import random

        if isinstance(data, list):
            data = "".join(data)
        elif isinstance(data, bytes):
            data = data.decode()
        elif isinstance(data, int) or (isinstance(data, float) or (isinstance(data, dict) or (isinstance(data, bool)))):
            data = str(data)

        binary_data = bytearray()

        # Serialize the header first using the PHeader class
        header_data = self.header.Pack()
        binary_data.extend(header_data)

        # 1. String serialization (length-prefixed UTF-8 string)
        encoded_string: bytes = data.encode('utf-8')
        binary_data.append(len(encoded_string))  # Length of the string as a single byte.
        binary_data.extend(encoded_string)  # Actual string data

        # 2. Custom flag section (1 byte flag to indicate custom data)
        if CB_flag:
            binary_data.append(0xFF)  # Custom flag byte to indicate extra data
            binary_data.append(random.randint(0, 255))  # Random byte between 0 and 255 for custom data

        # Return the complete binary data.
        self.data = bytes(binary_data)
        return self.data

    def Deserialize(self, binary_data:bytes) -> tuple[str, bool, Optional[int]]:
        """
        Deserializes the provided binary data into its original components.

        Args:
            binary_data (bytes): The binary data to deserialize.

        Returns:
            tuple: A tuple containing the deserialized values in the following order:
                - string_data (str): The deserialized string.
                - CB_flag (bool): Flag indicating whether custom data exists.
                - CB_data (Optional[int]): Custom data byte if present.
        """
        import io
        import struct

        # Unpack the header first
        header_data = binary_data[:self.header.Pack().__len__()]
        self.header.UnPack(header_data)

        # Continue with the rest of the deserialization
        stream = io.BytesIO(binary_data[len(header_data):])

        # 1. Deserialize string (length-prefixed)
        string_length: int = ord(stream.read(1))  # Read the length of the string (1 byte)
        string_data: str = stream.read(string_length).decode('utf-8')  # Read the string

        # 2. Check if there's a custom data flag
        custom_flag: bool = False
        custom_data: int = None
        if stream.read(1) == b'\xFF':
            custom_flag = True
            custom_data = ord(stream.read(1))  # Read the custom data byte

        return (string_data, custom_flag, custom_data)

    @property
    def BinaryData(self):
        return self.data

def ToBytes(data:Optional[Union[str, dict, int, bool]]) -> Optional[bytes]:
    """Encode the given data.

    Args:
        data (Optional[Union[str, dict, int, bool]]): The data.

    Returns:
        Optional[bytes]: Encoded data.
    """
    if not data:
        return None
    data = str(data)
    return data.encode()

def FromBytes(data:Optional[bytes]) -> Optional[str]:
    """Decode the given data.

    Args:
        data (Optional[bytes]): The data.

    Returns:
        Optional[str]: Decoded data.
    """
    if not data:
        return None
    return data.decode()

class TextFont:
    """Just a Class for Font.
    """
    def __init__(self, font:str="Arial", font_size:int=11, font_color:Color=Color(), font_background_color:Color=Color("black"), Italic:bool=False, Underline:bool=False,
                 Bold:bool=False, XtraBold:bool=False, StrikeThrough:bool=False) -> None:
        """Initialize for TextFont class.

        Args:
            font (str, optional): Font. Defaults to "Arial".
            font_size (int, optional): The size of the font. Defaults to 11.
            font_color (Color, optional): The color of the font. Defaults to Color().
            font_background_color (Color, optional): The bg color of the font. Defaults to Color("black").
            Italic (bool, optional): Font Italic. Defaults to False.
            Underline (bool, optional): Underlined Font. Defaults to False.
            Bold (bool, optional): Bold Font. Defaults to False.
            XtraBold (bool, optional): More Bolder Font. Defaults to False.
            StrikeThrough (bool, optional): StikeThrough Font. Defaults to False.
        """

        if Bold and XtraBold:
            Bold = False

        self.font = font
        self.size = font_size
        self.color = font_color
        self.background_color = font_background_color
        self.italic = Italic
        self.underline = Underline
        self.bold = Bold
        self.xtraBold = XtraBold
        self.strike_through = StrikeThrough

    def to_font_code(self):
        """Generate the font style escape codes."""
        codes = []
        if self.bold:
            codes.append("1")  # Bold
        if self.xtraBold:
            codes.append("8")  # Extra Bold (if supported by terminal)
        if self.italic:
            codes.append("3")  # Italic
        if self.underline:
            codes.append("4")  # Underline
        if self.strike_through:
            codes.append("9")  # Strike-through

        if codes:
            return f"\033[{';'.join(codes)}m"
        return ""

    def to_reset_code(self):
        """Reset the font styles."""
        return "\033[0m"

    def to_font_size_code(self):
        """Returns the Escape codes for Font Size. NOTE: Does't work with all OS/Terminals. Due to Font size not being supported universally.
        OS like -> MacOS, XTerm Based, GNOME (Not via Escape codes), Windows (By changing data in a windows file), etc do support it.

        Supported Platforms for this function -> MacOS (ITerm2), Xterm Based (Includes Konsole).
        """

        if self.size == 11:
            return None # Default size

        if "iTerm" in os.environ.get("TERM_PROGRAM", ""):
            return f"\033]50;SetProfile=font-size={self.size}\a" #ITerm2
        elif "xterm" in os.environ.get("TERM", "") or "konsole" in os.environ.get("TERM", ""):
            return f"ESC]50;SetProfile=font-size={self.size}" # Xterm & Konsole
        else:
            return None # Other OS/Terminals

class PWidget:
    def __init__(self, x:int=0, y:int=0, width:int=5, height:int=5, radius:int=0, bgColor:Color=Color(), textWrap:bool=False, textFont:TextFont=TextFont(), text:str="") -> None:
        """Initialize function for PWidget class.

        Args:
            x (int, optional): X coordinate. Defaults to 0.
            y (int, optional): Y coordinate. Defaults to 0.
            width (int, optional): Width of widget. Defaults to 5.
            height (int, optional): Height of widget. Defaults to 5.
            radius (int, optional): Radius of widget (If required). Defaults to 0.
            bgColor (Color, optional): Background color of widget. Defaults to Color().
            textWrap (bool, optional): Text In Widget?. Defaults to False.
            textFont (TextFont, optional): The Text Font (if required). Defaults to TextFont().
            text (str, optional): The text. (if required). Defaults to "".
        """
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.radius = radius
        self.bgColor = bgColor
        self.textWrap = textWrap
        self.textFont = textFont
        self.text = text

    def Contains(self, x:int, y:int) -> bool:
        """Check if a point (x, y) is within the widget's boundaries."""
        return self.x <= x <= self.x + self.width and self.y <= y <= self.y + self.height

    def Draw(self, window: Any):
        """Draw the widget onto the window. Should be overridden by subclasses."""
        raise NotImplementedError("draw() method must be implemented by the subclass.")

    def Change(self, x:Optional[int]=None, y:Optional[int]=None, width:Optional[int]=None, height:Optional[int]=None, radius:Optional[int]=None, bgColor:Optional[Color]=None, textWrap:Optional[bool]=None, textFont:Optional[TextFont]=None, text:Optional[str]=None) -> None:
        """Change the details.

        Args:
            x (Optional[int], optional): X. Defaults to None.
            y (Optional[int], optional): Y. Defaults to None.
            width (Optional[int], optional): Width. Defaults to None.
            height (Optional[int], optional): Height. Defaults to None.
            radius (Optional[int], optional): Radius. Defaults to None.
            bgColor (Optional[Color], optional): Background Color. Defaults to None.
            textWrap (Optional[bool], optional): Text Wrap?. Defaults to None.
            textFont (TextFont, optional): Text Font. Defaults to None.
            text (Optional[str], optional): Text. Defaults to None.
        """
        if x:
            self.x = x

        if y:
            self.y = y

        if width:
            self.width = width

        if height:
            self.height = height

        if radius:
            self.radius = radius

        if bgColor:
            self.bgColor = bgColor

        if textWrap != None:
            self.textWrap = textWrap

        if text:
            self.text = text

        if textFont:
            self.textFont = textFont

class PIcon:
    """PIcon (PHardware Icon) class.
    """
    def __init__(self, iconPath: Optional[str] = "", x: Optional[int] = None, y: Optional[int] = None, width: Optional[int] = None, height: Optional[int] = None) -> None:
        """The INIT function of the PIcon class.

        Args:
            iconPath (Optional[str], optional): The path to the icon file. Defaults to "".
            x (Optional[int], optional): The X coordinate of the icon. Defaults to None.
            y (Optional[int], optional): The Y coordinate of the icon. Defaults to None.
            width (Optional[int], optional): The Width of the icon. Defaults to None.
            height (Optional[int], optional): The Height of the icon. Defaults to None.
        """
        self.iconPath:Optional[str] = iconPath
        self.BiconPath:Optional[bytes] = self.ToBytes(iconPath)
        self.iconSurface:Optional[Any] = None
        self.x:Optional[int] = x
        self.y:Optional[int] = y
        self.width:Optional[int] = width
        self.height:Optional[int] = height

    def LoadImageSDL2(self) -> Any:
        """Loads the image for SDL2.

        Returns:
            Any: Loaded image.
        """
        import sdl2.sdlimage
        return sdl2.sdlimage.IMG_Load(self.BiconPath)

    def SetIconSDL2(self, window:Any) -> None:
        """Changes the icon in the specified window. SDL2.

        Args:
            window (Any): The window.
        """
        import sdl2
        import sdl2.sdlimage

        if self.BiconPath:
            self.iconSurface = self.LoadImageSDL2()
            if not self.iconSurface:
                return None

            sdl2.SDL_SetWindowIcon(window, self.iconSurface)
        else:
            return None

    def Free(self) -> None:
        """Frees the image.
        """
        import sdl2
        if self.iconSurface:
            sdl2.SDL_FreeSurface(self.iconSurface)

    def ToBytes(self, data:Optional[Union[str, dict, int, bool]]) -> Optional[bytes]:
        """Encode the given data.

        Args:
            data (Optional[Union[str, dict, int, bool]]): The data.

        Returns:
            Optional[bytes]: Encoded data.
        """
        if not data:
            return None
        data = str(data)
        return data.encode()

    def FromBytes(self, data:Optional[bytes]) -> Optional[str]:
        """Decode the given data.

        Args:
            data (Optional[bytes]): The data.

        Returns:
            Optional[str]: Decoded data.
        """
        if not data:
            return None
        return data.decode()
