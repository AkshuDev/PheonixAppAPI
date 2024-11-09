from typing import *

class Color:
    """Color Class for defining color.
    """
    def __init__(self, color:str="white") -> None:
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

        self.color = self.ColorToRGB(color)

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