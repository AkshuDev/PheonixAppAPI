from elftools.elf.elffile import ELFFile

# Load your ELF file
with open('./PLTEC/Tests/test_.o', 'rb') as f:
    elffile = ELFFile(f)

    # Print sections
    for section in elffile.iter_sections():
        print(f'Section: {section.name}, Size: {section.data_size}')

    # Print symbols (functions, variables, etc.)
    # if elffile.has_dwarf_info():
    #     dwarf_info = elffile.get_dwarf_info()
    #     for CU in dwarf_info.iter_CUs():
    #         for die in CU.iter_children():
    #             if die.tag == 'DW_TAG_subprogram':
    #                 print(f'Function: {die.attributes["name"].value}')
