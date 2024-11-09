class ELF:
    def __init__(self, labels_addr:dict, current_addr:int) -> None:
        self.labels_addr = labels_addr
        self.current_addr = current_addr
        self.text_section = bytearray()
        self.data_section = bytearray()
        self.bss_section = bytearray()
        self.function_addrs = {}
        self.no_cancelled_sections = 0
        self.string_table = bytearray(b'\0')

    def create_header(self, section_headers, debug=False):
        # ELF header
        header = bytearray()
        header.extend(b'\x7FELF')  # ELF magic number
        header.append(1)  # 32-bit
        header.append(1)  # Little-endian
        header.append(1)  # ELF version
        header.append(0)  # OS/ABI
        header.append(0)  # ABI version
        header.extend(b'\x00' * 7)  # Padding
        header.append(2)  # Type: Relocatable
        header.append(3)  # Machine: x86
        header.append(1)  # Version
        header.extend((self.current_addr).to_bytes(4, 'little'))  # Entry point
        header.extend((0).to_bytes(4, 'little'))  # Program header offset
        header.extend((0).to_bytes(4, 'little'))  # Section header offset
        header.extend((0).to_bytes(4, 'little'))  # Flags
        header.append(0x34)  # Size of this header
        header.append(0)  # Size of program header
        header.append(0)  # Number of program headers
        header.append(0x28)  # Size of section headers
        header.append(len(section_headers) // 40)  # Update for actual number of section headers
        header.append(len(section_headers) // 40 - 1)  # Section header string table index

        if debug:
            print("\nHEADERS:")
            print("\nELF:", b'\x7FELF')
            print("BITS: 1 #32-bit")
            print("ENDIAN: 1")
            print("ELF VERSION: 1")
            print("OS/ABI: 0")
            print("ABI VERISON: 0")
            print("PADDING:", b'\x00' * 7)
            print("TYPE: 2 #RELOCATABLE")
            print("MACHINE: 3 #x86")
            print("VERSION: 1")
            print("ENTRY POINT:", (self.current_addr).to_bytes(4, 'little'))
            print("PROGRAM HEADER OFFSET: ", (0).to_bytes(4, 'little'))
            print("SECTION HEADER OFFSET: ", (0).to_bytes(4, 'little'))
            print("FLAGS:", (0).to_bytes(4, 'little'))
            print("SIZE OF HEADER:", 0x34)
            print("SIZE OF PROGRAM HEADER: 0")
            print("NUMBER OF PROGRAM HEADERS: 0")
            print("SIZE OF SECTION HEADER:", 0x28)
            print("NUMBER OF SECTION HEADERS:", len(section_headers) // 40)
            print("STRING TABLE INDEX:", len(section_headers) // 40 - 1, "\n\n")

        return header

    def add_label(self, label):
        self.labels_addr[label] = self.current_addr
        self.function_addrs[label] = self.current_addr

    def advance_addr(self, size:int):
        self.current_addr += size

    def add_to_text_section(self, code):
        self.text_section.extend(code)

    def add_to_data_section(self, data):
        self.data_section.extend(data)

    def add_to_string_table(self, string:str):
        if string not in self.string_table.decode("utf-8"):
            offset = len(self.string_table)
            self.string_table.extend(string.encode('utf-8') + b'\0')
            return offset
        
        return self.string_table.decode('utf-8').index(string) + 1

    def finalize_elf(self):
        section_headers = bytearray()

        # .strtab section header
        strtab_offset = len(section_headers) + len(self.text_section) + len(self.data_section) + len(self.bss_section)
        section_headers.extend((self.add_to_string_table(".strtab")).to_bytes(4, 'little'))  # Offset in string table
        section_headers.extend((0x03).to_bytes(4, 'little'))  # Type: SHT_STRTAB
        section_headers.extend((0x00).to_bytes(4, 'little'))  # Flags
        section_headers.extend((0).to_bytes(4, 'little'))  # Address
        section_headers.extend((strtab_offset).to_bytes(4, 'little'))  # Offset in file
        section_headers.extend((len(self.string_table)).to_bytes(4, 'little'))  # Size
        section_headers.extend((0).to_bytes(4, 'little'))  # Link
        section_headers.extend((0).to_bytes(4, 'little'))  # Info
        section_headers.extend((0x01).to_bytes(4, 'little'))  # Alignment
        section_headers.extend((0).to_bytes(4, 'little'))  # Entry size

        # .text section header
        section_headers.extend((1).to_bytes(4, 'little'))  # Offset for .text in string table
        section_headers.extend((0x01).to_bytes(4, 'little'))  # Type: SHT_PROGBITS
        section_headers.extend((0x04).to_bytes(4, 'little'))  # Flags: executable
        section_headers.extend((self.current_addr).to_bytes(4, 'little'))  # Address
        section_headers.extend((0).to_bytes(4, 'little'))  # Offset in file (to be set later)
        section_headers.extend((len(self.text_section)).to_bytes(4, 'little'))  # Size
        section_headers.extend((0).to_bytes(4, 'little'))  # Link
        section_headers.extend((0).to_bytes(4, 'little'))  # Info
        section_headers.extend((0x04).to_bytes(4, 'little'))  # Alignment
        section_headers.extend((0).to_bytes(4, 'little'))  # Entry size

        # .data section header
        section_headers.extend((6).to_bytes(4, 'little'))  # Offset for .data in string table
        section_headers.extend((0x01).to_bytes(4, 'little'))  # Type: SHT_PROGBITS
        section_headers.extend((0x02).to_bytes(4, 'little'))  # Flags: writable
        section_headers.extend((self.current_addr + len(self.text_section)).to_bytes(4, 'little'))  # Address
        section_headers.extend((0).to_bytes(4, 'little'))  # Offset
        section_headers.extend((len(self.data_section)).to_bytes(4, 'little'))  # Size
        section_headers.extend((0).to_bytes(4, 'little'))  # Link
        section_headers.extend((0).to_bytes(4, 'little'))  # Info
        section_headers.extend((0x04).to_bytes(4, 'little'))  # Alignment
        section_headers.extend((0).to_bytes(4, 'little'))  # Entry size

        # .bss section header
        section_headers.extend((11).to_bytes(4, 'little'))  # Offset for .bss in string table
        section_headers.extend((0x01).to_bytes(4, 'little'))  # Type: SHT_NOBITS
        section_headers.extend((0x02).to_bytes(4, 'little'))  # Flags: writable
        section_headers.extend((self.current_addr + len(self.text_section) + len(self.data_section)).to_bytes(4, 'little'))  # Address
        section_headers.extend((0).to_bytes(4, 'little'))  # Offset
        section_headers.extend((0).to_bytes(4, 'little'))  # Size (0 for .bss)
        section_headers.extend((0).to_bytes(4, 'little'))  # Link
        section_headers.extend((0).to_bytes(4, 'little'))  # Info
        section_headers.extend((0x04).to_bytes(4, 'little'))  # Alignment
        section_headers.extend((0).to_bytes(4, 'little'))  # Entry size

        return section_headers

    def convert_to_o(self, code:str, data_vars:dict):
        opcodes = {
            "mov": {
                "eax": b"\xB8",
                "ebx": b"\xBB",
                "ecx": b"\xB9",
                "edx": b"\xBA",
                "esi": b"\xBE",
                "edi": b"\xBF",
                "ebp": b"\xBD",
                "esp": b"\xBC"
            },
            "add": {
                "eax": b"\x04",  # add eax, imm8
                "ebx": b"\x03",  # add ebx, imm32 (not direct, needs more work)
                "ecx": b"\x01",  # add ecx, imm32
                "edx": b"\x02",  # add edx, imm32
            },
            "sub": {
                "eax": b"\x2D",  # sub eax, imm32
                "ebx": b"\x3D",  # sub ebx, imm32
                "ecx": b"\x3C",  # sub ecx, imm32
                "edx": b"\x3A",  # sub edx, imm32
            },
            "int": b"\xCD",
            "call": b"\xE8"
        }
        
        code_lines = code.splitlines()

        function_addrs = {}
        
        for i, v in enumerate(code_lines):
            line = v.strip()

            if line.endswith(":"):
                self.add_label(line[:-1])
                self.add_to_text_section(f"{line[:-1]}:\n".encode('utf-8'))  # Add the function label
                continue

            code_words = line.split(" ")
            if code_words[0] in opcodes:
                if code_words[0] == "mov":
                    dest = code_words[1].replace(",", "")
                    src = code_words[2].replace(",", "")
                    
                    try:
                        im = int(src)
                        self.add_to_text_section(opcodes["mov"][dest] + im.to_bytes(4, byteorder='little'))
                    except ValueError:
                        if src in data_vars:
                            value = str(data_vars[src])
                            if not value.isdigit() and (not src.startswith('-') and not src[1:].isdigit()):
                                self.add_to_text_section(opcodes["mov"][dest] + value.encode('utf-8'))
                            else:
                                value = int(value)
                                self.add_to_text_section(opcodes["mov"][dest] + value.to_bytes(4, byteorder='little'))
                        else:
                            raise ValueError(f"Error while Compiling into '.o'. Value is not a immediate or a variable!\nLine -> {line}")
                        
                    self.advance_addr(len(opcodes["mov"][dest]) + 4)

                elif code_words[0] == "call":
                    label = code_words[1]
                    if label in function_addrs:
                        offset:int = function_addrs[label] - (self.current_addr + 5)  # 5 for E8 + rel32
                        self.add_to_text_section(opcodes["call"] + offset.to_bytes(4, byteorder='little'))
                        self.advance_addr(len(opcodes["call"]) + 4)

                elif code_words[0] == "int" and (code_words[1] == "80h" or code_words[1] == "0x80"):
                    self.add_to_text_section(opcodes["int"])
                    self.advance_addr(len(opcodes["int"]))

        return self.text_section, self.data_section
