class x86_Linux:
    @staticmethod
    def convert_to_asm(data:str, CompiledLangSet:dict, CompiledLang:dict) -> tuple[str, dict, int]:
        Output_data = ""
        Data_SECTION = {}

        data_lines = data.splitlines()
        temp_lines = ""

        section_text = "section .text\nglobal _start\n"
        section_data = "section .data\n"
        section_bss = "section .bss\n"

        func_list = []

        _start = "_start:\n"

        Include = False
        IncludeName = ""

        for i, v in enumerate(data_lines):
            data_words = v.split(" ")
            
            for index, word in enumerate(data_words):
                DVALUE = ""
                DSIZE = ""
                DNAME = ""

                if Include:
                    CompiledLang["SET"] = CompiledLang["SET"][IncludeName]
                    Include = False

                for index_, INS in enumerate(CompiledLang["SET"].keys()):

                    if CompiledLang["SET"][INS] == "includeFuncs" and "/INCLUDEINS" in INS:
                        split_INS = ''
                        seperator = ''
                        split_word = ''

                        INS = INS.replace("/INCLUDEINS", "")

                        if INS.split("/S")[1] == "":
                            split_INS = INS
                            seperator = None
                            split_word = word
                        else:
                            seperator = INS.split("/S")[1]
                            split_INS = INS.replace("/S", "").replace(seperator, "").split("/*")
                            split_word = data_lines[i].split(seperator)

                        if split_INS[0] in word:
                            for point_index, point_ in enumerate(split_INS):

                                if point_index == 0:
                                    continue

                                if point_ == "DVALUE":
                                    DVALUE = split_word[point_index]

                            for _Index, _Value in enumerate(CompiledLangSet["funcs"][DVALUE]):
                                func_list.append(_Value)

                            IncludeName = DVALUE + "/INCLUDE"
                            DVALUE = ""
                            Include = True
                            break
                        else:
                            raise ValueError("INVALID INCLUDE INSTRUCTION")

                    elif INS.split("/*")[0].replace("/S", "") in word and not "/INCLUDE" in INS:
                        word_s = ''

                        if INS.split("/S")[1] == "":
                            word_s = word
                        else:
                            word_s = v.split(INS.split("/S")[1])

                        INS_ = INS

                        INS = INS.replace("/S", "").replace(" ", "")

                        for index__, point in enumerate(INS.split("/*")):
                            if index__ == 0:
                                pass
                            else:
                                if point == "DVALUE":
                                    DVALUE = word_s[index__]
                                elif point == "DNAME":
                                    DNAME = word_s[index__]
                                elif point == "DSIZE":
                                    DSIZE = word_s[index__]
                                else:
                                    pass
                        
                        if CompiledLang["SET"][INS_] in CompiledLangSet["INSTRUCTION_SET"].keys():
                            _start += CompiledLangSet["INSTRUCTION_SET"][CompiledLang["SET"][INS_]].replace("*%*DNAME*%*", DNAME).replace("*%*DVALUE*%*", DVALUE).replace("*%*DSIZE*%*", DSIZE)
                            if CompiledLang["SET"][INS_] in CompiledLangSet["DATA_SET"].keys():
                                section_data += CompiledLangSet["DATA_SET"][CompiledLang["SET"][INS_]].replace("*%*DNAME*%*", DNAME).replace("*%*DVALUE*%*", DVALUE).replace("*%*DSIZE*%*", DSIZE)
                            
                            if CompiledLang["SET"][INS_] in CompiledLangSet["BSS_SET"].keys():
                                section_bss += CompiledLangSet["BSS_SET"][CompiledLang["SET"][INS_]].replace("*%*DNAME*%*", DNAME).replace("*%*DVALUE*%*", DVALUE).replace("*%*DSIZE*%*", DSIZE)

        _start += CompiledLangSet["S_TEXT_END"]

        func_out = ""

        if _start == "_start:\n":
            raise Exception("Compiled Code doesn't have any Instructions!")

        for i, v in enumerate(func_list):
            func_out += v + "\n"

        # Process Data Section for variable definitions
        for _index, line in enumerate(section_data.splitlines()):
            if _index == 0:
                continue

            if "equ" in line:
                var_name, value_expr = line.split(" equ ")
                var_name = var_name.strip()
                value = ""
                # Calculate the value (currently assumes linear addressing)
                if "$-" in value_expr.replace(" ", ""):
                    value = len(Data_SECTION[value_expr.replace(" ", "").replace("$-", "")])
                else:
                    value = value_expr
                Data_SECTION[var_name] = value
            elif "db" in line:
                Data_SECTION[line.split(' db ')[0]] = line.split(" db ")[1].replace("\"", "")
            elif var_name := line.split()[0]:
                # Handle direct value assignments
                Data_SECTION[var_name] = line

        # Process BSS Section for variable definitions
        for __index, line in enumerate(section_bss.splitlines()):
            if __index == 0:
                continue

            if "resb" in line:
                var_name, value_expr = line.split(" resb ")
                var_name = var_name.strip()
                value = value_expr
                Data_SECTION[var_name] = value
        
        cancelled_sections = 0

        if section_bss != "section .bss\n":
            if section_data != "section .data\n":
                Output_data = f"{section_data}\n{section_bss}\n{section_text}\n{_start}\n{func_out}"
            else:
                Output_data = f"{section_bss}\n{section_text}\n{_start}\n{func_out}"
                cancelled_sections += 1
        else:
            cancelled_sections += 1
            if section_data != "section .data\n":
                Output_data = f"{section_data}\n{section_text}\n{_start}\n{func_out}"
            else:
                Output_data = f"{section_text}\n{_start}\n{func_out}"
                cancelled_sections += 1

        return Output_data, Data_SECTION, cancelled_sections