def PLTEC_initCheck() -> None:
    import os
    import json

    DEF_lang = {
        "ELF": "",
        "x86": "",
        "SET": {
            "#include:/*DVALUE/INCLUDEINS/S ": "includeFuncs",
            "BasicIO/INCLUDE": {
                "print:/*DVALUE/*DNAME/S ": "printINS",
                "input:/*DNAME/*DSIZE/S ": "inputINS",
                "clean:/S": "cleanupINS",
                "return:/*DVALUE/S ": "returnINS"
            }
        }
    }

    DEF_LanguageSET = {
        "elf": {
            "x86": {
                "funcs": {
                    "BasicIO": [
                        "print:\nmov eax, 4\nmov ebx, 1\nint 80h\n", 
                        "input:\nmov eax, 3\nmov ebx, 1\nint 80h\n", 
                        "return:\nmov eax, 1\nint 80h\n",
                        "cleanup32:\nxor eax, eax\nxor ebx, ebx\nxor ecx, ecx\nxor edx, edx\nxor esi, esi\nxor ebp, ebp\nret\n"
                    ]
                },
                "INSTRUCTION_SET": {
                    "printINS": "mov ecx, *%*DNAME*%*_pri\nmov edx, *%*DNAME*%*_pri_LEN\ncall print\n",
                    "inputINS": "mov ecx, *%*DNAME*%*_inp\nmov edx, *%*DNAME*%*_inp_LEN\ncall input\n",
                    "returnINS": "mov ebx, *%*DVALUE*%*\ncall return\n",
                    "cleanupINS": "call cleanup32\n"
                },
                "DATA_SET": {
                    "printINS": "*%*DNAME*%*_pri db \"*%*DVALUE*%*\"\n*%*DNAME*%*_pri_LEN equ $ - *%*DNAME*%*_pri\n",
                    "inputINS": "*%*DNAME*%*_inp_LEN equ *%*DSIZE*%*\n"
                },
                "BSS_SET": {
                    "inputINS": "*%*DNAME*%*_inp resb *%*DSIZE*%*\n"
                },
                "S_TEXT_END": ""
            }
        }
    }

    PLTEC = os.path.dirname(os.path.abspath(__file__))

    DL_path = os.path.join(PLTEC, "DEF_lang.json")
    DLS_path = os.path.join(PLTEC, "DEF_LanguageSET.json")

    if not os.path.exists(DL_path):
        with open(DL_path, 'w') as f:
            json.dump(DEF_lang, f)
            f.close()

    if not os.path.exists(DLS_path):
        with open(DLS_path, 'w') as f:
            json.dump(DEF_LanguageSET, f)
            f.close()